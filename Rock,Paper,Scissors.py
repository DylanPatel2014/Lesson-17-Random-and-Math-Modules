import random
while True:
    user_action=input("Please chose one of the options out of rock, paper of scissor:")
    possible_actions=["rock","paper","scissor"]
    computer_choice=(random.choice(possible_actions))
    print("\nYou picked",user_action,"whilst computer picked",computer_choice)
    if user_action==computer_choice:
        print("It is a tie")
    elif user_action=="rock":
        if computer_choice=="paper":
            print("You lose, computer won.")
        else:
            print("You win, computer lose.")
    elif user_action=="paper":
        if computer_choice=="scissor":
            print("You lose, computer won.")
        else:
            print("You win, computer lose.")
    elif user_action=="scissor":
        if computer_choice=="rock":
            print("You lose, computer won.")
        else:
            print("You win, computer lose.")
    answer=input("Enter y if you want to play again otherwise enter n to not play again.")
    if answer=="n":
        break