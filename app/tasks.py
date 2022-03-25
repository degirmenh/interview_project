import time
from logging import getLogger

from app import celery
from db_helper import JobTableDatabaseHelperViaOrm
from exceptions import JobError

logger = getLogger(__name__)


"""
    TASK FUNCTIONS
    ================
    All tasks function call parent function, All task function run as async.

"""


@celery.task
def create_table_task():
    time.sleep(3)
    logger.info(' > Create Table')
    instance  = JobTableDatabaseHelperViaOrm()
    success = instance.create()
    logger.warn('Creation operation successfully finished')
    
@celery.task
def insert_task(name, status):
    logger.info('Insert Job: name: {}, status: {}'.format(name, status))
    instance  = JobTableDatabaseHelperViaOrm()
    success = instance.insert(name, status)
    logger.warn('Insertion operation successfully finished')
    


@celery.task
def insert_from_file_task(file_name):
    # Support only .csv format
    # Prepared temp file for test. This file path temp/job_list_for_insertion.csv
    logger.info('Insert Job From File: file name: {}'.format(file_name))
    instance  = JobTableDatabaseHelperViaOrm()
    success = instance.insert_from_file(file_name)
    logger.warn('Insertion operation successfully finished')


@celery.task
def check_job_status_task(id):
    logger.info('Check job status: job id: {}'.format(id))
    instance  = JobTableDatabaseHelperViaOrm()
    try:
        status = instance.check_status(id)
    except JobError as e:
        logger.error(e)
        return False
    logger.warn('The job is that id of [{}] {}'.format(id, status))
    return True

@celery.task
def delete_job_task(id):
    logger.info('Delete job status: job id: {}'.format(id))
    instance  = JobTableDatabaseHelperViaOrm()
    try:
        status = instance.delete(id)
    except JobError as e:
        logger.error(e)
        return False
    logger.warn('The job (id: {}) deleted'.format(id))
    return True

@celery.task
def valide_job_status_task(id, status):
    logger.info('Check and valide job status: job id: {}'.format(id))
    instance  = JobTableDatabaseHelperViaOrm()
    try:
        success = instance.check_status_value(id, status)
    except JobError as e:
        logger.error(e)
        return False
    logger.warn('Job status validation is [{}]'.format(success))
    return success

@celery.task
def change_status_task(id, status):
    logger.info('> Change job status: job id: {}'.format(id))
    instance  = JobTableDatabaseHelperViaOrm()
    try:
        success = instance.change_status(id, status)
    except JobError as e:
        logger.error(e)
        return False
    logger.warn('Job status changed. [{}]'.format(success))
    return success


@celery.task
def job_list_task():
    logger.info('> Change job status: job id: {}'.format(id))
    instance  = JobTableDatabaseHelperViaOrm()
    job_list = instance.get_list()
    print(job_list)