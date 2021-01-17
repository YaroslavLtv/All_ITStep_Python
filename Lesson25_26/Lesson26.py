import note_functions as nf
db = []
print("Hello, this is NotePad 1.0")
command = True
while command:
    command = str(input("Type a command:\nCreate user - [cu]\nCreate note - [cn]\nRead Users - [ru]\n"
                        "Read Notes - [rn]\nUpdate user's note - [un]\n"
                        "Update user's note by index - [uni]\n"
                        "\t\t\t\tor type [e] to exit: "))
    if command == "cu":
        nf.create_user(db, str(input("Enter user name: ")))
    elif command == "e":
        command = False
    elif command == "ru":
        nf.read_users(db)
    elif command == "cn":
        nf.create_user_note(db, input("Enter User Name: "), input("Enter your note: "))
    elif command == "rn":
        nf.read_users_note(db, input("Enter user name to read notes"))
    elif command == "un":
        nf.update_user_note(db, input("Enter your name"), input("Enter note, which you want to update"), input("Enter new note"))
    elif command == "uni":
        nf.update_user_note_by_index(db, input("Enter your name"), input("Enter index of note, which you want to update: "), input("Enter new note: "))