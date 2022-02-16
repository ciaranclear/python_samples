






if __name__ == "__main__":
    my_binary_number = 0b1101
    print(my_binary_number) # prints 13

    print("Bitwise AND &")
    x = 0b0001 # 1
    y = 0b1001 # 9
    # x & y == 0b0001 or 1
    print(x & y)

    print("Bitwise OR |")
    # x | y == 0b1001 or 9
    print(x | y)

    print("Bitwise XOR ^")
    # x ^ y == 0b1000 or 8
    print(x ^ y)

    print("Bitwise << or >>")
    # shift left 1 bit << 1
    # shift right 1 bit >> 1
    z = 0b1001
    print(z)
    print(z >> 1)
    print(z << 1)

    print(bin(1056072))
    print(0b111111)
