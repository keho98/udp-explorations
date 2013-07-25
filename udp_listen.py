import select, socket

port = 56833
bufferSize = 75 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))
s.setblocking(0)

while True:
    result = select.select([s], [],[])
    msg = result[0][0].recv(bufferSize)
    print "Message:" + str(msg)

