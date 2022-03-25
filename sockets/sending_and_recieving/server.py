import socket

# a socket is an endpoint to send and recieve information

print("SERVER STARTED")
# AF_INET is for IP4
# SOCK_STREAM is for TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# gethostname gets the hostname of this machine
# 1234 is the port number
s.bind((socket.gethostname(), 1234))

# listens for information with a que of 5
s.listen(5)

while True:
    # store client socket object and IP address
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    # send information to the client socket object
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
