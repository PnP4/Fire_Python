# Echo server program
import socket
import thread

def handleserver(conn,addr):
    while True:
        data = conn.recv(1024)
        # if not data: break
        conn.sendall(data)

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    thread.start_new_thread(handleserver, (conn,addr,))
    print('Connected by', addr)
