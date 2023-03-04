def lsearch(l,n,key):
    for i in range(0,n):
        if (l[i]==key):
            return i
n=int(input('enter size of list: '))
l=[]
for i in range(n):
    x=int(input('enter list element :'))
    l.append(x)
print(l)
key=int(input('enter key :'))
r=lsearch(l,n,key)
if r==-1:
    print("key is not foud")
else:
    print("key is found")