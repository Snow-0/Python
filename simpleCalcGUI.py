from tkinter import *
import tkinter as tk

root = Tk()
root.title("Simple Calculator")

# Adding two numbers


def add():
    blank.delete(0, END)
    num_sum = int(first_num.get()) + int(second_num.get())
    num_sum = str(num_sum)
    blank.insert(0, num_sum)


def quit():
    root.destroy()


first_num = tk.Entry(root, width=25)
second_num = tk.Entry(root, width=25)
blank = tk.Entry(root, width=25)

first_label = tk.Label(root, text="First Number: ").grid(row=0, column=0)
second_label = tk.Label(root, text="Second Number: ").grid(row=1, column=0)
blank_label = tk.Label(root, text="Sum: ").grid(row=2, column=0)

quit_button = tk.Button(root, text="Quit ", command=quit).grid(row=3, column=0)
calculate_button = tk.Button(
    text="Calculate", command=add).grid(row=3, column=2)

first_num.grid(row=0, column=2)
second_num.grid(row=1, column=2)
blank.grid(row=2, column=2)

root.mainloop()
