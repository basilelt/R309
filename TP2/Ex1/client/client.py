"""
Ce module contient la logique du client pour une application de chat.

Il définit trois fonctions principales : `client`, `send` et `listen`.

Fonctions
---------
client(user:str, host: str, port: int) -> None
    Établit une connexion avec le serveur à l'adresse et au port spécifiés, et lance deux threads pour envoyer et recevoir des messages.

send(socket: socket.socket, user:str) -> None
    Envoie des messages à travers la socket spécifiée. Les messages sont lus à partir de l'entrée standard.

listen(socket: socket.socket) -> None
    Écoute les messages sur la socket spécifiée et les affiche sur la sortie standard.


Lève
------
socket.gaierror
    Si une erreur se produit lors de la résolution de l'hôte.
ConnectionRefusedError
    Si la connexion est refusée.
TimeoutError
    Si une opération de socket dépasse le délai d'attente.
KeyboardInterrupt
    Si l'utilisateur interrompt le programme.
ConnectionResetError
    Si la connexion est réinitialisée pendant l'envoi d'un message.
"""

import socket, threading

flag = False

def client(user:str, host:str, port:int) -> None:
    global flag
    try:
        client_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket_tcp.connect((host, port))
        threading.Thread(target=listen, args=(client_socket_tcp, user)).start()
        send(client_socket_tcp, user)
    except(socket.gaierror):
        flag = True
        print("Erreur lors de la résolution de l'hôte")
    except(ConnectionRefusedError):
        flag = True
        print("Connexion refusée")
    except(TimeoutError):
        flag = True
        print("Timeout")
    except KeyboardInterrupt:
        flag = True
        print("Client en cours d'extinction...")
        client_socket_tcp.send(user + ": " + "bye".encode())
    except Exception as err:
        flag = True
        print(err)
    finally:
        client_socket_tcp.close()
        

def send(socket:socket.socket, user:str) -> None:
    global flag
    try:
        while not flag:
            data = input("Message: ")
            socket.send((user + ": " + data).encode())
    except(ConnectionResetError):
        flag = True
        print("Connexion réinitialisée")
    except(BrokenPipeError):
        flag = True
        print("Rupture de la connexion")

def listen(socket:socket.socket, user:str) -> None:
    global flag
    while not flag:
        try:
            data = socket.recv(1024).decode()
            if data == user + ": " + "arret":
                flag = True
            elif data == user + ": " + "bye":
                flag = True
            print(data)
        except(ConnectionResetError):
            flag = True
            print("Connexion réinitialisée")
        except(BrokenPipeError):
            flag = True
            print("Rupture de la connexion")
