import sys
from time import sleep

import server
import client
import chat_gui


UDP_IP = '127.0.0.1'
UDP_PORT = 5005

PLAYERS = {}
MIN_PLAYERS = 2

def main():

    print ("would you like to start a server? y/n")
    response = input(">> ").lower()
    if (response == "y" or response == "yes"):
        sock_server = server.server(ip=UDP_IP, port=UDP_PORT, min_clients=1)
        sock_server.start()

    sock_client = client.client(ip=UDP_IP, port=UDP_PORT, timeout=0.5)
    sock_client.start()

    while True:
        sleep(1)


    # handle client closing
    # handle host closing




if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt:
        sys.exit

