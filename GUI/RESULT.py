try:
    file=open("Result.txt","w")
    for i in range(5):
        roll_no=int(input('enter roll no of student:'))
        name=input('enter the name of student :')
        cname=input('enter the class:')
        tmarks=int(input('enter the total marks:'))
        data=str(roll_no)+"\t"+name+"\t"+cname+"\t"+str(tmarks)+"\n"
        file.write(data)
    file.close()

except(NameError,ValueError)as ex:
    print("error occured in",ex)
except Exception as e:
    print("error in program",e)
else:
    print("data enterd successfully")
finally:
    print("program is at end...")
    