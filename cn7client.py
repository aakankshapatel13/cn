import socket

# Create UDP client
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8080)

# Send the first file 'samplevideo.mp4' in chunks
with open('video.mp4', 'rb') as f:
    chunk = f.read(4096)
    while chunk:
        udp_client.sendto(chunk, server_address)
        chunk = f.read(4096)

# Optionally, send another file if needed (uncomment if you want to send another)
with open('audio.mp3', 'rb') as f:
     chunk = f.read(4096)
     while chunk:
         udp_client.sendto(chunk, server_address)
         chunk = f.read(4096)

# Send end of file marker
udp_client.sendto(b'EOF', server_address)
print("File sent successfully.")

# Close the client socket
udp_client.close()