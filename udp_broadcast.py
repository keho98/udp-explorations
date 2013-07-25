# Send UDP broadcast packets

MYPORT = 7777 

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    data = repr(time.time()) + '\n'
    s.sendto(data, ('230.0.0.1', MYPORT))
    time.sleep(2)
