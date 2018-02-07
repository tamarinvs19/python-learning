import logging as log

log.basicConfig(level=log.DEBUG,
				format='%(levelname)s::%(message)s',
				filename='log.log',
				filemode='w')

try:
	1/0
except:
	log.exception('error')

log.shutdown()