class LOG_LEVEL_TYPES:
    INFO = 'INFO'
    WARN = "WARN"   
    ERROR = 'ERROR' 
    
        
class LoggingHandler:
    CONSOLE = 'console'
    FILE = 'file_handler'
    WSGI = 'wsgi'
    

class Config:
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND='redis://localhost:6379'
    LOGGING_HANDLER = LoggingHandler.FILE
    LOGGING_FORMAT = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    LOG_LEVEL = LOG_LEVEL_TYPES.WARN
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:hedede@localhost:5432/cevizsoft_jobs'
    
    
