# countries = {'Ukraine': 'Kyiv', 'Poland': 'Warsaw'}
# in_country = input("Enter country name: ")
# change_city = input("Enter a new name of city: ")
# command = ""
#
# while True:
#     command = str(input("Enter command: "))
#     for country in countries:
#         if in_country == country:
#             countries[country] = change_city
#     print(countries)

# eng_ukr = {'dog': 'пес', 'cat': 'кіт', 'fish': 'риба'}
# user_word = input("Enter word to translate: ")
#
# if user_word in eng_ukr:
#     print(eng_ukr[user_word])
# else:
#     for key in eng_ukr:
#         if eng_ukr[key] == user_word:
#             print(key)

basketball_players = {"Michael Jordan": "2.0"}

user_input = True
while user_input:
    user_input = input("Enter a command:\n\t[add] - add players\n\t[del] - del players\n\t"
                       "[find] - find player by name\n\t"
                       "[edit] - edit player's growth by name\n\t"
                       "[i] - info about players: ")
    if user_input == "add":
        player_name = input("Enter player name: ")
        player_growth = input("Enter player growth: ")
        basketball_players[player_name] = player_growth
    if user_input == "del":
        del_player = input("Enter a name of player to delete: ")
        basketball_players.pop(del_player)
    if user_input == "find":
        user_word = input("Enter a player name to find: ")
        if user_word in basketball_players:
            print(user_word, basketball_players[user_word])
        else:
            for key in basketball_players:
                if basketball_players[key] == user_word:
                    print(key)
    if user_input == "edit":
        in_player = input("Enter player name: ")
        change_growth = input("Enter a new growth ")
        for player in basketball_players:
            if player == in_player:
                basketball_players[player] = change_growth

    if user_input == "i":
        print(basketball_players)