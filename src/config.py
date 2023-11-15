import os

from dotenv import load_dotenv

import logging

logging.basicConfig(level=logging.INFO, 
                    filename='../scanpatrol.log',
                    format = '%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
                    datefmt='%H:%M:%S')

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')