def is_fib(fib_list):
    not_fib = False
    for num in range(2, len(fib_list)):
        if fib_list[num] == fib_list[num - 1] + fib_list[num - 2]:
            continue
        else:
            not_fib = True
            break
    if not_fib == False:
        print("Is Fib")
    else:
        print("Not Fib")


is_fib([0, 1, 1, 2, 3, 4, 8])
