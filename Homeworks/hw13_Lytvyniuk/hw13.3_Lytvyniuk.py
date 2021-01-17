text = '''What is Lorem Ipsum? Lorem Ipsum 
is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown 
printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but 
also the leap into electronic typesetting, remaining essentially 
unchanged. It was popularised in the 1960s with the release of 
Letraset sheets containing Lorem Ipsum passages, and more recently 
with desktop publishing software like Aldus PageMaker including versions of 
Lorem Ipsum.'''

sentences_count = 0

for i in range(len(text)):
    if text[i].isupper() and text[i - 1] == " " and text[i - 2] == ".":
        sentences_count += 1
    elif text[i].isupper() and text[i - 1] == " " and text[i - 2] == "?":
        sentences_count += 1
    elif text[i].isupper() and text[i - 1] == " " and text[i - 2] == "!":
        sentences_count += 1
if text[0].isupper():
    sentences_count += 1
elif text.endswith("."):
    sentences_count += 1

print(f"The paragraph include {sentences_count} sentences")
