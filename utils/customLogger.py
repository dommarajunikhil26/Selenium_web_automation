import inspect
import logging
import os
import allure

def customLogger():
    logName = inspect.stack()[1][3]
    logger = logging.getLogger(logName)
    logger.setLevel(logging.DEBUG)
    
    log_directory = os.path.join(os.path.dirname(__file__), '..', 'reports')
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    log_path = os.path.join(log_directory, "TestLogs.log")
    fileHandler = logging.FileHandler(log_path, mode="a")
    fileHandler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger

def allureLogs(text):
    with allure.step(text):
        pass
