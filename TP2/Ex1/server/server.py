"""
Ce module contient la logique du serveur pour une application de chat.

Il définit deux fonctions principales : `server` et `handler`.

Fonctions
---------
server(host:str, port: int) -> None
    Démarre le serveur sur le port spécifié, accepte les connexions entrantes et lance un thread pour chaque client pour gérer la communication.

handler(connections: dict, conn: socket.socket) -> None
    Gère la communication avec un client spécifique. Si le client envoie "bye", la connexion est fermée. Si le client envoie "arret", une exception KeyboardInterrupt est levée.

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
BrokenPipeError
    Si une erreur de pipe cassé se produit lors de l'envoi d'un message.
Exception
    Si une autre exception est levée.
"""

import socket
import threading

def server(host:str, port:int) -> None:
    connections = {}
    server_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_tcp.bind((host, port))
    server_socket_tcp.listen(1)
    while True:
        try:
            conn, address = server_socket_tcp.accept()
            connections[conn] = address
            client_thread = threading.Thread(target=handler, args=(connections,conn))
            client_thread.start()
        except(socket.gaierror):
            print("Erreur lors de la résolution de l'hôte")
        except(ConnectionRefusedError):
            print("Connexion refusée")
        except(TimeoutError):
            print("Timeout")
        except KeyboardInterrupt:
            print("Serveur en cours d'extinction...")
            for conn in connections:
                conn.close()
            server_socket_tcp.close()
            break
        except Exception as err:
            print(err)

def handler(connections:dict, conn:socket.socket) -> None:
    try:
        data = conn.recv(1024).decode()
        if data == "bye":
            del connections[conn]
            conn.close()
        elif data == "arret":
            raise KeyboardInterrupt
        else:
            for client in connections:
                if client != conn:
                    client.send(data.encode())
    except(ConnectionResetError):
        print("Connexion réinitialisée")
    except(BrokenPipeError):
        print("Rupture de la connexion")

        