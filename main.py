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
---'   ____)____
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

game_choices = [rock, paper, scissors]
player_score = 0
computer_score = 0

print("Let's play Rock, Paper, Scissors! \n")
print("The first player to 10 points wins. \n")

while True:
    selection = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
    )
    print("")

    if selection > 2 or selection < 0:
        print("You chose an incorrect option. Surpise! You lose the game!")
        break
    else:
        player_choice = game_choices[selection]
        print("You chose: \n")
        print(player_choice, "\n")

        computer_choice = random.choice(game_choices)
        print("The computer chose: \n")
        print(computer_choice, "\n")

        if player_choice == computer_choice:
            print(
                f"""
    You tied!
    Player Score: {player_score}
    Computer Score: {computer_score}
                """
            )
        elif player_choice == rock and computer_choice == scissors:
            player_score += 1
            print(
                f"""
    You won!
    Player Score: {player_score}
    Computer Score: {computer_score}
                """
            )
        elif player_choice == rock and computer_choice == paper:
            computer_score += 1
            print(
                f"""
    You lost!
    Player Score: {player_score}
    Computer Score: {computer_score}
                """
            )
        elif player_choice == paper and computer_choice == rock:
            player_score += 1
            print(
                f"""
    You won!
    Player Score: {player_score}
    Computer Score: {computer_score}
                """
            )
        elif player_choice == paper and computer_choice == scissors:
            computer_score += 1
            print(
                f"""
    You lost!
    Player Score: {player_score}
    Computer Score: {computer_score}
                """
            )
        elif player_choice == scissors and computer_choice == paper:
            player_score += 1
            print(
                f"""
    You won!
    Player Score: {player_score}
    Computer Score: {computer_score}
                """
            )
        elif player_choice == scissors and computer_choice == rock:
            computer_score += 1
            print(
                f"""
    You lost!
    Player Score: {player_score}
    Computer Score: {computer_score}
                """
            )

        if player_score == 10:
            print("Congratulations! You won the game!")
            break
        elif computer_score == 10:
            print("The Computer won! Better luck next time!")
            break
