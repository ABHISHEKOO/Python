n=int(input('enter size of list '))
l=[]
for i in range(n):
    x=int(input('enter list element :'))
    l.append(x)
#print('unsorted list is :',l)
f=0
for i in range(len(l)-1):
    mv=l[i]
    for j in range(i+1,len(l)):
        if l[j]<mv:
            mv=l[j]
            mi=j
            f=l
        #mi=l.index(mmv,i)
    if f==1:
        l[i],l[mi]=l[mi],l[i]
    f=0
    print(l)

print('sorted list is :',l)