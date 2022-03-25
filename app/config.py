class LOG_LEVEL_TYPES:
    INFO = 'INFO'
    WARNING = "WARN"   
    ERROR = 'ERROR' 
    
class LoggingHandler:
    CONSOLE = 'console'
    FILE = 'file_handler'
    WSGI = 'wsgi'
    

class Config:
    CELERY_BROKER = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND='redis://localhost:6379'
    LOGGING_FORMAT = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    LOG_LEVEL = LOG_LEVEL_TYPES.INFO
    LOGGING_HANDLER = LoggingHandler.CONSOLE
    SQLALCHEMY_DATABASE_URI = ''  
    


