n=int(input("enter the number\n"))
flag=0
if (n==1):
    print (n,"is a prime number")
else:
    for i in range(2,(n//2)+1):
        if(n%2==0):
            flag=1
            break
if(flag==0):
    print(n,"is a prime number")
else:
    print(n,"is not prime")