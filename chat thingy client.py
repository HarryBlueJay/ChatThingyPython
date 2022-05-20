import socket
import sys
from threading import Thread
port = 10000
max_queue = 10
messages = [None] * max_queue
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
server_address = ("localhost",port)
s.connect(server_address)
def func(username):
    #username = bytearray(input("Input a username: "), "utf-8")
    #username = bytearray(username, "utf-8")
    #s.settimeout(0.5)
    while True:
        try:
            message = input('[' + username.decode() + ']: ')
        except:
            message = "Hello"#input('[' + username.decode() + ']: ')
        byte_message = bytearray(message,'utf-8')
        s.sendall(byte_message)
        s.sendall(username)
        data = s.recv(8192)
        user = s.recv(8192)
        if not user.decode() == username:
            sys.stdout.write("%s\n" % data.decode())
    
    print("Connection terminated.")
    s.close()
        
if __name__ == "__main__":
    try:
        username = bytearray(input("Input a username: "), "utf-8")
        func(username)
    finally:
        print("Server connection offline.")