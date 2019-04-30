from tkinter import *

#initialize the root window
root = Tk()


#############################
# 10. Dropdown Menu
#############################


# initialize menu

def someFunc():
    print("This is some function")


mainMenu = Menu(root)
root.configure(menu=mainMenu)

subMenu = Menu(mainMenu)

mainMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Some Func", command=someFunc)
subMenu.add_separator()
subMenu.add_command(label="New tab", command=someFunc)


# Keep the window runing until user closes it
root.mainloop()

#18  TkinterProject/1_label.py
#@@ -0,0 +1,18 @@
#from tkinter import *


#initialize the root window
root = Tk()
#######################
# 1. Adding label
######################
tk_label = Label(root, text="This is a label")
# If we run it right away, there is nothing showing
# we have to add it by doing this
tk_label.pack()

second_label = Label(root, text="This is a second label")
second_label.pack()

# Keep the window runing until user closes it
root.mainloop()
