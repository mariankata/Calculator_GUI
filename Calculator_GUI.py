from Tkinter import *
import tkMessageBox

# crate a window
window = Tk()

# give a title to the window
window.title("calculator")


# make a function for the + button
def plusB_click():
    try:
        num_1 = float(f1.get())
        num_2 = float(f2.get())
        plus_result = num_1 + num_2
        tkMessageBox.showinfo("result", plus_result)
    except ValueError:
        return


# make a funktion for the - button
def minusB_click():
    try:
        num_1 = float(f1.get())
        num_2 = float(f2.get())
        minus_result = float(num_1 - num_2)
        tkMessageBox.showinfo("result", minus_result)
    except ValueError:
        return


# make a funktion for the * button
def timesB_click():
    try:
        num_1 = float(f1.get())
        num_2 = float(f2.get())
        times_result = float(num_1 * num_2)
        tkMessageBox.showinfo("result", times_result)
    except ValueError:
        return


# make a funktion for the / button
def divideB_click():
    try:
        num_1 = float(f1.get())
        num_2 = float(f2.get())
        divide_result = float(num_1 / num_2)
        tkMessageBox.showinfo("result", divide_result)
    except ValueError:
        return


# label 1
l1 = Label(window, text="Enter first number here:")
l1.grid(row=0, sticky=E)


# label 2
l2 = Label(window, text="Enter second number here:")
l2.grid(row=1, sticky=E)


# field 1
f1 = Entry(window)
f1.grid(row=0, column=1)


# field 2
f2 = Entry(window)
f2.grid(row=1, column=1)


# + button
plusB = Button(window, text="+", command=plusB_click)
plusB.grid(row=0, column=2)


# - button
minusB = Button(window, text="-", command=minusB_click)
minusB.grid(row=1, column=2)


# * button
timesB = Button(window, text="*", command=timesB_click)
timesB.grid(row=0, column=3)


# / button
divideB = Button(window, text="/", command=divideB_click)
divideB.grid(row=1, column=3)






window.mainloop()