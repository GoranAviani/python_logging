import logging

#basic terminal logging
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')


#increasing loging level to include debug and info
'''
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
logging.info('This will also get loged now')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''

#basic logging to a file
#logging.basicConfig(filename='logging_file.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.warning('This will get logged to a file')


#Formatting the Output
#logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
#logging.warning('This is a Warning')


#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
#logging.info('Admin logged in')

#custom date and time format
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')


