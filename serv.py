import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_port = 12000
    server_socket.bind(('localhost', server_port))

    server_socket.listen(1)  
    print("Servidor iniciado! | Aguardando conexões...")

    while True:
        connection, client_address = server_socket.accept()
        print(f"Conectado a {client_address}")

        try:
            while True:
                data = connection.recv(1024)
                if data:
                    message = data.decode()
                    print(f"Recebido: {message}")
                    
                    connection.sendall(message.encode())
                else:
                    break  
        finally: 
            connection.close()


start_server()
