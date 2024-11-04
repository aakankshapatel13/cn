import socket

host = "127.0.0.1"
port = 12000
buffer_size = 1024
file_name = 'abc.txt'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open(file_name, 'rb') as f:  # Open file in binary mode
    data = f.read(buffer_size)
    
    while data:
        sock.sendto(data, (host, port))  # Send data to the server
        data = f.read(buffer_size)  # Read the next chunk

# Send termination message
sock.sendto("Now".encode("utf-8"), (host, port))

print(f'File "{file_name}" sent successfully.')
sock.close()  # Close the socket
