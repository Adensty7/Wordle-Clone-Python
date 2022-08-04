import random # For picking a random word
import os # For coloring letters in the terminal
import time

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
letters = []
for w in word:
    letters.append(w)
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

    t = input("WORD: ").upper()
    while t not in words:
        if t not in words:
            print("Word not in list! Try again!")
            t = input("WORD: ").upper()

    f = {}
    f2 = {}
    for j in range(65, 91):
        f[chr(j)] = 0
        f2[chr(j)] = 0

    for w in word:
        f[w] += 1

    bulls = []
    cows = []

    for g in t:
        f2[g] += 1

    for j in range(0, n):
        if t[j] == word[j]:
            bulls.append(j)
            f[t[j]] -= 1
            f2[t[j]] -= 1

    for j in range(0, n):
        if j not in bulls:
            if min(f[t[j]], f2[t[j]]) > 0:
                f[t[j]] -= 1
                f2[t[j]] -= 1
                cows.append(j)

    for j in range(0, n):
        # For each case, different color for the letter
        if j in bulls:
            print(style.GREEN + t[j], end="")
            time.sleep(1)
        elif j in cows:
            print(style.YELLOW + t[j], end="")
            time.sleep(1)
        else:
            print(style.RESET + t[j], end="")
            time.sleep(1)
    print(style.RESET + "")
    if word == t:
        win = 1
        break
    else:
        continue

if win == 1:
    print("You win!!!")
    print(f"You guessed it in {i+1} tries")
else:
    print("You lost!!!")
    print(f"The word was {word}")

