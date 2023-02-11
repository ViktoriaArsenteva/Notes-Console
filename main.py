from func import HelloNote,CreateNewNote,OpenNote,PrintAllNotes,Filter,ReadNote,ChangeNote,DeleteNote,CheckNote, Time,NewFilter,OldFilter,SaveNote

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
        text = input("Введите новые данные: ")
        print(filename)
        SaveNote(filename,text)
    elif res == "3":
        DeleteNote(filename)
