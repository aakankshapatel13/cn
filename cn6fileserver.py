import socket

host = "127.0.0.1"
port = 12000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

with open('Myfile2.txt', 'wb') as f:  # Open file using 'with' statement
    print('New file created')
    
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            break
        print(data)  # Print received data (optional)
        if data.decode("utf-8") == "Now":  # Check if the termination message is received
            break
        f.write(data)  # Write received data to the file

print('File is successfully received!!!')

# Open the file again to read and display its contents
with open('Myfile2.txt', 'r') as f:
    print(f.read())  # Correctly print the content

sock.close()  # Close the socket
print('Connection closed!')
