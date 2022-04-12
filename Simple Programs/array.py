# practicing traversing 2d arrays using python intead of java
import random

row = 4
col = 3
# generates a 4x3 2d array with random numbers from 1-15
array = [[random.randint(0, 15) for i in range(row)] for j in range(col)]
print(array)

# row major order
for row in range(0, len(array[0]) - 1 ):
    for col in range(0, len(array[0])): 
        print(array[row][col])

# column major order
for col in range(0, len(array[0])):
    for row in range(0, len(array[0]) - 1):
        print(array[row][col])
    
