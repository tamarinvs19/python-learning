import logging as log
log.basicConfig(level=log.DEBUG,
				format='%(levelname)s::%(message)s',
				filemode='w')
log.debug('message')