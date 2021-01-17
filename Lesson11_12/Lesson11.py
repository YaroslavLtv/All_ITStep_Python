# import random
# player_choice = ''
# bot_choice = ''
# player_score = 0
# bot_score = 0
# # bot_score, player_score = 0,0
#
# for i in range(3):
#     #Choose
#     player_choice = str(input("Enter [r], [p], [s]"))
#     bot_choice = random.choice('rps')
#     #Check
#     if player_choice == bot_choice:
#         print('Draw')
#     elif player_choice == 'r':
#         if bot_choice == 's':
#             player_score = player_score + 1
#         else:
#             bot_score = bot_score + 1
#     elif player_choice == 's':
#         if bot_choice == 'p':
#             player_score = player_score + 1
#         else:
#             bot_score = bot_score + 1
#     elif player_choice == 'p':
#         if bot_choice == 'r':
#             player_score = player_score + 1
#         else:
#             bot_score = bot_score + 1
#     print(f'Your choice : {player_choice}\nBot choice : {bot_choice}')
#     #Final
# if player_score > bot_score:
#     print("You win")
# elif player_score < bot_score:
#     print("You lose")
# else:
#     print("Draw")
import random
start = True
table = 'Name\t\tRounds  \tScore   \tType\n'
while start:
    player_choice = ''
    bot_choice = ''
    player_score = 0
    bot_score = 0
    rounds = int(input("Enter count of rounds : "))
    game_type = ''

    while game_type != 'PvE' and game_type != 'PvP':
        game_type = str(input("Enter type of game : [PvP] or [PvE]"))
    user_name = str(input("User 1 enter your name : "))
    if game_type == 'PvP':
        bot_name = str(input("User 2 enter your name : "))
    else:
        bot_name = 'Bot'

    spaces = 12 - len(user_name)
    user_name = user_name + (" "*spaces)
    spaces = 12 - len(bot_name)
    bot_name = bot_name + (" "*spaces)
    for i in range(rounds):
        #Choose
        player_choice = ''
        while player_choice != 'r' and player_choice != 's' and player_choice != 'p':
            player_choice = str(input("Enter [r], [p], [s] : "))
        if game_type == 'PvP':
            while bot_choice != 'r' and bot_choice != 's' and bot_choice != 'p':
                bot_choice = str(input("Enter [r], [p], [s] : "))
        else:
            bot_choice = random.choice('rps')

        #Check
        if player_choice == bot_choice:
            print('Draw')
        elif player_choice == 'r':
            if bot_choice == 's':
                player_score = player_score + 1
            else:
                bot_score = bot_score + 1
        elif player_choice == 's':
            if bot_choice == 'p':
                player_score = player_score + 1
            else:
                bot_score = bot_score + 1
        elif player_choice == 'p':
            if bot_choice == 'r':
                player_score = player_score + 1
            else:
                bot_score = bot_score + 1
        print(f'{user_name} choice : {player_choice}\n{bot_name} choice : {bot_choice}')
        #Final
    if player_score > bot_score:
        print(f"{user_name} win")
        table = table + f'{user_name}{rounds}   \t\t{player_score}   \t\t{game_type}\n'
    elif player_score < bot_score:
        print(f"{bot_name} win")
        table = table + f'{bot_name}{rounds}   \t\t{bot_score}   \t\t{game_type}\n'
    else:
        print("Draw")
    start = not bool(input("Press [Enter] to continue or [Any key] + [Enter] to exit : "))

print(table)
