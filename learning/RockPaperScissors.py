import random

user_wins = 0
comp_wins = 0

choices = ["rock", "paper", "scissors"]

print("")
print("")
print("")

print("                     Welcome to GENUINE CREATORS")
print("")
print("")
print("")

print("                    CHOOSE ONE OF THE OPTIONS")
print("        1. rock")
print("        2. paper")
print("        3. scissors")
print("        Q : in order to quit the game and get the results")


while True:
    my_choice = input("Your Pick:  ").lower()
    if my_choice == "q":
        break

    if my_choice not in choices:
        continue

    random_choice = random.randint(0, 2)
    # rock = 0, paper = 1, scissor = 2
    computer_choice = choices[random_choice]

    print(f"You have choosed: {my_choice}")
    print(f"The computer has choosed: {computer_choice}")

    if my_choice == "rock" and computer_choice == "scissors":
        print("You win")
        user_wins += 1

    elif my_choice == "scissors" and computer_choice == "paper":
        print("You win")
        user_wins += 1

    elif my_choice == "paper" and computer_choice == "rock":
        print("You win")
        user_wins += 1

    else:
        print("The computer wins")
        comp_wins += 1


print(f"you have won {user_wins} wins")
print(f"the computer has won {comp_wins} wins")
print("Goodbye!! ")
