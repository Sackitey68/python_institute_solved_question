secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess_number = int(input("Enter an integer number: "))

while guess_number != secret_number:
        print("Ha ha! You're stuck in my loop!")

        # Taking another number from the user
        guess_number = int(input("Enter an integer number: "))

print(secret_number)
print("Well done, muggle! You are free now.")
