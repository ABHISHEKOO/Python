#write  program to peprform opretion seek () ;
f1=open("weekdays.txt","w+")
f1.write("monday\n")
f1.write("tuesday\n")
f1.write("wednessday\n")
f1.write("thursday\n")
f1.write("friday\n")
f1.seek(0)
#print(f1.redd())
f1.seek(0,2)
f1.write("saturdy\n")
f1.write("sunday\n")
f1.seek(0)
print(f1.read())