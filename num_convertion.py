try:
    x = int(input())
    print(bin(x).replace("0b", ""))
    print(oct(x).replace("0o", ""))
    print(hex(x).replace("0x", ""))
except TypeError:
    print("Invalid number")