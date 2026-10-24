import pytest
from routes.Routes import Routes
from utils.ConfigReader import ReadConfig
import logging
import os
import requests

#path for log file
log_file= os.path.abspath(os.path.join(os.path.dirname(__file__),"../logs/test_logging.log"))
#create log folder if it does not exist
os.makedirs(os.path.dirname(log_file), exist_ok=True)
#create logger object
logger= logging.getLogger("api_logger")
#set logging level (DEBUG= log everything)
logger.setLevel(logging.DEBUG)

#prevent adding multiple handlers again and again
if not logger.handlers:
    #filehandler==> logs will be saved in file
    file_handler = logging.FileHandler(log_file, mode= 'a')
    #set log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    #apply format to the file handler
    file_handler.setFormatter(formatter)
    #attach filehandler to logger
    logger.addHandler(file_handler)

def log_request_response(response: requests.Response):
    req= response.request
    logger.info(f"Request: {req.method} {req.url}")
    logger.info(f"Request Header: {req.headers}")

    if req.body:
        logger.info(f"Request Body: {req.body}")

    logger.info(f"Response Status: {response.status_code}")
    logger.info(f"Response Headers: {response.headers}")
    try:
        logger.info(f"Response Body: {response.json()}")
    except:
        logger.info(f"Response Body: {response.text}")




@pytest.fixture(scope="class")
def setup():

    #saves original funtion
    #here original requests become requests session
    original_request= requests.Session.request

    #this is our own version of the request() method.
    def custom_request(self, method, url, **kwargs):
        #Call original request
        response = original_request(self, method, url, **kwargs)
        #log request and response
        log_request_response(response)
        return response

    requests.Session.request= custom_request


    yield {"base_url": Routes.Base_url, "config_reader": ReadConfig}