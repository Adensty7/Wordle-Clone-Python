import random # For picking a random word
import os # For coloring letters in the terminal

# System call
# os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# letters = [chr(i) for i in range(65, 91)] # A to Z in a list
# print(letters)

# Reading from a file containing 5000+ 5 letter-words and storing them in a list
words = []
with open("5_letter_words.txt") as words_file: # Using this method, we do not need to close the file
    for line in words_file:  # Reading a file using a for loop
        words.append(line.rstrip().upper())

# print(words)
# word = ""

# Picking a random word from the list
word = random.choice(words)

# Variable for win
win = 0

# n = int(input("Enter no of letters:"))

# No. of letters
n = 5
# for i in range(0, n):
    # word += random.choice(letters)


# print(word)

# For n letters, n+1 tries
for i in range(0, n+1):
    # Taking input word and checking if any letter or whole word matches
    t = input("WORD: ")

    for j in range(0, n):
        # For each case, different color for the letter
        if word[j] == t[j]:
            print(style.GREEN + t[j], end="")
        elif word[j] != t[j] and t[j] in word:
            print(style.YELLOW + t[j], end="")
        else:
            print(style.RESET + t[j], end="")
    print(style.RESET + "")
    if word == t:
        win = 1
        break
    else:
        continue

if win == 1:
    print("You win!!!")
else:
    print("You lost!!!")
    print(f"The word was {word}")

