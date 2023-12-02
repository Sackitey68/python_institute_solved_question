import random
import hangman_stages
import names

print("Let's play hangman🤠🤠")

# word_list = ["apple", "beautiful", "potato"]
lives = 6
chosen_word = random.choice(names.names)
# print(chosen_word)

display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)

game_over = False

while not game_over:
    guessed_word = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_word:
            display[position] = guessed_word
    print(display)
    if guessed_word not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You Win!!")

    print(hangman_stages.stages[6-lives])
