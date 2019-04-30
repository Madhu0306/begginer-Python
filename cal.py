#
from tkinter import *
root = Tk()
formula = ""
#equation = Stringvar()
equation.set("0")
calculation =Lable(root, texvariable = equation)
calculation.grid(row=0, column=4)
def pressBut(num):
    global formula
    result = str(eval(fomula))
    formula = formula + str (num)
    calculation.set(formula)
def equalbut():
    global formula
    result = str(eval(formula))
#
#
# button1 =Button(root, text="1", padx =15, pady=15, command = lambda: pressBut(1)) #1
# button1.grid(row=1, column=0)
#
# button2= Button(root, text="2" padx=15, pady=15, command = lambda: pressBut(2))   #2
# button2.grid(row=1, column=1)
#
#
#
# button3= Button(root, text="3" padx=15, pady=15,  command = lambda: pressBut(3))  #3
# button3.grid(row=1, column=2)
# #
# button4= Button(root, text="4" padx=15, pady=15, command = lambda: pressBut(4))   #4
# button4.grid(row=2, column=0)
# #
# button5= Button(root, text="5" padx=10, pady=15,  command = lambda: pressBut(5))  #5
# button5.grid(row=2, column=1)
# #
# button6= Button(root, text="6" padx=10, pady=10  command = lambda: pressBut(6))   #6
# button6.grid(row=2, column=2)
# #
# button7= Button(root, text="6" padx=10, pady=10 command = lambda: pressBut(6))    #7
# button7.grid(row=2, column=1)
# #
#
# buttonClear= Button(root, text="C" padx=10, pady=10 command = lambda: pressBut(6))    #8
# buttonClear.grid(row=4, column=6)
#
# buttonEqual= Button(root, text="+" padx =10, pady=10command = lambda: pressBut(6))   #9
# buttonEqual= Button(root, text="+")
#
# button0= Button(root, text="6" padx =10, pady=10command = lambda: pressBut(6))    #+
# button0= Button(root, text="6")
#
# button-= Button(root, text="6" padx =10, pady=10command = lambda: pressBut(6))
# button-= Button(root, text="6")
#
# button*= Button(root, text="6" padx =10, pady=10command = lambda: pressBut(6))
# button*= Button(root, text="6")
#
# button/= Button(root, text="6" padx =10, pady=10command = lambda: pressBut(6))
# button/= Button(root, text="6")
#
# button= Button(root, text="6" padx =10, pady=10command = lambda: pressBut(6))
# button= Button(root, text="6")
#
# button9= Button(root, text="6" padx =10, pady=10command = lambda: pressBut(6))
# button9= Button(root, text="6")
# root.mainloop()



button_1 = Button(root, text="1", command=lambda: buttonPress(1))
button_1.grid(row=1, column=0)

button_2 = Button(root, text="2", command=lambda: buttonPress(2))
button_2.grid(row=1, column=1)

button_3 = Button(root, text="3", command=lambda: buttonPress(3))
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4", command=lambda: buttonPress(4))
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", command=lambda: buttonPress(5))
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", command=lambda: buttonPress(6))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", command=lambda: buttonPress(7))
button_7.grid(row=3, column=0)

button_8 = Button(root, text="8", command=lambda: buttonPress(8))
button_8.grid(row=3, column=1)

button_9 = Button(root, text="9", command=lambda: buttonPress(9))
button_9.grid(row=3, column=2)

button_0 = Button(root, text="0", command=lambda: buttonPress(0))
button_0.grid(row=4, column=0)

button_plus = Button(root, text="+", command=lambda: buttonPress("+"))
button_plus.grid(row=1, column=3)

button_minus = Button(root, text="-", command=lambda: buttonPress("-"))
button_minus.grid(row=2, column=3)

button_multi = Button(root, text="*", command=lambda: buttonPress("*"))
button_multi.grid(row=3, column=3)

button_divide = Button(root, text="/", command=lambda: buttonPress("/"))
button_divide.grid(row=4, column=3)

button_equal = Button(root, text="=", command=equalBut)
button_equal.grid(row=4, column=2)


button_clear = Button(root, text="C", command=clearBut)
button_clear.grid(row=4, column=1)

root.mainloop()
