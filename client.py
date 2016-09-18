# Echo client program
import socket
from time import sleep
import sys


HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
soc= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

for i in range(0,10):
    soc.sendall(b'Hello, world -> '+str(i)+"   "+sys.argv[1])
    data = soc.recv(1024)
    print('Received', repr(data))

    sleep(2) # Time in seconds
