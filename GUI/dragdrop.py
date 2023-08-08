a=[]
size=int(input("enter size of the array:"))
for i in range(size):
    e=int(input("enter element of the array: "))
    a.append(e)
f=0
t=int(input("Enter element to be search:"))
for i in range(size):
    if (a[i]==t):
        f=1
        break
if f==1:
    print(f'the position of element in array:{i}:',t)
else:
    print('Element is not in the array:')
