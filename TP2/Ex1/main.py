from client.client import client
from server.server import server
import sys, getopt

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:p:", ["address=", "port="])
        if not args:
            raise ValueError
    except ValueError:
        print("main.py -p <port> -a <address>")
        sys.exit(2)
    except getopt.GetoptError:
        print("main.py -p <port> -a <address>")
        sys.exit(2)

    try:
        address = args[0]
        port = int(args[1])
        if port not in range(0, 65536):
            raise ValueError("Le port doit être un entier entre 0 et 65535")
    except ValueError as err:
        print(err)
    else:
        server(port)
        client(address, port)
    