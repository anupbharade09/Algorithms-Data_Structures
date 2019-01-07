def addBinary(a,b):
    print(bin(int(a, 2) + int(b, 2))[2:])
    return bin(int(a, 2) + int(b, 2))[2:]

addBinary('1010','1011')