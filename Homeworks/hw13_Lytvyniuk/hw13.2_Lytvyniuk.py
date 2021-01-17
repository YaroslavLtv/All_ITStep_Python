user_string = str(input("Enter the sentence: "))
enter_words = True
changed_string = ""
while enter_words:
    user_words = str(input("Enter the word that you want to uppercase: "))
    changed_string = user_string.replace(user_words, user_words.upper())
    enter_words = not input("Press [Enter] to continue entering words, or Any Key to continue: ")
print(changed_string)
