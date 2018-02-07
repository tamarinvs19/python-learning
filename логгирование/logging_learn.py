import logging as log

log.basicConfig(level=log.DEBUG,
				format='%(levelname)s::%(message)s',
				filename='log1.log',
				filemode='w')

log.debug('message')

'''try:
	1/0
except:
	log.exception('err')
print('fgbs')

log.shutdown()'''