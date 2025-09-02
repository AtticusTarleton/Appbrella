from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import datetime
import click


bp = Blueprint('blog', __name__)


def get_the_date():
    today = datetime.date.today()
    return str(today)


@bp.route('/')
def index():
    date = get_the_date()
    db = get_db()



    preds = db.execute(f'SELECT guess_made, date_made FROM WeatherPredictions WHERE '
                      f'date_made = "{date}"').fetchall()

    if preds == []:
        db.execute('INSERT into WeatherPredictions ("guess_made", "date_made")'
                   f'VALUES ("testing123", "{date}")')

        db.commit()

        preds = db.execute(f'SELECT guess_made, date_made FROM WeatherPredictions WHERE '
                           f'date_made = "{date}"').fetchall()


    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('blog/index.html', preds=preds, posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")
        #will raise a special exception that returns an HTTP status code.
        #It takes an optional message to show with the error, otherwise a default message is used.
        #404 means “Not Found”, and 403 means “Forbidden”. (401 means “Unauthorized”, but you redirect to the login page instead of returning that status

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


def get_pred(id, check_author=True):
    post = get_db().execute(
        'SELECT id, date_made, guess_made'
        ' FROM WeatherPredictions '
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Weather Prediction id {id} doesn't exist.")
        #will raise a special exception that returns an HTTP status code.
        #It takes an optional message to show with the error, otherwise a default message is used.
        #404 means “Not Found”, and 403 means “Forbidden”. (401 means “Unauthorized”, but you redirect to the login page instead of returning that status

    return post

#go back to the update info: https://flask.palletsprojects.com/en/stable/tutorial/blog/
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
# for the weird rule, basically checks for the line before update to be the int ID
# and how you guarantee this is in the HTML code that links to update
@login_required #says we need to be logged in or else use wrapper
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

#this is just within the update realm
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))