import logging

LOGGERS = {}
DEFAULT_HANDLER = None

DEFAULT_PATH = 'logs/'
DEFAULT_LEVEL = 'INFO'
DEFAULT_FILE_NAME = 'app'
DEFAULT_FORMATER = logging.Formatter(
    '%(asctime)s - %(name)s (%(process)d) - %(levelname)s - %(message)s')
