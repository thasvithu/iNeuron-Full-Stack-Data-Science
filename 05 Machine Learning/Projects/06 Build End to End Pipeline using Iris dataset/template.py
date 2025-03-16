import os
from pathlib import Path
import logging

# Configure logging at the start
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S %p'
)

def test():
    logging.debug('This will get logged')   
    logging.warning('This will get logged')
    logging.info('This will not get logged')
    logging.error('This will get logged')
    logging.critical('This will get logged')
    logging.debug('This will get logged')   
    logging.warning('This will get logged')
    logging.info('This will not get logged')
    logging.error('This will get logged')
    logging.critical('This will get logged')
    logging.debug('This will get logged')   
    logging.warning('This will get logged')
    logging.info('This will not get logged')
    logging.error('This will get logged')
    logging.critical('This will get logged')



if __name__ == '__main__':
    test()
