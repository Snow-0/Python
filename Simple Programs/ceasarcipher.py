# Encrypts a word by shifting the ascii of each letter or symbol by 3.
# Requires no parameter.
def encrypt_word():
    encr_word = []
    # Iterates through the word and appends the shifted ascii number to ascii_list
    for letter in word:
        ascii_list.append(ord(letter) + 3)
    # Coverts the ascii into the new encrypted phrase
    for num in ascii_list:
        encr_word.append(chr(num))
    # Joins the list together into a string
    encr_word = "".join(encr_word)
    # Prints the encrypted phrase out
    print(encr_word)


# Decryptes a phrase
# parameter - string


def decrypt_word(encr_word):
    decr_word = []
    # idk what this does
    encr_word = str(word)
    ascii_list = []
    # Decrypts phrase by shifting phrase back three places
    for letter in encr_word:
        ascii_list.append(ord(letter) - 3)
    # converts ascii into the letter
    for num in ascii_list:
        decr_word.append(chr(num))
    # Joins the list into a string
    decr_word = "".join(decr_word)
    # Prints original text
    print(decr_word)


while True:

    ascii_list = []

    ans = input(
        "Would you like to encrypt(e) or decrypt(d) a phrase? Type in q to quit. "
    )

    if ans == "e":
        word = input("Type in the word you want encrypt: ")
        encrypt_word()
    elif ans == "d":
        word = input("Type in the phrase you want to decrypt: ")
        decrypt_word(word)
    elif ans == "q":
        break
    else:
        print("Error, please type in e, d, or q. ")
