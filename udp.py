import socket

UDP_IP = "230.0.0.1"
UDP_PORT = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print "received message:", data
