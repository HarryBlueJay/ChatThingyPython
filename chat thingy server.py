#import multiprocessing as mp
import socket
import sys
from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
max_clients = 4
clients = [None] * max_clients
server_address = ("localhost", 10000)
print("Starting up on %s port %s" % server_address)
s.bind(server_address)

s.listen(1)
def server(id):
    cid, addr = s.accept()
    clients[id] = cid
    try:
        print("Connection from: ", addr)
        while True:
            data = cid.recv(8192)
            user = cid.recv(8192)
            #print("Received '%s'" % data.decode())
            if data:
                message = ("[" + user.decode() + "]") + ": " + data.decode()
                sendtoall(bytearray(message, "utf-8"))
                sendtoall(user)
            else:
                print("Dried up from", clients[id])
                break
    
    finally:
        #cid.close()
        pass
def sendtoall(message):
    for i in range(max_clients):
        if clients[i] == None:
            return
        clients[i].send(message)
for id in range(max_clients):
    Thread(target=server,args=(id,)).start()