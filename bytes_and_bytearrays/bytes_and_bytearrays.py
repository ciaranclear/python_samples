
# A byte is a string of 8 bits

# create a string of empty bytes
empty_bytes = bytes(4)

print(empty_bytes)
print(type(empty_bytes)) # type bytes

# bytes are immutable

# make byte string with values
data_bytes = bytes(b'\xFF\xFF')
print(data_bytes)

# to make mutable bytes use a byte array
mutable_bytes = bytearray(b'\xDE\xAD\xBE\xEF')
mutable_bytes[0] = 0
mutable_bytes.append(255) # 255 is max value for byte and hex value
print(mutable_bytes)
print(type(mutable_bytes))