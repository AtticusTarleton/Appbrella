import sqlite3
from datetime import datetime

import click
from flask import current_app, g
# g is a special object that is unique for each request.
# It is used to store data that might be accessed by multiple functions during the request.
# The connection is stored and reused instead of creating a new connection if get_db is called a second time in the same request


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
#open_resource opens a file relative to the flaskr package,
# which is useful since you won’t necessarily know where that location
# is when deploying the application later


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.') #prints in terminal


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)
#converts time in database to datetime value in python


def init_app(app):
    app.teardown_appcontext(close_db)
    #teardown_appcontext tells python to call this when cleaning up after a response
    app.cli.add_command(init_db_command)
    #add_command tells python to add this as a command