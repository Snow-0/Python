import time
# print out an array of all odd numbers that lead up to the nth value inputed by nth user
# eg: if user inputs 10, list: [1,3,5,7,9]

# res = int(input("Input a number: "))

start = time.time()

# # list comprehension method
res = 15
num_list = [num for num in range(res + 1) if num % 2 == 1]
print(num_list)

# res = 15
# num_list = []
# for num in range(res + 1):
#     if num % 2 == 1:
#         num_list.append(num)
# print(num_list)


end = time.time()
print("The execution for this program is: ", end-start)
