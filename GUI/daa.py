r=int(input("enter raw count"))
c=int(input("enter column count"))
a=[]
for i in range(r):
    t=[]
    for j in range(c):
        v=int(input(f'enter element of {r,c} matrix'))
        t.append(v)
    a.append(t)
# for row_sum.
s=[]
for i in range(r):
    v=0
    for j in range(c):
        v+=a[i][j]
    s.append(v)
print("sum of raw elements")
for i in range(r):
    print(s[i])
#for column sum
s=[]
for i in range(r):
    v=0
    for j in  range(c):
        v+=a[j][i]
    s.append(v)
print('sum of colun elements')
for i in range(r):
    print(s[i])