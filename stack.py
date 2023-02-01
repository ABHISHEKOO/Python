s=[]
def push():
    if len(s)==n:
        print('stack is full')
    else:
        v=int(input('enter no:'))
        s.append(v)
    print(s)
def pop () :
    if not s:
        print('stack is empty')
    else:
        v=s.pop()
        print('remove element',v)
        print(s)
def disp():
    if not s:
        print('stack is full')
    else:
        i=len(s)-1
        while i>=0:
            print(s[i])
            i-=1

n=int(input('enter size:'))
while True:
    print('select option \n1.push \n2.push \n3 display \n4 quit')
    c=int(input('enter choise:'))
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        disp()
    elif c==4:
        break
    else:
        print('invalid code')