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

import socket, threading, queue
from pynput import keyboard

input_queue = queue.Queue()

def client(user:str, host:str, port:int) -> None:
    flag = False
    while not flag:
        try:
            client_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket_tcp.connect((host, port))
            threading.Thread(target=send, args=(client_socket_tcp, user)).start()
            threading.Thread(target=listen, args=(client_socket_tcp,)).start()
        except(socket.gaierror):
            print("Erreur lors de la résolution de l'hôte")
        except(ConnectionRefusedError):
            print("Connexion refusée")
        except(TimeoutError):
            print("Timeout")
        except KeyboardInterrupt as err:
            print("Client en cours d'extinction...")
            if err.args:
                if err.args[0] == "arret":
                    client_socket_tcp.send("arret".encode())
            else:
                client_socket_tcp.send("bye".encode())
            client_socket_tcp.close()
            break
        except Exception as err:
            print(err)

def on_press(key):
    try:
        input_queue.put(key.char) # Essaie de récupérer le caractère associé à la touche
    except AttributeError:
        pass # Touche spéciale (flèches, ctrl, alt, etc.)


def send(socket:socket.socket, user) -> None:
    while True:
        try:
            data = ''
            while not input_queue.empty():  # Tant que la file n'est pas vide
                data += input_queue.get()  # Prend le prochain caractère
            if data == "arret":
                raise KeyboardInterrupt(data)
            elif data == "bye":
                raise KeyboardInterrupt(data)
            elif data:
                socket.send((user+data).encode())
        except(ConnectionResetError):
            print("Connexion réinitialisée")
        except(BrokenPipeError):
            print("Rupture de la connexion")

def listen(socket:socket.socket) -> None:
    while True:
        try:
            data = socket.recv(1024).decode()
            if data:
                print(data)
        except(ConnectionResetError):
            print("Connexion réinitialisée")
        except(BrokenPipeError):
            print("Rupture de la connexion")
