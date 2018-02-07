import logging as log

log.basicConfig(level=log.DEBUG,
				format='%(message)s',
				filename='log4.log',
				filemode='w')
log.info('message')
