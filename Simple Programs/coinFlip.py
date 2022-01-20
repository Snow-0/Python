# simple coin flip program that will tell the total number of heads or tails

import random 

res = int(input("How many times do you want to flip a coin? "))

# declare variables
num = []

count = 0
heads_count = 0 
tails_count = 0 

#a dds the numbers into a list
# increments by one 
while count < res:

    num.append(random.randint(1,2))
    count += 1 

# iterates through the num list; if number is one, add one to the heads_count. 
# If number is two, add one to the tails_count list
for numbers in num: 
    if numbers == 1:
        heads_count += 1 

    else:
        tails_count += 1

# pirnts the total of each
print("Total Heads: " + str(heads_count))
print("Total Tails: " + str(tails_count))

