company = {
    "Lytvyniuk Yaroslav": ["0123456789", "email", "worker", "skype"],
}


def find(string_to_find, user_dictionary):
    for key in user_dictionary:
        if string_to_find in key:
            print(key, user_dictionary[key])
        elif string_to_find in user_dictionary[key]:
            print(key, user_dictionary[key])


def add(user_dictionary, user_name, *args):
    user_dictionary[user_name] = list(args)


# add(company, "Lytvyniuk Yevheniia", "0677092561", "email_1", "admin", "whatsapp")


def del_item(item_to_delete, user_dictionary) -> object:
    for key in user_dictionary:
        if item_to_delete in key:
            return user_dictionary.pop(key)
        elif item_to_delete in user_dictionary[key]:
            return user_dictionary[key].remove(item_to_delete)


def change_data(select_user, item_to_change, new_item, user_dictionary):
    if select_user in user_dictionary:
        print(user_dictionary[select_user])
        for items in user_dictionary[select_user]:
            if items == item_to_change:
               user_dictionary[select_user][user_dictionary[select_user].index(items)] = new_item


def show_info(user_dictionary):
    for key in user_dictionary:
        print(key, user_dictionary[key], end="\n")


user_input = True
while user_input:
    user_input = input("Enter a command:\n\t"
                       "[add] - add user\n\t"
                       "[del] - del user\n\t"
                       "[find] - find user\n\t"
                       "[edit] - edit data\n\t"
                       "[i] - info about users: ")
    if user_input == "add":
        name = input("Enter your name: ")
        tel = input("Enter your phone number: ")
        email = input("Enter your email: ")
        position = input("Enter your position: ")
        skype = input("Enter your skype: ")

        add(company, name, tel, email, position, skype)

    if user_input == "del":
        item_to_delete = input("Enter item to delete from user list: ")
        del_item(item_to_delete, company)
    if user_input == "find":
        user_search = input("Enter word to find: ")
        find(user_search, company)
    if user_input == "edit":
        user_name = input("Enter user name to start editing: ")
        find(user_name, company)
        item_to_edit = input("Enter item to edit: ")
        new_item = input("Enter new item: ")
        change_data(user_name, item_to_edit, new_item, company)

    if user_input == "i":
        show_info(company)
