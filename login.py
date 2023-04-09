from tkinter import*
from tkinter import messagebox
root=Tk()

root.geometry("600x400")

name_var=StringVar()
passw_var=StringVar()

def login():

    name=name_var.get()
    password=passw_var.get()
    if(name=="Admin" and password=="Amc123"):
        messagebox.showinfo("Login validation","Welcome Admin ....")
    else:
        messagebox.showerror("Login validation","invalid user!!!!")
    name_var.set("")
    passw_var.set("")

name_label = Label(root, text = 'Username', font=('calibre',15,'bold'))
name_entry = Entry(root,textvariable=name_var, font=('calibre',15,'bold'))
passw_lable = Label(root,text=  passw_var, font=('calibre',15,'bold'))
passw_entry = Entry(root, textvariable=passw_var, font=('calibre',15,'bold'),show='*')
sub_btn=Button(root,text ='LOGIN',font=('calibre',15,'bold' ),command=login)

name_label.grid(row=0,column=0,pady=10,padx=25)
name_entry.grid(row=0,column=1)
passw_lable.grid(row=1,pady=10,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1,pady=10)

root.mainloop()

