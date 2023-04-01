import re 
str=input('enter a string :\n')
m=re.match('this | that',str)
if m:
    print('string starts with this or that')
else:
    print('string dose not stands with this or that')