import socket
import select
import threading

class server(object):

    
    # INIT
    def __init__(self, ip='', port=5005, family=socket.AF_INET, type=socket.SOCK_STREAM, min_clients=0, max_clients=0):
        self.ip = ip
        self.port = port
        self.address = (ip, port)
        self.family = family
        self.type = type
        self.min_clients = min_clients
        self.max_clients = max_clients
        
        self.clients = {}


    # START
    # start the server
    def start(self):

        self.sock = socket.socket(family=self.family, type=self.type)
        self.sock.bind(self.address)
        self.sock.listen()

        tAcceptClients = threading.Thread(target=self.accept_clients)

        tAcceptClients.start()


    # ACCEPT CLIENTS
    # accept clients until boundary parameters are met
    def accept_clients(self):

        while True:

            # implement min/max clients later

            client, address = self.sock.accept()

            self.clients[address[1]] = client

            self.send_all ("[SERVER]: client with ip: %s joined server on port: %i" % (address[0], address[1]))

            recv_thread = threading.Thread(target=self.recv, args=([address[1]]))
            recv_thread.daemon = True
            recv_thread.start()
         
            
    # RECV
    # recieve messages from clients
    def recv(self, address):

        while True:
            message = self.clients.get(address).recv(1024).decode("UTF-8")
            self.send_all ("[CLIENT @ %i]: %s" % (address, message))


    # SEND
    # send a specific client a message
    def send(self, client, message):
        client.send(bytes(message, "UTF-8"))


    # SEND ALL
    # send all clients a message
    def send_all(self, message):
        for address in self.clients:
            self.send(self.clients[address], message)