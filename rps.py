from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

print("Enter your choice")
input_player = input()

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
elif input_player[0].upper() == "R" and input_computer[0].upper() == "S":
    print("You win!")
elif input_player[0].upper() == "S" and input_computer[0].upper() == "P":
    print("You win!")
else:
    print("Computer wins!")
