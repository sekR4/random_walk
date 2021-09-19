# doku:
# https://logzero.readthedocs.io/en/latest/
# https://opensource.com/article/20/2/logzero-python
# https://anaconda.org/conda-forge/logzero

from logzero import logger, logfile
import os

# 1. Define where to store your logfile
path = os.path.dirname(os.path.abspath(__file__))
log=path +'/testlog.log'
logfile(log)
# infos/prints will appear in the log AFTER defining the file
logger.info(log) # ~ print(?)

# print('\n See different logging levels below:')
# logger.debug("hello")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")


logger.debug('wird das weggeschrieben?')
# # This is how you'd log an exception
# try:
#     raise Exception("this is a demo exception")
# except Exception as e:
#     logger.exception(e)
