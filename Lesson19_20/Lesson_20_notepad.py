user_notes = [['Andrey',2345],['Sten',433],['Ben',4567]]
note_index = 0
while True:
    command = str(input("Enter command :\n [NEW] - create user\n"
                        " [SELECT] - select user\n"
                        " [create] - create note\n"
                        " [read] - read notes\n"
                        " [update] - update note\n"
                        " [delete] - delete note\n : "))
    #NEW
    if command == 'NEW':
        name = str(input("Enter your name : "))
        check = True
        for i in range(len(user_notes)):
            if name in user_notes[i]:
                check = False
        if check:
            notes = list()
            notes.insert(0,name)
            user_notes.append(notes)
    if command == 'SELECT':
        name = str(input("Enter your name : "))
        for i in range(len(user_notes)):
            if name in user_notes[i]:
                note_index = i
                break
    if command == 'SHOW':
        for i in range(len(user_notes)):
            print(f'User index {i} User {user_notes[i][0]}')
    #Create
    if command == 'create':
        note = str(input("Enter your note : "))
        user_notes[note_index].append(note)

    #Read
    elif command == 'read':
        for note in user_notes[note_index]:
            print(note)

    #Update
    elif command == 'update':
        note = str(input("Enter your note what you want change : "))
        note1 = str(input("Enter your new note : "))
        # for i in range(len(notes)):
        #     if notes[i] == note:
        #         notes[i] = note1
        #         break

        i = user_notes[note_index].index(note)
        user_notes[note_index][i] = note1

    #Delete
    elif command == 'delete':
        note = str(input("Enter your note what you want delete : "))
        user_notes[note_index].remove(note)