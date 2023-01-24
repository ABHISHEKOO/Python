def program():
    f = open("intro.txt","w")
    line1=input("enter the text:")
    line2=input("enter the text:")
    line3=input("enter the text:")
    new_line="\n"
    f.write(line1)
    f.write(new_line)
    f.write(line2)
    f.write(new_line)
    f.write(line3)
    f.write(new_line)
    f.close()
program()