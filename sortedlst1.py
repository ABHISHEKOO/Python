def insort(ml):
    for i in range(1,len(ml)):
        cv=ml[i]
        p=i
        while cv<ml[p-1] and p>0:
            ml[p]=ml[p-1]
            p=p-1
        ml[p]=cv
        print(ml)
n=int(input("enter size of list  :"))
ml=[]
for i in range(n):
    x=int(input("enter list element :"))
    ml.append(ml)
print("unsorted list is :",ml)
insort(ml)
print('sorted list is :',ml)