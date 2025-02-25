import os
import socket

FLAG = os.getenv('FLAG', 'Not Found')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen(1)

client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

try:
  FLAG_hex = "( *｀ω´)\n"
  client_socket.send(b"Enter a value: ")
  user_input = client_socket.recv(1024).decode().strip()
  FLAG_hex = hex(int(user_input))

  if FLAG_hex[2] == 'f':
    if FLAG_hex[5] == '9':
      if FLAG_hex[4] == 'a':
        if FLAG_hex[3] == '1':
          client_socket.send(f"{FLAG}\n".encode())

except Exception as e:
  client_socket.send(b"Invalid value\n")
finally:
  client_socket.send(FLAG_hex.encode('utf-8') + b"\n")
  client_socket.send(b"bye\n")
  client_socket.close()