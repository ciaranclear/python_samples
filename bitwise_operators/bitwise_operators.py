

n1 = 28
n2 = 19

print(bin(n1))
print(bin(n1)[2:])

print(bin(n2))
print(bin(n2)[2:])

# AND operation using the & operator
n3 = n1 & n2
print(bin(n3)[2:])

# OR operation using the | operator
n4 = n1 | n2
print(bin(n4)[2:])

# XOR operation using ^ operator
n5 = n1 ^ n2
print(bin(n5)[2:])

# NOT operation using ~ operator
print(bin(~n1)) # does not negate the bitmap in python just turns the number negative

# To perform NOT operation in python with bitmap of known length
n6 = 19841
print(bin(n6)[2:])
print("0"+bin(0b111111111111111 - n6)[2:])

# SHIFTS
number = 20
number <<= 1 # shift left multiplies by 2 for each shift
print(number)

number = 20
number >>= 1
print(number)

# Using bits for permissions

person1 = 0b1000
person2 = 0b1100
person3 = 0b1001
person4 = 0b1011
person5 = 0b1101

# get the least permission in common
togeather = person1 & person2 & person3 & person4 & person5
print(bin(togeather))

NEURAL_READ = 0b1000
NEURAL_WRITE = 0b0100
NEURAL_EXEC = 0b0010
NEURAL_CHANGE = 0b0001

def myfunction(permission):
    # combines the permissions
    print(bin(permission))

myfunction(NEURAL_READ | NEURAL_WRITE)

# swap two value using bits
a = 10  # 01010
b = 20  # 10100
print(a, b)

a ^= b  # 11110
b ^= a  # 01010
a ^= b  # 10100
print(a, b)

# check if number is even or odd
somenumber = 128

if somenumber & 1 == 0:
    print("even")
else:
    print("odd")

if __name__ == "__main__":
    pass
