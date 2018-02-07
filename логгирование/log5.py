import logging as log
log.basicConfig(level=log.DEBUG,
			format='%(levelname)s::%(module)s::%(name)s::%(message)s',
			filemode='w')
from log5_1 import one 
from log5_2 import two
one()
two()
log.info('message_main')
