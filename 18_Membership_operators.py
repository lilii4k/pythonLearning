word = "apple"

letter=input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}.")
else:
    print(f"{letter} is not in the word.")



grades= {}