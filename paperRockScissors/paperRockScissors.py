import random

computer_choce = random.randint(0, 2)
user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(f"User's choice is {user_choice} \nComputer's choice is {computer_choce}")

if not (0 <= user_choice <= 2):
    print("Invalid number")

elif user_choice == computer_choce:
    print("Draw")

elif user_choice == 0 and computer_choce == 2:
    print("Congratulations🎉, You won")

elif user_choice == 2 and computer_choce == 0:
    print("Opps😒, You lose")

elif computer_choce > user_choice:
    print("Opps😒, You lose")

elif user_choice > computer_choce:
    print("Congratulations🎉, You won")
