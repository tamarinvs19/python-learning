import logging as log

log.basicConfig(level=log.DEBUG,
				format='%(asctime)s::%(levelname)s::%(message)s',
				filemode='w')

log.info('message')