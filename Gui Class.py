



from tkinter import *

root=Tk()
root.geometry("400x400")
title=Label(root,text="form")
title.pack()
n_name=StringVar()
a_age=StringVar()
Label(root,text="enter your name").pack()
name=Entry(root,textvariable=n_name)
name.pack()
Label(root,text="enter your age").pack()
age=Entry(root,textvariable=a_age)
age.pack()
def show(name,age):
    top=Toplevel(root,)
    Label(top,text=(name,age)).pack()

sub=Button(root,text="click me!!",command=lambda:show(n_name.get(),a_age.get()))
sub.pack()

root.mainloop()



