"""
    This file is project initial file. 
    Configure and setup all tool.
    
    # SetUps:
        - app
        - logger
        - config
        - db
        - celery
"""


from flask import Flask

app = Flask(__name__)


#  set logging config
import logging
from logging.config import dictConfig

from config import LoggingHandler
    
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        LoggingHandler.WSGI: {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        LoggingHandler.FILE:{
            'class' : 'logging.FileHandler',
            'filename' : '/tmp/interview_project.log',
            'formatter': 'default'
        } 
                            
    },
    'root': {
        'level': "INFO",
        'handlers': [LoggingHandler.FILE, LoggingHandler.WSGI]
    }
})


# set app config
try:
    from config_local import Config
except Exception as e:
    # if programmer didn't copy/create config_local.py 
    app.logger.warn('Please copy config file and then set local config')
    from config import Config
finally:
    app.config.from_object(Config())
    
#  set logger level then setting config. If log level doesn't exists config default set WARN
app.logger.setLevel(app.config.get('LOG_LEVEL') or 'WARN')

#  set logger format then setting config. If log level doesn't exists config default set default format
from flask.logging import default_handler
default_handler.setFormatter(app.config.get('LOGGING_FORMAT') or 
                             '[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

# set logging handler
if app.config.get('LOGGING_HANDLER') == LoggingHandler.CONSOLE:
    app.logger.removeHandler(default_handler)


# Set ORM 
db = None

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
    

# import views
from views import index


# set celery
from celery_app import make_celery
celery = make_celery(app)

# import command functions
from commands import *