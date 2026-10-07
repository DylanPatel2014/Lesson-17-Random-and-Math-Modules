import random
playing=True
number=str(random.randint(0,9))
print("I am generating a number between 0 and 9 so you can try and guess it, Good luck.")
while playing:
    guess=input("Please guess your first number, give your best.")
    if guess==number:
        print("Good job, you guessed the correct number which is",number)
        break
    else:
        print("Sorry you guessed the wrong number, try again:")