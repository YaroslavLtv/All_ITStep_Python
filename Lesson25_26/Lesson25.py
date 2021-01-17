data_base = []  # [["Yarek",  "Milk", "Bread", "Water"], ["Sten", "Fish", "Potato"]]
data_base1 = [["Glen", "Something"], ["Den", "Something"]]  # [["Yarek",  "Milk", "Bread", "Water"], ["Sten", "Fish", "Potato"]]
# Create user
def create_user(data_base, name):
    l = list()
    l.insert(0, name)
    data_base.append(l)
    return name

# Create note
def create_user_note(data_base, name, note):
    for i in range(len(data_base)):
        if data_base[i][0] == name:
            data_base[i].append(note)
            break
    return note

# Read Users
def read_users(data_base):
    print("User ID\t\tUser Name ")
    for i in range(len(data_base)):
        print(f"{i}\t\t{data_base[i][0]}")

# Read Notes
def read_users_note(data_base, name):
    print("User ID\t\tUser Name ")
    for i in range(len(data_base)):
        if data_base[i][0] == name:
            print(f"{i}\t\t{data_base[i][0]}")
            for j in range(1, len(data_base[i])):
                print(f"\t{j}\t\t{data_base[i][j]}")
# Update Note
def update_user_note(data_base, name, old_note, new_note):
    print("User ID\t\tUser Name ")
    for i in range(len(data_base)):
        if data_base[i][0] == name:
            for j in range(1, len(data_base[i])):
                if data_base[i][j] == old_note:
                    data_base[i][j] == new_note
                    return new_note

print(data_base)
create_user(data_base, "Yarek")
print(data_base)

print(create_user(data_base, "Sten"))
print(data_base)
print(create_user(data_base, "Yarek_2"))
print(create_user_note(data_base, "Yarek", "Hello World1"))
print(create_user_note(data_base, "Yarek", "123"))
print(create_user_note(data_base, "Yarek", "Hello World3"))
print(create_user_note(data_base, "Yarek_2", "Hello World4"))
print(create_user_note(data_base, "Yarek_2", "Hello World5"))
print(create_user_note(data_base, "Yarek_2", "Hello World6"))
print(data_base)

# read_users(data_base)
update_user_note(data_base, "Yarek", "123", "456")
read_users_note(data_base, "Yarek")
read_users_note(data_base, "Yarek_2")