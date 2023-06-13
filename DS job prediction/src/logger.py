# logging module, which provides functionality for logging
import logging
# from src.exception import CustomException

# os module, which provides functions for interacting with the operating system.
import os

# It will help us to deal with the date and time
from datetime import datetime

# First we will generate a log file name and then we will create path to directory to store log files
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Basic configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

    