from app import db


class Jobs(db.Model):
    """
    A class used to database model for Job object

    ...

    Attributes
    ----------
    id : int
       unique identity number
    name : str
        the name of the job
    status : str
        job state
    created_date : int
        job creation time

    Methods
    -------
    __repr__(self)
        Prints the job formatted
    """
    
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    status = db.Column(db.String())
    created_date = db.Column(db.DateTime, server_default=db.func.now())
    
    
    
    def __repr__(self) -> str:
        return '{} {} {}'.format(self.id, self.name, self.status)
    