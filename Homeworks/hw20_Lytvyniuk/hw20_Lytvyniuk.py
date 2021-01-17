import note_functions as nf
db = [["Yarek", "111", "note1", "note2", "note3"], ["Marek", "222", "note1", "note2", "note3"], ["Pedro", "333", "note1", "note2"]]
print("Hello, this is NotePad 1.0")
command = True
user = ""
while command:
    command = str(input("Type a command:\n"
                        "Create user - [cu]\n"
                        "Log in user - [li]\n"
                        "Read Users - [ru]\n"
                        "Create note - [cn]\n"
                        "Read Notes - [rn]\n"
                        "Update user's note - [un]\n"
                        "Delete  notes - [del]\n"
                        "Update user's note by index - [uni]\n"
                        "Log off user - [lo]\n"
                        "\t\t\t\tor type [e] to exit: "))
    if command == "cu":
        user_name = input("Enter user name: ")
        user_password = input("Enter password: ")
        nf.create_user(db, user_name, user_password)
    elif command == "li":
        user_name = input("Enter user name: ")
        user_password = input("Enter password: ")
        user = nf.user_login(db, user_name, user_password)
    elif command == "ru":
        nf.read_users(db)
    elif command == "cn":
        if user:
            user_note = input("Enter your note: ")
            nf.create_user_note(db, user, user_note)
        else:
            print("You are not logged in, please log in...")
            user_name = input("Enter user name: ")
            user_password = input("Enter password: ")
            user = nf.user_login(db, user_name, user_password)
    elif command == "rn":
        if user:
            nf.read_users_note(db, user)
        else:
            print("You are not logged in, please log in...")
            user_name = input("Enter user name: ")
            user_password = input("Enter password: ")
            user = nf.user_login(db, user_name, user_password)
    elif command == "un":
        if user:
            nf.read_users_note(db, user)
            note_to_update = input("Enter note, which you want to update: ")
            new_user_note = input("Enter new note: ")
            nf.update_user_note(db, user, note_to_update, new_user_note)
        else:
            print("You are not logged in, please log in...")
            user_name = input("Enter user name: ")
            user_password = input("Enter password: ")
            user = nf.user_login(db, user_name, user_password)
    elif command == "uni":
        if user:
            nf.read_users_note(db, user)
            note_index = int(input("Enter index of note, which you want to update: "))
            new_user_note = input("Enter new note: ")
            nf.update_user_note_by_index(db, user, note_index, new_user_note)
        else:
            print("You are not logged in, please log in...")
            user_name = input("Enter user name: ")
            user_password = input("Enter password: ")
            user = nf.user_login(db, user_name, user_password)
    elif command == "del":
        if user:
            nf.read_users_note(db, user)
            note_index = int(input("Enter index of note to remove: "))
            nf.delete_note(db, user, note_index)
        else:
            print("You are not logged in, please log in...")
            user_name = input("Enter user name: ")
            user_password = input("Enter password: ")
            user = nf.user_login(db, user_name, user_password)
    elif command == "lo":
        if user:
            print(f"{user} is logged off")
            user = ""
        else:
            print("You are not logged in, please log in...")
            user_name = input("Enter user name: ")
            user_password = input("Enter password: ")
            user = nf.user_login(db, user_name, user_password)
    elif command == "e":
        command = False
    else:
        print("wrong command")

    print("\n")
