import os

from flask import Flask
# to run: flask --app appbrellaflask run --debug
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'appbrellaflask.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        #overrides the default below if it is passed
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        #lets you use a specific test

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        #creates a path if it does not exist
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db  # imports from folder
    db.init_app(app)  # runs the init function
    # ran: flask --app flaskr init-db     to initialize the database(make the file)