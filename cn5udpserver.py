# udp_server.py
import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 8080))
    print("UDP server listening on port 8080")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Message from {addr}: {data.decode()}")

        response = "Hello from udp server"
        server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    udp_server()
