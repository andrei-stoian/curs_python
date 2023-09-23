def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (
            (player1_choice == "rock" and player2_choice == "scissors")
            or (player1_choice == "scissors" and player2_choice == "paper")
            or (player1_choice == "paper" and player2_choice == "rock")
    ):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


def main():
    print("Welcome to the Rock-Paper-Scissors game!")
    player1_wins = 0
    player2_wins = 0
    rounds = int(input("Enter the number of rounds: "))

    for round in range(rounds):
        print(f"Round {round + 1}")
        player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
        player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

        result = determine_winner(player1_choice, player2_choice)
        print(result)

        if result == "Player 1 wins!":
            player1_wins += 1
        elif result == "Player 2 wins!":
            player2_wins += 1

    if player1_wins > player2_wins:
        print("Player 1 is the overall winner!")
    elif player2_wins > player1_wins:
        print("Player 2 is the overall winner!")
    else:
        print("It's a tie in the overall game!")


if __name__ == "__main__":
    main()