import socket

def server(port):
    try:
        server_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket_tcp.bind(("0.0.0.0", port))
    server_socket_tcp.listen(1)
    conn, address = server_socket_tcp.accept()
    data = conn.recv(1024).decode()
    conn.send(data.encode())
    conn.close()
    