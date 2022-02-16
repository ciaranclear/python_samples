import pdb

def add(x, y):
    sum = x + y
    return sum

def main():
    x = int(input("ENter X:"))
    y = int(input("ENter Y:"))
    pdb.set_trace()
    sum = add(x, y)
    print("X + Y = ", sum)

if __name__ == "__main__":
    x = int(input("Enter X:"))
    y = int(input("Enter Y:"))
    sum = add(x, y)
    print("X + Y = ", sum)
