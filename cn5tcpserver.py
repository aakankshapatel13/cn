# tcp_server.py
import socket

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(1)
    print("TCP server listening on port 8080")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        data = conn.recv(1024).decode()
        print(f"Message from client: {data}")
        
        response = "Hello from tcp server"
        conn.send(response.encode())
        
        conn.close()

if __name__ == "__main__":
    tcp_server()
