import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
load_dotenv()


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE = os.getenv("LOG_FILE", "app/logs/app.log")

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def setup_logger(name: str = "image_analysis_api") -> logging.Logger:
    """
    logger with console and rotating file handler.
    
    Args:
        name (str): Logger name. Defaults to "image_analysis_api".
        
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if not logger.handlers:  
        console_handler = logging.StreamHandler()
        console_handler.setLevel(LOG_LEVEL)
        console_formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        file_handler = RotatingFileHandler(
            LOG_FILE, maxBytes=5*1024*1024, backupCount=3
        )
        file_handler.setLevel(LOG_LEVEL)
        file_handler.setFormatter(console_formatter)
        logger.addHandler(file_handler)

    return logger
