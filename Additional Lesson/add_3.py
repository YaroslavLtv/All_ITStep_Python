"""
Нужно создать класс User
В котором будут следующие свойства:
 - name, нужно проверить, что передаваемый аргумент - строка и сделать имя с заглавной буквы
 - email, нужно проверить, что передаваемый аргумент - строка и в почте есть символ "@" и "."
 - password, нужно проверить, что передаваемый аргумент - строка, а так-же, что длина пароля больше 8 символов и в нем есть хотя бы одно число, большая и маленькая буква
 - confirm_password, нужно проверить, что передаваемый аргумент - строка, а так-же, что поле совпадает с свойством password
В случае, если хотя бы одно поле не соответствует валидации, то выбросить ошибку ValueError с описанием проблемы.
После создания класса, необходимо сделать простой интерфейс для просмотра, добавления, редактирования и удаления пользователей.
"""


# class User:
#     def __init__(self, name, email, password, confirm_password):
#         if isinstance(self.name, str):
#             self.name = name.title()
#         else:
#             print("Value error, name must be a string")
#
#         if isinstance(self.email, str) and '@' in email and '.' in email:
#             self.email = email
#         else:
#             print("Value error, email address must contain @ and . symbols")
#         if (isinstance(self.password, str)) and (len(self.password) > 8):
#             for character in self.password:
#                 if character.isupper() or character.isdigit():
#                     self.password = password
#         if isinstance(self.confirm_password, str) and (self.password == self.confirm_password):
#             self.confirm_password = confirm_password
#
#
# users = {}
#
# user_input = True
# while user_input:
#     user_input = input("Enter a command:\n\t[add] - add user\n\t[del] - del user\n\t"
#                        "[i] - info about users: ")
#     if user_input == "add":

import string


class User:

    def __init__(self, name, email, password, confirm_password):
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.validate_name()
        self.validate_email()
        self.validate_password()
        self.validate_confirm_password()

    def validate_name(self):
        if not isinstance(self.name, str):
            raise ValueError('Name error')
        self.name.capitalize()

    def validate_email(self):
        if not isinstance(self.email, str) or self.email.find('@') == -1 or self.email.find('.') == -1:
            raise ValueError('Email error')

    def validate_password(self):
        password_is_str = isinstance(self.password, str)
        normal_len = len(self.password) > 8
        has_upper = False
        has_lower = False
        has_digit = False
        for char in self.password:
            if char.isdigit():
                has_digit = True
            if char.islower():
                has_lower = True
            if char.isupper():
                has_upper = True
        if not (password_is_str and normal_len and has_upper and has_lower and has_digit):
            raise ValueError('Password error')

    def validate_confirm_password(self):
        if not isinstance(self.confirm_password, str) or self.password != self.confirm_password:
            raise ValueError('Confirm password error')


user = User('Ivan', 'asdmin@admin.com', 'Pasd14$4asDd', 'Pasd14$4asDd')
print(user)
print(int(user))
users = []
while True:
    name = input('name')
    email = input('email')
    password = input('password')
    password_confirm = input('password_confirm')
    users.append(User(name, email, password, password_confirm))