import random
start = True
table = "Name      Rounds    Score     Type\n"

while start:
    player1_choice = ''
    player2_choice = ''
    player1_score = 0
    player2_score = 0
    rounds = int(input("Enter count of rounds: "))
    game_type = ''

    while game_type != "pve" and game_type != "pvp":
        game_type = str(input("Enter type of game : [pvp] or [pve]"))
    player1_name = str(input("User 1 enter your name: "))
    if game_type == "pvp":
        player2_name = str(input("User 2 enter your name: "))
    else:
        player2_name = "Computer"
        
    for i in range(rounds):
        # Choose
        player1_choice = ""
        player2_choice = ""
        while player1_choice != "rock" and player1_choice != "scissors" and player1_choice != "paper" and player1_choice != "lizard" and player1_choice != "spock":
            player1_choice = str(input(f"{player1_name}, enter [rock], [paper], [scissors], [lizard], [spock]: "))
        if game_type == "pvp":
            while player2_choice != "rock" and player2_choice != "scissors" and player2_choice != "paper" and player2_choice != "lizard" and player2_choice != "spock":
                player2_choice = str(input(f"{player2_name}, enter [rock], [paper], [scissors], [lizard], [spock]: "))
        else:
            player2_choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])

        # Check
        if player1_choice == player2_choice:
            print("Draw")
        elif player1_choice == "rock":
            if player2_choice == "scissors" or player2_choice == "lizard":
                player1_score = player1_score + 1
            else:
                player2_score = player2_score + 1
        elif player1_choice == "scissors":
            if player2_choice == "paper" or player2_choice == "lizard":
                player1_score = player1_score + 1
            else:
                player2_score = player2_score + 1
        elif player1_choice == "paper":
            if player2_choice == "rock" or player2_choice == "spock":
                player1_score = player1_score + 1
            else:
                player2_score = player2_score + 1
        elif player1_choice == "lizard":
            if player2_choice == "paper" or player2_choice == "spock":
                player1_score = player1_score + 1
            else:
                player2_score = player2_score + 1
        elif player1_choice == "spock":
            if player2_choice == "rock" or player2_choice == "scissors":
                player1_score = player1_score + 1
            else:
                player2_score = player2_score + 1

        print(f"{player1_name}'s choice: {player1_choice}\n{player2_name}'s choice: {player2_choice}")
        # Final
    if player1_score > player2_score:
        print(f"{player1_name} win")
        table = table + f"{player1_name.ljust(10, ' ')}{str(rounds).ljust(10, ' ')}" \
                        f"{str(player1_score).ljust(10, ' ')}{game_type.ljust(10, ' ')}\n"
    elif player1_score < player2_score:
        print(f"{player2_name} win")
        table = table + f"{player2_name.ljust(10, ' ')}{str(rounds).ljust(10, ' ')}" \
                        f"{str(player2_score).ljust(10, ' ')}{game_type.ljust(10, ' ')}\n"
    else:
        print("Draw")
    start = not bool(input("Press [Enter] to continue or [Any key] + [Enter] to exit : "))

print(table)
