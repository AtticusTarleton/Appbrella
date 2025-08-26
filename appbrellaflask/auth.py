import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from appbrellaflask.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
#blueprints organize all this authentication stuff together, then can send that to
#an application, which simplifies things
#__name__ says where the blueprint is defined


#this is a view for the register
@bp.route('/register', methods=('GET', 'POST'))
#assocates /register url with register view function
def register():
    if request.method == 'POST':
        #if user submitted form, the method will be post, so start doing input validation
        username = request.form['username']
        #request.form is a special type of dict mapping submitted form keys and values.
        #The user will input their username and password.
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        #checking the validation
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                #? avoids sql injection attack
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
            #redirects them to new url
            #url_for allows for you to change the url for auth.login without retyping everywhere

        flash(error)
        #flash stores messages to be retrieved when rendering the template

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        #session is a dict that stores data across requests.
        #When validation succeeds, the user’s id is stored in a new session.
        #The data is stored in a cookie that is sent to the browser, and the browser then sends it back with subsequent requests.
        #Flask securely signs the data so that it can’t be tampered with

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
#registers a function that runs before the view function, no matter what URL is requested
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

    #this just sees if a userid is in the session, and if so uses that one

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

#this wraps the old view, requiring a login
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view