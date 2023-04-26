import socket
import sys
from _thread import *

""" Class that represents a Server """
class Server():
    """ Initialize Server Object """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def handle_connection(self, conn):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            conn.sendall(b"PONG!")

    def run(self):
        self.server.bind((self.host, self.port))
        self.server.listen()

        while True:
            conn, addr = self.server.accept()
            start_new_thread(self.handle_connection, (conn,))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ("How to Use: python3 server.py [host] [port]")
        exit()

    # Start server on host & port given by command line
    host = sys.argv[1]
    port = int(sys.argv[2])

    server = Server(host, port)
    server.run()
