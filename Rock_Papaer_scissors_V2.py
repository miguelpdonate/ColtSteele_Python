from random import randint
player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins <= winning_score and computer_wins <= winning_score: 
    print(f"Player Score: {player_wins}  Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("Player 1 , make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else: 
        computer = "scissors"
    print(f"\ncomputer plays: {computer}")


    if player == computer:
        print("it's a tie")

    if player == "rock":
        if computer == "scissors":
            print("player1 wins!")
            player_wins += 1
        elif computer == "paper":
            print("computer wins!")
            computer_wins += 1

    elif player == "paper":
        if computer == "rock":
            print("player1 wins!")
            player_wins += 1
        elif computer == "scissors":
            print("computer wins!")
            computer_wins += 1

    elif player == "scissors":
        if computer == "paper":
            print("player1 wins!")
            player_wins += 1
        elif computer == "rock":
            print("ncomputer wins!")
            computer_wins += 1

    else:
        print("something went wrong")

if player_wins > computer_wins:
    print("Congrats you won!!")
elif player_wins == computer_wins:
    print("it's a tie!!")
else:
    print("This computer is probably cheating anyways...")
print(f"FINAL SCORES..... Player Score: {player_wins}  Computer Score: {computer_wins}")
