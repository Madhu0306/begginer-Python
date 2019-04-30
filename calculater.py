from tkinter import *


#initialize the root window
root = Tk()

#############################
# 3. Layout, Frame
#############################
tk_topFrame = Frame(root)
tk_topFrame.pack()

tk_botFrame = Frame(root)
tk_botFrame.pack(side=BOTTOM)

# Since we have only two frames, and sepcified one is BOTTOM
# Python will understand that the other one is TOP
# If we have more frames, we might have to specify more

button3 = Button(tk_topFrame, text="Button 3", fg="Yellow")
button3.pack(side=RIGHT)

button4 = Button(tk_topFrame, text="Button 4", fg="Purple")
button4.pack(side=LEFT)

button5 = Button(tk_botFrame, text="Button 5", fg="Orange")
button5.pack(side=LEFT)

button6 = Button(tk_botFrame, text="Button 6", fg="Green")
button6.pack(side=RIGHT)

# Keep the window runing until user closes it
root.mainloop()

#33  TkinterProject/4_fill.py
#@@ -0,0 +1,33 @@
from tkinter import *

#initialize the root window
root = Tk()

#############################
# 4. Fill
#############################

#If we resize the window (make it bigger or smaller, the size of the buttons doesn't change)
# Therefore we use fill
button1 = Button(None, text="Button 1", fg="Yellow")
button1.pack()

button2 = Button(None, text="Button 2", fg="Purple")
# fill X axis
button2.pack( fill=X)

button3 = Button(None, text="Button 3", fg="Orange")
# Fill along Y axis
button3.pack(side=RIGHT, fill=Y)

button4 = Button(None, text="Button 4", fg="Green")
button4.pack()







# Keep the window runing until user closes it
root.mainloop()
