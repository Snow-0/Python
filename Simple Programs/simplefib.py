# Fibonacci Sequence
# Series of numbers in which the next number is the sum
# of the two previous numbers


# first to items in the sequence is
# always 0 and 1
num_list = [0, 1]

# asks for user input and converts to an int from string
ans = int(input("Input the number of terms for the Fibonocci Sequence: "))

# Main function
# Takes in user input of number of terms
def fib_seq(term):
    # range() create a sequence of numbers
    # from 1 to term + 1
    # range upper bound is excludes the second number
    for num in range(1, term + 1):
        # adds the current number in the list with the previous number in the list
        # appends the sum to end of list
        num_list.append(num + (num - 1))
    # returns list once desired amount of terms is apended
    return num_list

# ex. input: 5
# return: [0, 1, 1, 3, 5, 7, 9]
# appended 5 new items excluding 0 and 1
print(fib_seq(ans))
