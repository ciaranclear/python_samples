
import random

# a byte is an 8 bit integer value in range 0 - 255

def randomBytes(size):
    bytes = []
    for x in range(size):
        bytes.append(random.randrange(0,255))
    return bytes

def displayBytes(bytes):
    print("_"*20)
    for index, item in enumerate(bytes, start=1):
        print(f"{index} = {item} ({hex(item)})")
    print("_"*20)

# write bytes to file
def writeBytes(filename, bytes):
    with open(filename, "wb") as file:
        for i in bytes:
            file.write(i.to_bytes(1, byteorder="big"))

# read bytes from file
def readBytes(filename):
    bytes = []
    with open(filename, "rb") as file:
        while True:
            b = file.read(1)
            if not b:
                break
            bytes.append(int.from_bytes, byteorder="big")
        return bytes


outbytes = randomBytes(10)
filename = "text.txt"
writeBytes(filename, outbytes)

b = randomBytes(10)
displayBytes(b)
