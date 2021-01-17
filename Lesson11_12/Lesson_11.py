import random

start = False

while not start:
    players_choice = ""
    players_choice2 = ""
    bot_choice = ""
    player_score = 0
    player_score2 = 0
    bot_score = 0
    game_type = str(input("Choose type of game [pvp] or [pvm]"))
    table = "Name      Rounds    Score     Type      "

    if game_type == "pvm":
        players_name = input("Enter your name: ")
        rounds = int(input("Enter count of rounds: "))
        for i in range(rounds):

            # Choose
            players_choice = ""
            while players_choice != "r" and players_choice != "s" and players_choice != "p":
                players_choice = str(input("Enter [r], [p], [s]: "))
            bot_choice = random.choice('rps')
            # Check
            if players_choice == bot_choice:
                print('Draw')
            elif players_choice == "r":
                if bot_choice == "s":
                    player_score = player_score + 1
                else:
                    bot_score = bot_score + 1
            elif players_choice == "s":
                if bot_choice == "p":
                    player_score = player_score + 1
                else:
                    bot_score = bot_score + 1
            elif players_choice == "p":
                if bot_choice == "r":
                    player_score = player_score + 1
                else:
                    bot_score = bot_score + 1
            print(f"{players_name}, your choice: {players_choice}\nBot choice: {bot_choice}")
            # Final
        if player_score > bot_score:
            print(f"{players_name}, you win!")
        elif player_score < bot_score:
            print(f"{players_name}, you loose")
        else:
            print("Draw")
    if game_type == "pvp":

        players_name = input("Enter your name: ")
        players_name2 = input("Enter your friend name: ")
        rounds = int(input("Enter count of rounds: "))
        for i in range(rounds):

            # Choose
            players_choice = ""
            while players_choice != "r" and players_choice != "s" and players_choice != "p":
                players_choice = str(input(f"{players_name}, enter [r], [p], [s]: "))

            while players_choice2 != "r" and players_choice2 != "s" and players_choice2 != "p":
                players_choice2 = str(input(f"{players_name2}, enter [r], [p], [s]: "))
            # Check
            if players_choice == players_choice2:
                print('Draw')
            elif players_choice == "r":
                if players_choice2 == "s":
                    player_score = player_score + 1
                else:
                    player_score2 = player_score2 + 1
            elif players_choice == "s":
                if players_choice2 == "p":
                    player_score = player_score + 1
                else:
                    player_score2 = player_score2 + 1
            elif players_choice == "p":
                if players_choice2 == "r":
                    player_score = player_score + 1
                else:
                    player_score2 = player_score2 + 1
            print(f"{players_name}'s choice: {players_choice}\n{players_name2}'s choice: {players_choice2}")
            # Final

        if player_score > player_score2:
            print(f"{players_name}, you win!")
        elif player_score < player_score2:
            print(f"{players_name}, you loose")
        else:
            print("Draw")
    print(table)



    start = bool(input("Press [Enter] to continue or [Any Key] + [Enter] to exit: "))
