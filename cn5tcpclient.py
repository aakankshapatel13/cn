# tcp_client.py
import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8080))

    message = "Hello from tcp client"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Message from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    tcp_client()
