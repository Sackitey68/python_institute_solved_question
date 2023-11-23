import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

gameImage = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(f"User's choice is {gameImage[user_choice]} \nComputer's choice is {gameImage[computer_choice]}")

if not (0 <= user_choice <= 2):
    print("Invalid number")

elif user_choice == computer_choice:
    print("Draw")

elif user_choice == 0 and computer_choice == 2:
    print("Congratulations🎉, You won")

elif user_choice == 2 and computer_choice == 0:
    print("Opps😒, You lose")

elif computer_choice > user_choice:
    print("Opps😒, You lose")

elif user_choice > computer_choice:
    print("Congratulations🎉, You won")
    
