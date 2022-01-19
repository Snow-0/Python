initial_amount = int(input("What is your initial investment? "))
interest_rate = float(
    input("What is your interest rate in decimal form (i.e 10% = 0.1)? "))
time_of_interest = int(
    input("What is the number of times you will be compounding per year (i.e quarterly = 4, monthly = 12, or yearly = 1)? "))
time = int(
    input("What is the number of years you will save your investment? "))


def compound_calculator():
    ans = initial_amount * (1 + (interest_rate /
                            time_of_interest)) ** (time * time_of_interest)
    print("$" + str(round(ans, 2)))


compound_calculator()
