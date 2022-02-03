# counts the total number of vowels in a string
# can also count the total number for each value

word = "Today is Wednesday"
vowels = ["a", "e", "i", "o", "u"]


def total_vowels(string):
    num_vowels = 0
    for letter in word:
        if letter in vowels:
            num_vowels += 1
    return "Total number of vowels: " + str(num_vowels)


def total_each_vowel(string):
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    for letter in word:
        if letter == "a":
            a_count += 1
        elif letter == "e":
            e_count += 1
        elif letter == "i":
            i_count += 1
        elif letter == "o":
            o_count += 1
        elif letter == "u":
            u_count += 1
        else:
            continue
    print("Total:")
    print("a: " + str(a_count))
    print("e: " + str(e_count))
    print("i: " + str(i_count))
    print("o: " + str(o_count))
    print("u: " + str(u_count))


print(total_vowels(word))
total_each_vowel(word)
