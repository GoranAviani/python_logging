import logging

#basic terminal logging
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')


#increasing loging level to include debug and info
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
logging.info('This will also get loged now')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
