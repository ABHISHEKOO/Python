import re
f1=open("input.txt",'r')
f2=open("output.txt",'w')
for line in f1:
    items=re.findall("[6-9]\d{9}",line)
    for n in items:
        f2.write(n+"\n")
print("data extracted succesfully")
f1.close()
f2.close()