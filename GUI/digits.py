import re
str =input('enter a string :\n')
m=re.search('[0-9]',str)
if m:
    print('string contain digits')
else:
    print('string dose not contain digits')