
from func import HelloNote,CreateNewNote,OpenNote,PrintAllNotes,Filter,ReadNote,DeleteNote,CheckNote,NewFilter,OldFilter,SaveNote

num = HelloNote()
if num == "1":
    name,text = CreateNewNote()
    check = False
    while check == False:
        check,name = CheckNote(name,text,check)
    print("Данные успешно сохранены")
if num == "2":
    filt = Filter()
    if filt == "1":
        notes = NewFilter()
    elif filt == "2":
        notes = OldFilter()
    noteId = PrintAllNotes(notes)
    filename = notes[noteId]
    res = OpenNote()
    if res == "1":
        ReadNote(filename)
    elif res == "2":
        ReadNote(filename)
        text = input("Введите новые данные: ")
        SaveNote(filename,text)
        print("Данные успешно сохранены")
    elif res == "3":
        DeleteNote(filename)
