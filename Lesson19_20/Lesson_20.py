# import random
# random_list = []
# even = []
# odd = []
# negative = []
# positive = []
# for i in range(20):
#     random_list.append(random.randint(-99, 99))
# print(random_list)
#
# for num in random_list:
#     if num % 2 == 0:
#         even.append(num)
#     elif num % 2 != 0:
#         odd.append(num)
#     if num > 0:
#         positive.append(num)
#     elif num < 0:
#         negative.append(num)
# print(f"even {even}\nodd{odd}\nnegative{negative}\npositive{positive}")

# Notepad

# Create
# Read
# Update
# Delete

notes = []
name = str(input("Enter your name: "))
notes.insert(0, name)
while True:
    #  Create

    choice = str(input("What you want to do with this note? [add], [upd], [read], [del]: "))
    note = str(input("Enter your note: "))
    if choice == "add":
        notes.append(note)
    elif choice == "read":
        # Read
        for note in notes:
            print(note)
    elif choice == "upd":
        # Update
        # note = str(input("Enter your note which you want to change: "))
        # note1 = str(input("Enter your new note: "))
        # for i in range(len(notes)):
        #     if notes[i] == note:
        #         notes[i] = note1
        #         break

        i = notes.index(note)
        notes[i] = note
    elif choice == "del":
        # Delete
        note = str(input("Enter the note which you want to delete: "))
        notes.remove(note)