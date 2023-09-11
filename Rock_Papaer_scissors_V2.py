import random

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player 1 , make your move: ")
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else: 
    computer = "scissors"
print(f"computer played {computer}")


if player == computer:
    print("it's a tie")

if player == "rock":
    if computer == "scissors":
        print("player1 wins!")
    elif computer == "paper":
        print("computer wins!")

elif player == "paper":
    if computer == "rock":
        print("player1 wins!")
    elif computer == "scissors":
        print("computer wins!")

elif player == "scissors":
    if computer == "paper":
        print("player1 wins!")
    elif computer == "rock":
        print("computer wins!")

else:
    print("something went wrong")


