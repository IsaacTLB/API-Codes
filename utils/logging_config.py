import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # Create a custom logger
    logger = logging.getLogger()

    # Set the minimum log level for the logger
    logger.setLevel(logging.DEBUG)

    # Create a formatter for log messages
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Console handler for printing log messages to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File handler for writing logs to a file, with log rotation
    file_handler = RotatingFileHandler('app.log', maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)  # Logs all messages (DEBUG and above) to the file
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
