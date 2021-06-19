def gcd(n1,n2):
    if(n2==0):
        return n1
    else:
        return gcd(n2,n1%n2)

if __name__ == '__main__':
    try:
        a=int(input("Enter the 1st no"))
        b=int(input("Enter the 2nd no"))
    except ValueError:
        print("Invalid number")
    else:
        print("GCD value is :"+str(gcd(a,b)))
