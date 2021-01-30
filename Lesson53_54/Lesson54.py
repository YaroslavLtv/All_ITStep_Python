# #User - Simple Abstract Class
# class User:
#     __id = 0
#     __count_of_users = 0
#     name = 'default'
#     password = 'default'
#     def change(self,*data):
#         if len(data) == 1:
#             self.name = data[0]
#         elif len(data) == 2:
#             self.name = data[0]
#             self.password = data[1]
#         elif len(data) == 3 and self.__class__.__name__ == 'Administrator':
#             self.name = data[0]
#             self.password = data[1]
#             self.__id = data[2]
#
#     def change_user(self,user, *data):
#         if self.__class__.__name__ != 'Administrator':
#             if len(data) == 1:
#                 self.name = data[0]
#             elif len(data) == 2:
#                 self.name = data[0]
#                 self.password = data[1]
#         elif self.__class__.__name__ == 'Administrator':
#             if len(data) == 1:
#                 user.name = data[0]
#             elif len(data) == 2:
#                 user.name = data[0]
#                 user.password = data[1]
#             elif len(data) == 3:
#                 user.name = data[0]
#                 user.password = data[1]
#                 user.__id = data[2]
#
#
#     def __init__(self,name,password):
#         self.name = name
#         self.password = password
#         User.change_count_of_user()
#         self.set_user_id()
#     def __str__(self):
#         return f'Name : {self.name}\n' \
#                f'Password : {self.password}\n' \
#                f'Count : {User.__count_of_users}\n' \
#                f'ID : {self.__id}\n'
#     @staticmethod
#     def change_count_of_user():
#         User.__count_of_users = User.__count_of_users + 1
#     def set_user_id(self):
#         self.__id = User.__count_of_users
#
#
# class Guest(User):
#     def send_message(self,*messages):
#         self.messages = messages
#
# class Administrator(User):
#     def delete_all_posts(self,username):
#         username.messages = ()
#
#
# admin = Administrator('admin','password')
# print(admin)
# andrey = Guest('andrey','password')
# print(andrey)
# andrey.send_message('Andrey',"Hello","Glad")
# print(andrey.messages)
# admin.delete_all_posts(andrey)
# print(andrey.messages)
# andrey.change('Sten','123456')
# print(andrey)
# admin.change('Ben','654321',999)
# print(admin)
# andrey.change('Ben','654321',999)
# print(andrey)
# andrey.change_user(admin,'Ben','654321',999)
# print(admin)
#
# admin.change_user(andrey,'GGGGGG','KKKKKKKK',22222345)
# print(andrey)


#User - Simple Abstract Class
class User:
    __rules = "Guest"
    __id = 0
    __count_of_users = 0
    name = 'default'
    password = 'default'
    def change(self,*data):
        if len(data) == 1:
            self.name = data[0]
        elif len(data) == 2:
            self.name = data[0]
            self.password = data[1]
        elif len(data) == 3 and self.__class__.__name__ == 'Administrator':
            self.name = data[0]
            self.password = data[1]
            self.__id = data[2]

    def change_user(self,user, *data):
        if self.__class__.__name__ != 'Administrator':
            if len(data) == 1:
                self.name = data[0]
            elif len(data) == 2:
                self.name = data[0]
                self.password = data[1]
        elif self.__class__.__name__ == 'Administrator':
            if len(data) == 1:
                user.name = data[0]
            elif len(data) == 2:
                user.name = data[0]
                user.password = data[1]
            elif len(data) == 3:
                user.name = data[0]
                user.password = data[1]
                user.__id = data[2]


    def __init__(self,name,password):
        self.name = name
        self.password = password
        User.change_count_of_user()
        self.set_user_id()
    def __str__(self):
        return f'Name : {self.name}\n' \
               f'Password : {self.password}\n' \
               f'Count : {User.__count_of_users}\n' \
               f'ID : {self.__id}\n'
    @staticmethod
    def change_count_of_user():
        User.__count_of_users = User.__count_of_users + 1
    def set_user_id(self):
        self.__id = User.__count_of_users


class Guest(User):
    def send_message(self,*messages):
        self.messages = messages

class Administrator(User):
    def delete_all_posts(self,username):
        username.messages = ()


admin = Administrator('admin','password')
print(admin)
andrey = Guest('andrey','password')
print(andrey)
andrey.send_message('Andrey',"Hello","Glad")
print(andrey.messages)
admin.delete_all_posts(andrey)
print(andrey.messages)
andrey.change('Sten','123456')
print(andrey)
admin.change('Ben','654321',999)
print(admin)
andrey.change('Ben','654321',999)
print(andrey)
andrey.change_user(admin,'Ben','654321',999)
print(admin)

admin.change_user(andrey,'GGGGGG','KKKKKKKK',22222345)
print(andrey)