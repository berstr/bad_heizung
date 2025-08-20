import logging
import os
from enum import Enum

# log = None

class LOG_LEVEL(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

class LOG():

    log = None

    @staticmethod
    def init(log_level:LOG_LEVEL = LOG_LEVEL.WARNING):
        ENV_LOG_LEVEL=os.environ.get("LOG_LEVEL")
        if ENV_LOG_LEVEL == None:
            effective_log_level = log_level.value
        else:
            match ENV_LOG_LEVEL:
                case 'DEBUG' : effective_log_level = LOG_LEVEL.DEBUG.value
                case 'INFO' : effective_log_level = LOG_LEVEL.INFO.value
                case 'WARNING' : effective_log_level = LOG_LEVEL.WARNING.value
                case 'ERROR' : effective_log_level = LOG_LEVEL.ERROR.value
                case 'CRITICAL' : effective_log_level = LOG_LEVEL.CRITICAL.value
                case _ : effective_log_level = log_level.value

        LOG.log = logging.getLogger()
        LOG.log.setLevel(effective_log_level)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(effective_log_level)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        LOG.log.addHandler(console_handler)    

    @staticmethod
    def debug(msg:str):
        LOG.log.debug(msg)

    @staticmethod
    def info(msg:str):
        LOG.log.info(msg)

    @staticmethod
    def warning(msg:str):
        LOG.log.warning(msg)

    @staticmethod
    def error(msg:str):
        LOG.log.error(msg)

    @staticmethod
    def fatal(msg:str):
        LOG.log.fatal(msg)

def init_logger(log_level:LOG_LEVEL = LOG_LEVEL.WARNING):
    global log
    
    __log = logging.getLogger()
    log.setLevel(log_level.value)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    log.addHandler(console_handler)


