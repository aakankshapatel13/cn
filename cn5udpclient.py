# udp_client.py
import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = " udp Hello from client"

    client_socket.sendto(message.encode(), ('127.0.0.1', 8080))

    response, addr = client_socket.recvfrom(1024)
    print(f"Message from server: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    udp_client()
