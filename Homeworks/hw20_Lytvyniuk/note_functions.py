# Create user
def create_user(data_base, name, password):
    l = list()
    l.insert(0, name)
    l.insert(1, password)
    data_base.append(l)
    return name


# Log in user
def user_login(data_base, name, password):
    for i in range(len(data_base)):
        if data_base[i][0] == name and data_base[i][1] != password:
            print("Wrong password")
            break
        elif data_base[i][0] == name and data_base[i][1] == password:
            print(f"{name} is logged in")
            return name
        elif data_base[i][0] != name:
            if i == len(data_base)-1:
                print("User not exist, please create new user")


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
            print(f"\t{i}\t\t{data_base[i][0]}")
            for j in range(2, len(data_base[i])):
                print(f"\t\t{j}\t\t{data_base[i][j]}")


# Update Note by Name
def update_user_note(data_base, name, old_note, new_note):
    print("User ID\t\tUser Name ")
    for i in range(len(data_base)):
        if data_base[i][0] == name:
            for j in range(2, len(data_base[i])):
                if data_base[i][j] == old_note:
                    data_base[i][j] = new_note
                    return new_note


# Update Note by index
def update_user_note_by_index(data_base, name, index, new_note):
    print("User ID\t\tUser Name ")
    for i in range(len(data_base)):
        if data_base[i][0] == name:
            data_base[i][index] = new_note


# Delete note
def delete_note(data_base, name, index):
    print("User ID\t\tUser Name ")
    for i in range(len(data_base)):
        if data_base[i][0] == name:
            deleted_note = data_base[i].pop(index)
            print(f"{deleted_note} is removed")
