import os
import socket

FLAG = os.getenv('FLAG', 'Not Found')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen(1)

while True:
  try:
    client_socket, addr = server_socket.accept()
    turn = 1
    i = 5
    res = "b_3co_i1r_p0t_i4x{AOXnmzydvM}3h4"
    while(i):
      client_socket.send(res.encode("utf-8"))
      option = f"""
  1. Caesar + {turn}
  2. Shift + {turn}
  3. reverse
  4. exit
  """
      client_socket.send(option.encode("utf-8"))
      client_socket.send(b"Select the option: ")
      user_input = client_socket.recv(1024).decode().strip()

      new = ""
      if(user_input == "1"):
        for x in res:
          if 'a' <= x <= 'z':
            new += chr(((ord(x) - ord("a") + turn) % 26) + ord('a'))
          elif 'A' <= x <= 'Z':
            new += chr(((ord(x) - ord("A") + turn) % 26) + ord('A'))
          else:
            new += x

      elif(user_input == "2"):
        l = list(res)
        l = l[turn:] + l[:turn]
        new = ''.join(l)

      elif(user_input == "3"):
        new = res[::-1]

      else:
        client_socket.send(b"bye\n")
        break

      res = new
      i -= 1
      turn += 1

  except Exception as e:
    client_socket.send(b"Invalid value\n")
  finally:
    client_socket.send(b"Here are the flags created :" + res.encode("utf-8") + b"\n")
    client_socket.close()