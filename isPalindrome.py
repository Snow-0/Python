# Simple palindrome checker
word = input("Enter a word to see if it is a palindrome: ")
word_reversed = word[::-1]
if word == word_reversed:
    print("This word is a palindrome!")
else:
    print("This word is not a palindrome!")
