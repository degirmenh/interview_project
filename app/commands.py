"""
    The file contains all command promt request methods
    
    # Commands:
     - flask create-table
     - flask get-list
     - flask insert <job_name: str> <status: str> 
     - flask insert-from-file <file_name: str>
     - flask check-job-status <id: int>
     - flask delete <id: int> 
     - flask valide-job-status <id: int> <status: str>
     - flask change-status <id: int> <status: str>
"""

import click
from app import app
from exceptions import JobError
from db_helper import JobTableDatabaseHelperViaOrm

from tasks import *


@app.cli.command('create-table')
def create_table():
    create_table_task.apply_async()
    

@app.cli.command('get-list')
def create_table():
    job_list_task.apply_async()
    


@app.cli.command('insert')
@click.argument("name", nargs=1)
@click.argument("status", nargs=1)
def insert(name, status):
    insert_task.apply_async(args=[name, status])
    


@app.cli.command('insert-from-file')
@click.argument("file_name")
def insert_from_file(file_name):
    insert_from_file_task.apply_async(args=[file_name])


@app.cli.command('check-job-status')
@click.argument("id")
def check_job_status(id):
    check_job_status_task.apply_async(args=[id])


@app.cli.command('delete')
@click.argument("id")
def delete_job(id):
    delete_job_task.apply_async(args=[id])



@app.cli.command('valide-job-status')
@click.argument("id", nargs=1)
@click.argument("status", nargs=1)
def valide_job_status(id, status):
    valide_job_status_task.apply_async(args=[id, status])


@app.cli.command('change-status')
@click.argument("id", nargs=1)
@click.argument("status", nargs=1)
def change_status(id, status):
    change_status_task.apply_async(args=[id, status])
