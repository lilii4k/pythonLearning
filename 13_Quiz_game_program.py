import time
questions = ("What colour is the sky?: ",
             "Where is Beyonce from?: ",
             "How old am I?: ",
             "Who sings 'Diamonds'?: ",
             "How many diamonds can I mine in 1 second?: ")

options = (("A. Blue", "B. Green", "C. Pink", "D. Orange"),
           ("A. Mars", "B. United Kingdom", "C. USA", "D. Spain"),
           ("A. 22", "B. 23", "C. 20", "D. 21"),
           ("A. Rihanna", "B. Doja Cat", "C. Alex G", "D. Keith Lemon"),
           ("A. 64", "B. 32", "C. 16", "D. 0"))

answers = ("A", "C", "D", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print()
    print(question)
    for option in options[question_num]:
        print(option)
    
    print()
    guess = input("Enter A, B, C, or D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print()
        print("Correct!")
        time.sleep(1)
    else:
        print()
        print("Incorrect...")
        time.sleep(1)
        print()
        print(f"{answers[question_num]} is the correct answer.")
        time.sleep(1)
    
    question_num += 1

print()
print('\033[1m'+f"Your final score is {score}!")
print('\033[0m')