# Task 6
# def prime_num(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#         return True
#
# print(prime_num(50))

# Task 7
# def lucky_num(num):
#     part1 = 0
#     part2 = 0
#     string_num = str(num)
#     for i in range(len(string_num) // 2):
#         part1 = part1 + int(string_num[i])
#     for j in range(len(string_num) // 2):
#         part2 = part2 + int(string_num[-i])
#     if part1 == part2:
#         return True
#     else:
#         return False
# print(lucky_num(723422))

# Notebook
notes = []

def add_note(notes, note):
    notes.append(note)
    print(f"Note: {note} successfully added! ")

def read_note(notes):
    for note in notes:
        print(note)
    print(f"Notes: successfully read! ")

while True:
    command = str(input("Enter command: "))
    if command == "add":
        note = str(input("Enter note: "))
        add_note(notes, note)
    elif command == "read":
        read_note(notes)