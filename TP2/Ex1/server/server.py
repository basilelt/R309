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

import socket, threading, re, time, sys

flag = False
flag2 = False

def server(host:str, port:int) -> None:
    global flag, flag2
    connections = {}
    server_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket_tcp.bind((host, port))
    server_socket_tcp.listen(1)

    try:
        while not flag:
            conn, address = server_socket_tcp.accept()
            connections[conn] = address
            threading.Thread(target=handler, args=(connections,conn,port,host)).start()
    except(socket.gaierror):
        print("Erreur lors de la résolution de l'hôte")
    except(ConnectionRefusedError):
        print("Connexion refusée")
    except(TimeoutError):
        print("Timeout")
    except KeyboardInterrupt:
        print("Serveur en cours d'extinction...")
        flag = True
        flag2 = True
        if connections:
            for conn in connections:
                conn.close()
    except Exception as err:
        print(err)
    finally:
        time.sleep(0.5)
        server_socket_tcp.close()
        sys.exit()

def handler(connections:dict, conn:socket.socket, port:int, host:str) -> None:
    global flag, flag2
    while not flag2:
        try:
            data = conn.recv(1024).decode()

            pattern_bye = r'^.*: bye'
            match_bye = re.search(pattern_bye, data)

            pattern_arret = r'^.*: arret'
            match_arret = re.search(pattern_arret, data)

            if match_bye:
                conn.send(data.encode())
                del connections[conn]
                flag2 = True
            elif match_arret:
                print("Serveur en cours d'extinction...")
                clone = connections.copy()
                for conn in clone:
                    conn.send(data.encode())
                    del connections[conn]
                flag2 = True
                flag = True

                shut_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                shut_socket_tcp.connect((host, port))
                shut_socket_tcp.send(("Server shutdown...").encode())
                shut_socket_tcp.close()
            elif data:
                for client in connections:
                    if client != conn:
                        client.send(data.encode())
        except(ConnectionResetError):
            print("Connexion réinitialisée")
        except(BrokenPipeError):
            print("Rupture de la connexion")

        