# import * from tkinter
from tkinter import *
import tkinter

#create window variable
win = Tk() 
win.title("Calculator")
win.geometry("500x400")  
win.resizable(1, 1)
win.configure(bg='#222')

# create expression variable
expression = ""

# functions
def click_btn(num):
    global expression
    expression = expression + str(num)
    input_text.set(expression)



def clear_btn():
    global expression 
    expression = "" 
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

# create input_text. It's equal to StringVar()
 
input_text = StringVar()
 
# Input frame
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black" ,highlightthickness=2)
 
input_frame.pack(side=TOP)

 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10)

# buttons


buttons_frame = Frame(win, width=312, height=272.5, bg="grey")
 
buttons_frame.pack()
 
# first row
 
clear = Button(buttons_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", command = lambda: clear_btn()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 2)
 
# second row
one = Button(buttons_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff" ,command = lambda: click_btn(1)).grid(row = 1, column = 0, padx = 1, pady = 1)
two = Button(buttons_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(2)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
three = Button(buttons_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(3)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
plus = Button(buttons_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command = lambda: click_btn("+")).grid(row = 1, column = 3, padx = 1, pady = 1)
# third row
 
four = Button(buttons_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(buttons_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(buttons_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command = lambda: click_btn("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
seven = Button(buttons_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
eight = Button(buttons_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
nine = Button(buttons_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
multiply = Button(buttons_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command = lambda: click_btn("*")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fifth row
 
zero = Button(buttons_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", command = lambda: click_btn(0)).grid(row = 4, column = 0, padx = 1, pady = 1)
 
point = Button(buttons_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command = lambda: click_btn(".")).grid(row = 4, column = 1, padx = 1, pady = 1)
 
equals = Button(buttons_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command = lambda: bt_equal()).grid(row = 4, column = 2, padx = 1, pady = 1)

divide = Button(buttons_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", command = lambda: click_btn("/")).grid(row = 4, column = 3, padx = 1, pady = 1)
# run app
win.mainloop()