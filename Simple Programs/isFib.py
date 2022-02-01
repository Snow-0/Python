# Fibonacci Sequence
# Series of numbers in which the next number is the sum
# of the two previous numbers


def is_fib(fib_list):
    not_fib = False
    # range()
    # returns a sequence of a given number range from 2 to length of list
    for num in range(2, len(fib_list)):
        # checks if the current item is the sum of the preveious number and
        # the number before that
        # continues through the list if it is
        if fib_list[num] == fib_list[num - 1] + fib_list[num - 2]:
            continue
        # if not
        # code breaks and changes not_fib to false
        else:
            not_fib = True
            break
    # prints different out if the list is a fibonancci or not
    if not_fib == False:
        print("Is Fib")
    else:
        print("Not Fib")


is_fib([0, 1, 1, 2, 3, 5, 8])  # length of list is 7
is_fib([0, 1, 1, 2, 2, 5, 8])
