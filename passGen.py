import random, string

# saving lowercase alphabet, uppercase alphabet, and symbols into string
alphabet = string.ascii_lowercase
up_alphabet = string.ascii_uppercase
symbols = string.punctuation

all_char = alphabet + up_alphabet + symbols
# turns string list
all_char = list(all_char) 

password = []

# asks users to input a intger 
# if the input is an integer, then the while loop breaks 
# the while keeps running when the input cannot be converted to an integer
while True:
    try:
        user_input = int(input("Input the length of password: "))
        break
    except ValueError: 
        print("The input is not an integer. Please try again.") 

# Randomizes the list 
random.shuffle(all_char)  

# determines the length of the password set by the user
# appends each charcter into the password list
for _ in range(user_input):
    password.append(random.choice(all_char))

# joins the list into a string
password = ''.join(password)
print(password)
