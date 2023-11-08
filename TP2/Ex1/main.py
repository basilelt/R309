from client.client import client
from server.server import server
import sys, getopt

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:a:", ["p=", "a="])
        if not args:
            raise ValueError("main.py -p <port> -a <address>")
    except getopt.GetoptError:
        print("main.py -p <port> -a <address>")
        sys.exit(2)

    try:
        port = int(args[0])
        if port not in range(0, 65536):
            raise ValueError("Le port doit être un entier entre 0 et 65535")
        address = args[1]
    except ValueError:
        print("Le port doit être un entier entre 0 et 65535")
    else:
        server(port)
        client(address, port)
    