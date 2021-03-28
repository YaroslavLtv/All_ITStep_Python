english_ukr = {"book": "книга"}

user_input = True
while user_input:
    user_input = input("Enter a command:\n\t"
                       "[add] - add words\n\t"
                       "[del] - del words\n\t"
                       "[find] - find word\n\t"
                       "[edit] - edit words\n\t"
                       "[i] - info about dictionary: ")
    if user_input == "add":
        new_en_word = input("Enter english word: ")
        new_ua_word = input("Enter ukrainian word: ")
        english_ukr[new_en_word] = new_ua_word
    if user_input == "del":
        del_word = input("Enter english word to delete: ")
        english_ukr.pop(del_word)
    if user_input == "find":
        user_word = input("Enter word to find: ")
        for key in english_ukr:
            if user_word in key:
                print(english_ukr[key])
        else:
            for key in english_ukr:
                if english_ukr[key] == user_word:
                    print(key)
    if user_input == "edit":
        to_edit = input("Enter word to edit: ")
        change_growth = input("Enter a new growth ")
        for word in english_ukr:
            if word == to_edit:
                english_ukr[word] = to_edit

    if user_input == "i":
        print(english_ukr)