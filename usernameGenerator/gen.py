# Simple username generator

import os 
import random

directory = os.path.dirname(__file__)
adjective_file = os.path.join(directory, 'adjectives.txt')
noun_file = os.path.join(directory, 'english-nouns.txt')


def pick_word():

    # opens the files and reads contents
    with open(adjective_file, "r") as file:
        words = file.read()
        # takes all the words and puts in a list, then selects a random word
        adjective = random.choice(words.split())
        

    with open(noun_file, "r") as file:
        words = file.read()
        noun = random.choice(words.split())
        return adjective, noun


def main():

    # generates three random numbers and turns them into strings
    rand_num = [str(random.randint(0, 9)) for x in range(3)]
    # main loop
    # validates user input and returns a username or quits the program
    while True:
        try:
            user_input =  input("Press g to regenerate username or q to quit: ")
            if user_input == "g":
                chosen_words = pick_word()
                # concatenates the adjective and noun with three numbers
                username = chosen_words[0] + chosen_words[1] + rand_num[0] + rand_num[1] + rand_num[2]
                print(username)
            if user_input == "q":
                break
        except:
            print("Invalid input please try again")


main()