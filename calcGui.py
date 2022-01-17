from tkinter import *
import tkinter as tk
from math import *

# basic 4 function +, -, x, /


def add():
    ans = int()


# Display numbers
def output_button(num):
    output.insert(END, num)


def save_input():
    inputs = output.get()

    global number_list
    number_list = inputs


# window
root = Tk()
root.title("Calculator")
# root.geometry("350x500")
# buttons
button9 = tk.Button(text='9', width="3", height="3",
                    command=lambda: output_button(9))
button8 = tk.Button(text='8', width="3", height="3",
                    command=lambda: output_button(8))
button7 = tk.Button(text='7', width="3", height="3",
                    command=lambda: output_button(7))
button6 = tk.Button(text='6', width="3", height="3",
                    command=lambda: output_button(6))
button5 = tk.Button(text='5', width="3", height="3",
                    command=lambda: output_button(5))
button4 = tk.Button(text='4', width="3", height="3",
                    command=lambda: output_button(4))
button3 = tk.Button(text='3', width="3", height="3",
                    command=lambda: output_button(3))
button2 = tk.Button(text='2', width="3", height="3",
                    command=lambda: output_button(2))
button1 = tk.Button(text='1', width="3", height="3",
                    command=lambda: output_button(1))
button0 = tk.Button(text='0', width="10", height="3",
                    command=lambda: output_button(0))
output = Entry(root, width=25)

# percent_button = tk.Button(text='%', width="3", height="3")
# plusneg_button = tk.Button(text='+/=', width="3", height="3")
# decimal_button = tk.Button(text='.', width="3", height="3")
mult_button = tk.Button(text='*', width="3", height="3",
                        command=lambda: output_button(0))
div_button = tk.Button(text='/', width="3", height="3",
                       command=lambda: output_button(0))
sub_button = tk.Button(text='-', width="3", height="3",
                       command=lambda: output_button(0))
add_button = tk.Button(text='+', width="3", height="3",
                       command=lambda: output_button("+"))
equals_button = tk.Button(text='=', width="3", height="3")
clear_button = tk.Button(text='C', width="3", height="3", command=save_input)


# place buttons and output
output.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

button9.grid(row=2, column=2)
button8.grid(row=2, column=1)
button7.grid(row=2, column=0)

button6.grid(row=3, column=2)
button5.grid(row=3, column=1)
button4.grid(row=3, column=0)

button3.grid(row=4, column=2)
button2.grid(row=4, column=1)
button1.grid(row=4, column=0)

button0.grid(row=5, column=0, columnspan=2)
# plusneg_button.grid(row=1, column=1)
# percent_button.grid(row=1, column=2)
# decimal_button.grid(row=5, column=2)


div_button.grid(row=1, column=4)
mult_button.grid(row=2, column=4)
sub_button.grid(row=3, column=4)
add_button.grid(row=4, column=4)

equals_button.grid(row=5, column=4)
clear_button.grid(row=1, column=0)

root.mainloop()

print(number_list)
