import os
import socket

FLAG = os.getenv('FLAG', 'Not Found')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen(1)

while True:
  try:
    client_socket, addr = server_socket.accept()
    client_socket.send(b"Only lowercase alphabets are allowed\n")
    client_socket.send(b"Enter a value: ")
    plain = client_socket.recv(1024).decode().strip()
    Caesar = ""
    for x in plain:
      if 'a' <= x <= 'z':
        Caesar += chr(((ord(x) - ord("a") + 13) % 26) + ord('a'))
      else:
        client_socket.send(b"Invalid value\n")
        raise Exception("Invalid value")

    client_socket.send(b"target value: cryptography\n")
    client_socket.send(b"your value: " + Caesar.encode("utf-8") + b"\n")

    if Caesar == "cryptography":
      client_socket.send(f"{FLAG}\n".encode())
    client_socket.close()
  except Exception as e:
      client_socket.close()