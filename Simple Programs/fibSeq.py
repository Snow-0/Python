"""
Fibonocci Sequence program that asks user for the length of sequnce to the
nth term
"""


fib = [0, 1]


while True:
    try:
        ans = int(input("Input the number of terms for the Fibonocci Sequence: "))
        if ans < 0:
            print("Input cannot be negative")
            continue
        else:
            break
    except ValueError:
        print("Invalid Number. Input must be greater than zero.")
    else:
        break


def fib_sequence(term):
    for num in range(1, term + 1):
        fib.append(fib[-1] + fib[-2])
    return fib


print(fib_sequence(ans))
