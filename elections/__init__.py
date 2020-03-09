import os

import sys
from flask import Flask
from elections.utilities import dateformat

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from elections import upcoming
    app.register_blueprint(upcoming.bp)

    app.jinja_env.filters['dateformat'] = dateformat
    return app


# Add main method so app can be run with debugger in IDE. This is the same as `flask run`
if __name__ == '__main__':
    create_app().run()
