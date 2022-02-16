import socket

HEADERSIZE = 10

print("SERVER STARTED")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg
    print(msg)
    clientsocket.send(bytes(msg, "utf-8"))