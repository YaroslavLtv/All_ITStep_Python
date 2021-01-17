text = '''In the hole in the ground there lived a hobbit'''
new_string = ""
for i in range(len(text)):
    if text[i] == "h":
        new_string = text[:i]
        break
for j in range(len(text) - 1, 0, -1):
    if text[j] == "h":
        new_string += text[j + 1:]
        break
print(new_string)
