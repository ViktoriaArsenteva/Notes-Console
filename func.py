import datetime
import os
import pathlib

def HelloNote():
    print("Заметки \n")
    print(" 1.создать новую заметку \n 2.Открыть заметку \n ")
    num = input("Введите номер действия: ")
    return num

def CreateNewNote():
    noteName = input("Имя заметки: ")
    noteBody = input("Тело заметки: ")
    return noteName,noteBody

def CheckNote(name,text,check):
    try:
        f = open("notes/" + name + ".json","x")
        date = Time()
        f.write(date +"\n")
        f.write(text)
        f.close()
        check = True
        return check,name
    except FileExistsError:
        print("Заметка с таким именем уже существует, введите другое:")
        fname = input()
        check = False
        return check,fname

def Filter():
    print(" 1.Сначала новые \n 2.Сначала старые \n ")
    num = input("Введите номер действия: ")
    return num

def NewFilter():
    notes = Catalog()
    dates = []
    for i in notes:
        f = open("notes/"+i)
        date = f.readline()
        name = date + " "+ i
        dates.append(name)
    dates.sort(reverse=True)
    newnotes = []
    for j in range(len(dates)):
        date,name = dates[j].split("\n ")
        newnotes.append(name)
    return newnotes



def OldFilter():
    notes = NewFilter()
    notes.reverse()
    return notes

def Catalog():
    notes = []
    dir = 'notes/'
    d = pathlib.Path(dir)
    for file in d.iterdir():
        notes.append(file.name)
    return notes


def OpenNote():
    print(" 1.Открыть только для чтения \n 2.Открыть для редактирования \n 3.Удалить заметку \n ")
    num = input("Введите номер действия: ")
    return num

def PrintAllNotes(list):
    for i in range(len(list)):
        print(i,list[i])
    num = int(input("Ввeдите номер зaметки: "))
    return num


def SaveNote(name,body):
        note = open("notes/"+name,"a")
        note.write(body)
        note.close()


def Time():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    return date

def ReadNote(filename):
    print(filename)
    file = open("notes/"+filename)
    f = file.read()
    print(f)
    file.close()

    

def DeleteNote(filename):
    os.remove("notes/"+filename)
    print("Файл удален")
