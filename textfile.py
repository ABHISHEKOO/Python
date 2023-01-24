def program():
    f = open("intro.txt","w")
    text=input("enter the text:")
    f.write(text)
    f.close()
program()