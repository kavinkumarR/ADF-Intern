import time
n=2
while(n):
    f=0
    for i in range(2,n):
        if(n%i==0):
            f=1
            break
    if(f==0):
        print(n)
        time.sleep(5)
    n+=1