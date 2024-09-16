import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_porta = 12000
    client_socket.connect(('localhost', 12000))

    try:
        # Loop para enviar várias mensagens
        while True:
            message = input("Digite uma mensagem ou  digite 'sair' para encerrar: ")
            
            if message.lower() == 'sair':
                print("Encerrando a conexão com o servidor.")
                break
            client_socket.sendall(message.encode())

            data = client_socket.recv(1024)
            print(f"Resposta do servidor: {data.decode()}")
    finally:
        client_socket.close()

start_client()

