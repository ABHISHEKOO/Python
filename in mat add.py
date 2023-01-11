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
b=[ ]
for i in range (r):
    t=[ ]
    for j in range (c):
        v=int(input('entter no'))
        t.append (v)
    b.append (t)
# processing loop.
s=[ ]
for i in range (r):
    t=[ ]
    for j in range (c):
        v=a[i][j]+b[i][j]
        t.append (v)
    s.append (t)
# output loop.
for i in range (r):
    for j in range (c):
        print(a[i][j], end = " ")
    print("  ", '+' , "  ")
# --
    for j in range (c):
        print(b[i][j], end = "  ")
    print("  " , '=' , "  ")
    for j in range (c):
        print(s[i][j], end = "  ")
    print( )