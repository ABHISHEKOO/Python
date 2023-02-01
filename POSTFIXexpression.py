op=set(['+','-','*','/','^','(',')',])
pre={'+':1,'-':1,'*':2,'/':2,'^':3}
def itop(exp):
    st=[]
    s=''
    for ch in exp:
        if ch not in op:
            s+=ch
        elif ch=='(':
            st.append(ch)
        elif ch==')':
            while st and st[-1]!='(':
                s+=st.pop()
            st.pop()
        else:
            while st and st[-1]!='('and pre[ch]<=pre[st[-1]]:
                s+=st.pop()
            st.append(ch)
    while st:
        s+=st.pop()
    return s
exp=input('\nEnter infix expression:')
print('\nPostfix expression is:',itop(exp))