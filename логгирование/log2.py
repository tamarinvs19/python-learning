import logging as log

log.basicConfig(level=log.DEBUG,
				format='%(message)s',
				filemode='w')

try:
	raise RuntimeError
except:
	log.exception('error')

log.shutdown()