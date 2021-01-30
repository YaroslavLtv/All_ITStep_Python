class Notebook:
    notes = {}
    name = "default"
    password = "default"

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def add_note(self, key, note):
        self.notes[key] = note

    def del_note(self, key):
        self.notes.pop(key)

    # def __str__(self):
        # return f"{self.notes}"
    def __str__(self):
        nn = ''
        for key in self.notes:
            nn = nn + str(key) + " : " + str(self.notes[key]) + '\n'
        return nn


yarek = Notebook("yarek", "1")

while True:
    command = str(input("Enter command: "))
    if command == "show":
        print(yarek)
    elif command == "add":
        k = str(input("Enter key: "))
        n = str(input("Enter note: "))
        yarek.add_note(k, n)
    elif command == "del":
        k = str(input("Enter key: "))
        yarek.del_note(k)

