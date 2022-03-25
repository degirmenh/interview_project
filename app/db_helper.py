import psycopg2
from exceptions import JobError
from models import Jobs
from csv import reader
from app import app, db


class BaseJobTableDatabaseHelper:
    """
        BaseJobTableDatabaseHelper all db operations base class
    """
    
    error_string  = ''

    def create(self) -> bool:
        """
            Create 'jobs' table, return successuction
        
        """
        pass
    
    def insert(self, name: str, status: str) -> bool:
        """
            Insert new job. Then return success or fail (True / False) 
        """
        pass
    
    def insert_via_file(self, file_path: str) -> bool:
        """
            Insert new job from file. Then return success or fail (True / False) 
            If file does not exist return False
        """
        pass
    
    def change_status(self, id: int, new_status: str) -> bool:
        """
            Change exists new job. Then return success or fail (True / False) 
            if job is not exist or new status is not valid return False
        """
        pass
        
    def delete(self, id: int) -> bool:
        """
            Delete exists job. Then return success or fail (True / False) 
            if job is not exist is not valid return False
        """
        pass
    
    def check_status(self, id: int) -> str:
        """
            Check exists job. Return status value
            if job is not exist throw exception
        """
    
    def check_status_value(self, id:int, status: str) -> bool:
        """
            Check exists job. 
            Check job status value is equal to given status.
        """
        
    def get_list() -> list:
        """
            Return all job list
        """
        
    def _write_job_from_file(self, file_path):
        """
            Give a file path. Read file and return dict.
            File format : .csv  name,status
            E.g. File content
                job1,active
                job2,started
            return data:
                [{"name": "job1", "status": "active"}, {"name": "job2", "status": "started" ...}]
            
        """
        result_data = []
        with open(file_path, 'r') as f:
            csv_reader = reader(f)
            
            for row in csv_reader:
                if len(row) != 2:
                    continue
                result_data.append({"name": row[0], "status": row[1]})
        return result_data
        

class JobTableDatabaseHelperViaOrm(BaseJobTableDatabaseHelper):
    
    """
        Derivative from BaseJobTableDatabaseHelper class. The class was specified for Orm Methods
    """
    
    def create(self) -> bool:
        """
            Create table via db object
        """
        db.create_all()
        db.session.commit()
        return True

    def insert(self, name: str, status: str) -> bool:
        job = Jobs(name=name, status=status)
        db.session.add(job)
        db.session.commit()
        return True
    
    
    def insert_from_file(self, file_path: str) -> bool:
        data = self._write_job_from_file(file_path)
        for d in data:
            self.insert(d.get('name'), d.get('status'))
        return True
    
    
    def check_status(self, id: int) -> str:
        try:
            job = self._get_job(id)
        except JobError as e:
            return False
        
        return job.status

    def delete(self, id: int) -> bool:
        try:
            job = self._get_job(id)
        except JobError as e:
            return False
        db.session.delete(job)
        db.session.commit()
        return True
    
    def get_list() -> list:
        job_list = Jobs.query.all()
        return job_list
        
        
    def check_status_value(self, id: int, status: str) -> bool:
        real_status = self.check_status(id)
        return status == real_status
    
    def change_status(self, id: int, new_status: str) -> bool:
        try:
            job = self._get_job(id)
        except JobError as e:
            return False
        job.status = new_status
        db.session.commit()
        return True
    
    def _get_job(self, id:int)-> object:
        job = Jobs.query.get(id)
        if not job:
            message = 'Job could not found.'
            self.error_string = message
            app.logger.error(message)
            raise JobError(message)
        return job

