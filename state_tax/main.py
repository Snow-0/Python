# Calculates tax rate  based on state
# import pandas to read excel sheet and convert to dict
# must install panda and openpyxl
import pandas
import os 
directory = os.path.dirname(__file__)
excel_file = os.path.join(directory, "state_tax_rate.xlsx")
xlsx = pandas.read_excel(excel_file)
file = xlsx.to_dict("dict")

# param{str}
# return{float}
abbrev_states = []
for i in file["Abbreviation"]:
    abbrev_states.append(file["Abbreviation"][i])


def get_tax(state_abbrev):
    for i in file["Abbreviation"]:
        if(file["Abbreviation"][i] == state_abbrev):
            tax_rate = file["Tax Rate"][i]
            return tax_rate

# param{float}
# return{str}


def calculate(get_tax):
    object_inp = float(input("Price of Object(Decimal format): "))
    return "Final Price: $" + str(object_inp + (get_tax*object_inp))

# param{none}
# return{none}


def get_user_input():
    while True:
        try:
            print("type in l to list the states or q to quit. ")
            state_initials = input("Please input state abbreviation in CAPS: ")
            if state_initials in abbrev_states:
                print("You have selected: " + state_initials)
                print(calculate(get_tax(state_initials)))
                break
            elif state_initials == "l":
                print(*abbrev_states, sep="\n")
            elif state_initials == "q":
                break
            else:
                print("Invalid input. Please enter a state. ")
        except:
            continue


get_user_input()
