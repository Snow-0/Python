"""
Simple GUI compound interest calculator 
Uses this forumla to calculate compound interest:
A = P(1 + r / n)^ n * t
A = amount
P = initial amount
r = interest rate (decimal)
t = time (years)
n = number of times compounded per year

"""
import tkinter as tk
from tkinter import *

# Initializes tkinter window
root = Tk()
root.title("Compound Interest Calculator")

""" 
[Summary]
Takes P, r, t, and n from the user and plugs into the compount interest formula.
Then rounds the result by two decimals places and converts the result into a string 
Inserts the result into the Tkinter for the user to see
[Parameters]
None

"""


def compound_calculator():

    blank.delete(0, END)
    init_amount = float(init_invest_entry.get())
    interest_rate = float(interest_rate_entry.get())
    times_of_interest = int(times_of_interest_entry.get())
    time = int(time_entry.get())

    ans = init_amount * (1 + (interest_rate /
                              times_of_interest)) ** (time * times_of_interest)
    ans = "$" + str(round(ans, 2))
    blank.insert(0, ans)

# Quits the program


def quit_calculator():
    root.destroy()


# Entry boxes for user to input the numbers
init_invest_entry = tk.Entry(root, width=25)  # width is size 25
interest_rate_entry = tk.Entry(root, width=25)
time_entry = tk.Entry(root, width=25)
times_of_interest_entry = tk.Entry(root, width=25)
blank = tk.Entry(root, width=25)

init_invest_label = tk.Label(
    root, text="Initial Investment:").grid(row=0, column=0)
interest_rate_label = tk.Label(
    root, text="Interest Rate: ").grid(row=1, column=0)
time_label = tk.Label(
    root, text="Time (how long will you save your money in years)").grid(row=2, column=0)
time_of_interest_label = tk.Label(
    root, text="Compound Frequency (Number of times that interest will be compounds i.e quarterly=4, yearly=1, monthly=12)").grid(row=3, column=0)
result_label = tk.Label(root, text="Result: ").grid(
    row=4, column=0)

calculate_button = tk.Button(
    root, text="Calculate", command=compound_calculator)
quit_button = tk.Button(root, text="Quit", command=quit_calculator)

# Positions the buttons and entry boxes
init_invest_entry.grid(row=0, column=1)
interest_rate_entry.grid(row=1, column=1)
time_entry.grid(row=2, column=1)
times_of_interest_entry.grid(row=3, column=1)
blank.grid(row=4, column=1)
calculate_button.grid(row=5, column=1)
quit_button.grid(row=5, column=0)

# Starts the program
root.mainloop()
