#input loop
r=int(input('enter the row no'))
c=int(input('enter column no'))
a=[ ]
for i in range (r):
    t=[ ]
    for j in range (c):
        v=int(input('enter no'))
        t.append (v)
    a.append(t)
print(a)
b=[ ]
for i in range(r):
    t=[ ]
    for j in range(c):
        v=int(input('enter no'))
        t.append(v)
    b.append (t)
print(b)
# processing loop.
s=[]
for i in range (r):
    t=[]
    for j in range (c):
        t.append
    s.append
for i in range (len(a)):
    for j in range (len(s)):
        for k in range (len(b)):
            s[i][j]+=a[i][j]*b[i][j]
# output loop.
for i in range (r):
    for j in range (c):
        print(a[i] [j],end=" ")
    print("  ", '+' , "  ")
    for j in range (c):
        print(b[i][j],end=" ")
    print("  " , '=' , "  ")
    for j in range (c):
        print(s[i][j], end = " ")
    print()