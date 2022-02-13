# practicing recursion
def factorial(nth):
    if nth == 1:
        return 1
    else:
        return (nth * factorial(nth - 1))


print(factorial(3))
# 1st call factorial(3)
# 3 * factorial(2)
# 3 * 2 * factorial(1)
# 3 * 2 * 1 returns 1 as the number
# return 2nd call 3 * 2
# return 1st call 6
