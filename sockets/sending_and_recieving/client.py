import socket

print("CLIENT STARTED")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# size of data chunks you want to recieve
s.connect((socket.gethostname(), 1234))

full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)

