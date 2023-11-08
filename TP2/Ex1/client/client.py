import socket

def client(address, port):
    client_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket_tcp.connect((address, port))
    client_socket_tcp.send("Hello, World!".encode())
    data = client_socket_tcp.recv(1024).decode()
    client_socket_tcp.close()