from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"You: {player_wins} vs computer: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    print("Enter your choice")
    input_player = input()

    if input_player[0].upper() == "Q":
        break

    input_computer = ['Rock', 'Paper', 'Scissors'][randint(0, 2)]
    print(input_computer)

    print("SHOOT!")

    if input_player[0].upper() != "P" \
            and input_player[0].upper() != "R" \
            and input_player[0].upper() != "S" \
            and input_player.upper() != "PAPER" \
            and input_player.upper() != "ROCK" \
            and input_player.upper() != "SCISSORS":
        print("Invalid input")
    elif input_player[0].upper() == input_computer[0].upper():
        print("It's a tie.")
    elif input_player[0].upper() == "P" and input_computer[0].upper() == "R":
        print("You win!")
        player_wins += 1
    elif input_player[0].upper() == "R" and input_computer[0].upper() == "S":
        print("You win!")
        player_wins += 1
    elif input_player[0].upper() == "S" and input_computer[0].upper() == "P":
        print("You win!")
        player_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

if player_wins > computer_wins:
    print("Congratz!")
elif player_wins == computer_wins:
    print("Bye")
else:
    print("Bummer!")
