import os
filename=input('enter the filename:')
ans=os.path.isfile(filename)
if ans:
    f=open(filename,'r')
    data=f.read()
    print(data)
    f.seek(len(data)-19)
    lines=f.read()
    print("\n last 20 characters of the file: ",lines)
else:
    print("file dose not exist !")