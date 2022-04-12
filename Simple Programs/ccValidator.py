# simple credit card validator that uses the Luhn algoritim 
# read more: https://www.sapling.com/7966257/checksum-credit-card

# user_input = input("Enter a credit card number: ")
card_num = "4578423013769219"
inv_card_num = "4578423013769291"

def validator(credit_card_num):
    """_summary_
    Uses the luhn algorithim checks if the card number is valid

    Args:
        credit_card_num (string): user input

    Returns:
        string: returns a string that says if its valid or not
    """
    # turns the string into a list
    num_list = [int(num) for num in credit_card_num]
    # removes the last number from the list
    last_num = num_list.pop()

    # iterates every second digit
    for num in range(0, len(num_list), 2):
        total = 0 # this is to keep track of the sum of a two digit number
        num_list[num] *= 2
        # checks if a number has two digits 
        if num_list[num] >= 10:
            # if the index has a two digit number
            # add the digits to get a 1 digit sum
            for digit in str(num_list[num]):
                total += int(digit)
                # reassign that to the index
                num_list[num] = total
    # calculates the sum
    res = sum(num_list) + last_num
    # checks if the sum is a multiple of ten
    if res % 10 == 0: 
        return "This is a valid credit card number"
    return "This is an invalid credit card number"

print(validator(card_num))
print(validator(inv_card_num))
print(validator(user_input))

