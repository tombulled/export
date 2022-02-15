pre = None
post = None

pre = set(locals().keys())

from lib import *

post = set(locals().keys())

print('Exported:', pre ^ post)