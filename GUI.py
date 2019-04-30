from tkinter import *
win = Tk() # Tk is a class,castracter


#mylable = Label(win,text = "GUI") #win means a window
#mylable.pack()
# topFrame = Frame(win)
# topFrame.pack()
# bottomframe = Frame(win)
# bottomframe.pack(side=BOTTOM)

#win.geometry("200")
def fun():
    print("Welcome to knowledge")
    print("M")


# entry_1 = Entey(win)
# entry_2 = Entey(win)
# entry_3 = Entey(win)
#
# check = Checkbutton()

# lable = Label(win, text= "Red", bg="Blue", fg="white")
# lable.pack()
#
# lable1 = Label(win, text= "Black", bg="Blue", fg="white")
# lable1.pack(fill=X)
#
# lable2 = Label(win, text= "Red", bg="red", fg="pink")
# lable2.pack(side=LEFT,fill=X)
#
# lable3 = Label(win, text= "Red", bg="yellow", fg="blue")
# lable3.pack(side=RIGHT,fill=Y)
button = Button(win, text ="click me", command = fun)
#button = Button(win, text ="click me")
button.pack()

# button1 = Button(topFrame,text="Button1",fg="red")
# button2 = Button(topFrame,text="Button2",fg="yellow")
# button3 = Button(topFrame,text="Button3",fg="pink")
# button4 = Button(bottomframe,text="Button4",fg="orange")
#
# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack(side=LEFT)
# button4.pack(side=RIGHT)
win.mainloop()
