# This script should log my progress in practicing coding
import os
from logzero import logger, logfile

class log_me(object):

    def __init__(self, file):
        self.file = file

    def start_logging(self):
        self.path = os.path.dirname(os.path.abspath(self.file))
        logfile(self.path + '/main.log')
        logger.info('\n Starting logging at\n {}\n for {}'.format(self.path,self.file))
        # logger.info(self.file)

def lprint(string):
    logger.info(string)

def start_logging(file):
    path = os.path.dirname(os.path.abspath(file))
    logfile(path + '/main.log')
    logger.info('\n Starting logging at\n {}\n for {}'.format(path,file))
