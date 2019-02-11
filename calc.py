from tkinter import *

op = Tk()
expression=""
def sum(number):
    global expression
    expression=expression+str(number)
    a.set(expression)

def equals_to():
    global expression
    total=str(eval(expression))
    a.set(total)
    expression=""

def clear():
    global expression
    expression=""
    a.set("")

op.geometry("260x250")
op.resizable(False,False)
title = Label(op,text="calculator")
title.grid()

a=StringVar()
display= Entry(op,bd=9,font=("",17),width=15,textvariable=a)
display.grid(row=1,column=0,padx=9,pady=9,rowspan=1,columnspan=15)


b1= Button(op,text="1",bd=8,font=("",10),width=5, command =lambda:sum(1) )
b1.grid(row=2,column=0)
b2= Button(op,text="2",bd=8,font=("",10),width=5,command = lambda:sum(2))
b2.grid(row=2,column=1)
b3= Button(op,text="3",bd=8,font=("",10),width=5,command = lambda:sum(3))
b3.grid(row=2,column=2)

b4= Button(op,text="4",bd=8,font=("",10),width=5 , command= lambda:sum(4))
b4.grid(row=3,column=0)
b5= Button(op,text="5",bd=8,font=("",10),width=5, command= lambda:sum(5))
b5.grid(row=3,column=1)
b6= Button(op,text="6",bd=8,font=("",10),width=5, command= lambda:sum(6))
b6.grid(row=3,column=2)

b7= Button(op,text="7",bd=8,font=("",10),width=5, command= lambda:sum(7))
b7.grid(row=4,column=0)
b8= Button(op,text="8",bd=8,font=("",10),width=5, command= lambda:sum(8))
b8.grid(row=4,column=1)
b9= Button(op,text="9",bd=8,font=("",10),width=5, command= lambda:sum(9))
b9.grid(row=4,column=2)

plus= Button(op,text="+",bd=8,font=("",10),width=5, command= lambda:sum("+"))
plus.grid(row=2,column=3)
minus= Button(op,text="-",bd=8,font=("",10),width=5, command= lambda:sum("-"))
minus.grid(row=3,column=3)
division= Button(op,text="/",bd=8,font=("",10),width=5, command= lambda:sum("/"))
division.grid(row=4,column=3)

multiplication= Button(op,text="*",bd=8,font=("",10),width=5, command= lambda:sum("*"))
multiplication.grid(row=5,column=0)
equals = Button(op,text="=",bd=8,font=("",10),width=5,command= lambda:equals_to())
equals.grid(row=5,column=2)
clr= Button(op,text="C",bd=8,bg="red",font=("",10),width=5,command= lambda:clear())
clr.grid(row=5,column=3)
zero= Button(op,text="0",bd=8,font=("",10),width=5,command= lambda:sum("0"))
zero.grid(row=5,column=1)


op.mainloop()