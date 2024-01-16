import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response = data.decode('utf-8').upper()
        client_socket.send(response.encode('utf-8'))
    client_socket.close()

def start_echo_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 65432))
    server.listen(5)
    print("[INFO] Server listening on port 8080")

    while True:
        client_socket, addr = server.accept()
        print(f"[INFO] Accepted connection from {addr}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_echo_server()
