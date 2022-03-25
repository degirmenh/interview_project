"""
    NOTE: This file manages migrations
    
    This code copied from https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc
    
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

import models

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()