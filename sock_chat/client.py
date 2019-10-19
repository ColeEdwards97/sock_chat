import sys
import select
import socket
import threading

import chat_gui

from random import randint

class client(object):
    

    # INIT
    def __init__(self, ip, port, family=socket.AF_INET, type=socket.SOCK_STREAM, timeout=None):
        self.ip = ip
        self.port = port
        self.address = (ip, port)
        self.family = family
        self.type = type
        self.timeout = timeout


    # START
    # starts the client
    def start(self):

        self.sock = socket.socket(self.family, self.type)
        self.sock.settimeout(self.timeout)

        try:
            self.sock.connect(self.address)
            print ("[CLIENT]: connected to: %s on port %i" % (self.ip, self.port))
        except:
            print ("[CLIENT]: connection refused")
            pass

        self.tRecv = threading.Thread(target=self.recv)
        self.tRecv.daemon = True
        self.tRecv.start()

        self.gui = chat_gui.chat_gui(self.sock)

    # RECV
    # recieve data
    def recv(self):

        while True:
            try:
                data = self.sock.recv(1024).decode("UTF-8")
                self.gui.push_message(data)
            except:
                pass


    # SEND
    # send data to server
    def send(self, message):
        self.sock.send(message.encode("UTF-8"))

