#ivri korem 2020
"""
description
"""

#init
#importing
from tkinter import *
import tkinter.font as font
import time


#setting the gui
root = Tk()
root.title('calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#setting var
comp = 0 #comparison, Add=1, Multiplie=2, Divide=3, blank = 0
firstNum = 0

def buttonClick(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def Clear():
    global comp
    comp = 0
    e.delete(0, END)

def Equal():
    global comp 
    secondNum = float(int(e.get()))
    if comp == 1:
        Clear()
        e.insert(0, firstNum + secondNum)
    elif comp == 2:
        Clear()
        e.insert(0, firstNum * secondNum)
    elif comp == 3:
        Clear()
        e.insert(0, firstNum / secondNum)

def Add():
    global comp 
    global firstNum
    firstNum = float(e.get())
    print(firstNum)
    Clear()
    comp = 1
    
def Multiplie():
    global comp 
    global firstNum
    firstNum = float(e.get())
    print(firstNum)
    Clear()
    comp = 2

def Divide():
    global comp 
    global firstNum
    firstNum = float(e.get())
    print(firstNum)
    Clear()
    comp = 3

#define the buttons
button_1 = Button(root,text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button_2 = Button(root,text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button_3 = Button(root,text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button_4 = Button(root,text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button_5 = Button(root,text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button_6 = Button(root,text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button_7 = Button(root,text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button_8 = Button(root,text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button_9 = Button(root,text="9", padx=40, pady=20, command=lambda: buttonClick(9))

button_0 = Button(root,text="0", padx=40, pady=20, command=lambda: buttonClick(0))
button_clear = Button(root,text="C", padx=40, pady=20, command=Clear, fg='black', bg='orange')
button_equal = Button(root,text="=", padx=40, pady=20, command=Equal, fg='black', bg='orange')

button_add = Button(root,text="+", padx=40, pady=20, command=Add, fg='white', bg='black')
button_multiplie = Button(root,text="X", padx=40, pady=20, command=Multiplie, fg='white', bg='black')
button_divide = Button(root,text="%", padx=40, pady=20, command=Divide, fg='white', bg='black')

#display the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_add.grid(row=5, column=0)
button_multiplie.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

#main loop
root.mainloop()