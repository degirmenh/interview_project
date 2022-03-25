# InterviewProject

This project created for interview case project. 
Project Goals:
    Jobs menagement via console

Enviorments:
==============
    Python version: 3.9
    Flask Version: 1.1.2
    OS: MacOs
    Database: PostgreSQL

Requirements:
===============
     #. Python 3.9
     #. Postgres Server
     

## Getting started

    Installation server or local machine
    =========================================

    brew install python
    brew install postgresql
    brew install postgresql-contrib
    brew install postgresql

    ## Create Enviroment and Set up
    ========================================
    pip install virtualenv
    virtualenv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    cd app
    set FLASK_APP=app
    flask run


    # open the terminal and run command (be sure redis running cmd: redis-server)
    celery -A app.celery worker

## Add your files
    cd app
    cp config.py config_local.py
    # set to local config 

