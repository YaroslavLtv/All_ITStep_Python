from tkinter import *

notes = {}


def create():
    global notes
    name = entry_name.get()
    note = entry_note.get()
    entry_name.delete(0, END)
    entry_note.delete(0, END)
    notes[name] = note

def read():
    good_notes = ''
    for note in notes:
        good_notes = good_notes + f'{note} \n {notes[note]}\n\n'
    label_notes.config(text=good_notes)

def update():
    global notes
    name = entry_name.get()
    note = entry_note.get()
    entry_name.delete(0, END)
    entry_note.delete(0, END)
    notes[name] = note

def delete():
    global notes
    name = entry_name.get()
    entry_name.delete(0, END)
    entry_note.delete(0, END)
    del notes[name]


root = Tk()
root.title('Notes')
root.geometry('180x250')

label_notes_name = Label(root, anchor='c')
label_notes_name.config(text='NAME')
label_notes_name.pack()
entry_name = Entry(root, bd=5)
entry_name.pack()
label_notes_notes = Label(root, anchor='c')
label_notes_notes.config(text='NOTE')
label_notes_notes.pack()
entry_note = Entry(root, bd=5)
entry_note.pack()
button_create = Button(width=16, bg='green', command=create)
button_create.config(text='CREATE')
button_create.pack()
button_read = Button(width=16, bg='blue', command=read)
button_read.config(text='READ')
button_read.pack()
button_update = Button(width=16, bg='yellow', command=update)
button_update.config(text='UPDATE')
button_update.pack()
button_delete = Button(width=16, bg='red', command=delete)
button_delete.config(text='DELETE')
button_delete.pack()
label_notes = Label(root, anchor='c')
label_notes.pack()
root.mainloop()