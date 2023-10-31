# Приложение заметки (Python)

import json
import datetime
import random

def load_notes():
    try:
        with open("notes.json", "r", encoding="utf-8") as notes_json:
            return json.load(notes_json)
    except:
        with open("notes.json", "w", encoding="utf-8") as notes_json:
            notes_json.write(json.dumps(notes, ensure_ascii=False))
        with open("notes.json", "r", encoding="utf-8") as notes_json:
            return json.load(notes_json)


def save_changes(notes_to_save):
    with open("notes.json", "w", encoding="utf-8") as notes_json:
        notes_json.write(json.dumps(notes, ensure_ascii=False))
    with open("notes.json", "r", encoding="utf-8") as notes_json:
        notes_to_save = json.load(notes_json)
    return notes_to_save

def new_note(notes_to_supplement):
    if len(notes_to_supplement)!= 0:
        for i in range(len(notes_to_supplement)):
                    for j in range(len(notes_to_supplement)-1):
                        if notes_to_supplement[j][0] > notes_to_supplement[j+1][0]:
                            remember_me = notes_to_supplement[j]
                            notes_to_supplement[j] = notes_to_supplement[j+1]
                            notes_to_supplement[j+1] = remember_me
        id = str(int(notes_to_supplement[(len(notes_to_supplement)-1)][0]) + 1)
    else:
        id = str(1)
    title = input("Введите заголовок заметки:")
    body = input("Введите текст заметки: ")
    date_of_change = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    new_note = [id, title, body, date_of_change]
    notes_to_supplement.append(new_note)
    save_changes(notes_to_supplement)
    print("Новая заметка успешно создана!")
    return notes_to_supplement
    
def show_notes():
    notes = load_notes()
    for i in range(len(notes)):
        print(f"ID заметки: {notes[i][0]}\nЗаголовок: {notes[i][1]}\nСодержание: {notes[i][2]}\nДата изменения: {notes[i][3]}\n") 

def edit_note(notes_to_edit):
    id_to_edit = input('Введите ID заметки, которую вы хотите отредактировать: ')
    try:
        for i in range(len(notes_to_edit)):
            if id_to_edit == notes_to_edit[i][0]:
                remember_i = i
                break
    except:
        print("Не удалось найти заметку с таким ID")
    
    title = input("Введите новый заголовок заметки:")
    body = input("Введите новый текст заметки: ")
    date_of_change = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes_to_edit[remember_i] = [id_to_edit, title, body, date_of_change]
    save_changes(notes_to_edit)
    print("Заметка успешно изменена!")
    return notes_to_edit

def remove_note(notes_to_remove_in):
    id_of_note_to_remove = input('Введите ID заметки, которую вы хотите удалить: ')
    id_found = False
    for i in range(len(notes_to_remove_in)):
        note = notes_to_remove_in[i]
        if note[0] == id_of_note_to_remove:
            id_found = True
            notes_to_remove_in.remove(notes_to_remove_in[i])
            break
    if id_found == True:
        save_changes(notes_to_remove_in)
        print('Вы успешно удалили заметку')
    else:
        save_changes(notes_to_remove_in)
        print('Не существует заметки с таким ID!')
    return notes_to_remove_in

def sort_notes(notes_to_sort):
    how_to_sort = int(input("Введите 1, если хотите отсортировать заметки от самой новой к самой старой.\n"+
                            "Введите 2, если хотите отсортировать заметки от самой старой к самой новой.\n"+
                            "Номер вашего выбора: "))
    try:
        if how_to_sort == 1:
            for i in range(len(notes_to_sort)):
                    for j in range(len(notes_to_sort)-1):
                        if notes_to_sort[j][3] < notes_to_sort[j+1][3]:
                            remember_me = notes_to_sort[j]
                            notes_to_sort[j] = notes_to_sort[j+1]
                            notes_to_sort[j+1] = remember_me             
        elif how_to_sort == 2:
            for i in range(len(notes_to_sort)):
                    for j in range(len(notes_to_sort)-1):
                        if notes_to_sort[j][3] > notes_to_sort[j+1][3]:
                            remember_me = notes_to_sort[j]
                            notes_to_sort[j] = notes_to_sort[j+1]
                            notes_to_sort[j+1] = remember_me        
        save_changes(notes_to_sort)
        return notes_to_sort 
    except:
        print("Ошибка ввода, для стабильного продолжения работы программа сортирует заметки по умолчанию.\n")
        
    
id = 1
notes = [["1", "Покупки", "Молоко, яйца, корень имбиря, лимон, кошачьи пакетики, что-нибудь к чаю", "2022-11-29 18:02:57"], 
         ["2", "Кино для просмотра", "Бункер, Как приручить дракона 2, Притворись моей женой", "2021-10-30 15:07:51"],
         ["3", "ВАЖНО", "Отвезти кота к ветеринару в 12.00 завтра, клиника Кит, Сходня", "2023-10-31 01:12:52"],
         ["4", "дверь установка", "Дождаться звонка от установщиков двери, договориться о дате", "2023-10-30 09:44:52"]]

print("Добро пожаловать в приложение 'Ваши заметки'!\nИспользуйте команду /start, чтобы начать работу с заметками.")
while True:
    notes = load_notes()
    command = input("Введите команду:")
    if command == "/start":
        print("Вы можете использовать следующие команды: \n"+ 
                "/all - для показа всех заметок\n"+
                "/add - для добавления новой заметки\n" +
                "/edit - для изменения вашей заметки\n" +
                "/remove - для удаления вашей заметки\n" + 
                "/sort - для сортировки ваших заметок по дате\n" +
                "/stop - для выхода из приложения")
    elif command == "/stop":
        save_changes(notes)
        print("Вы закрыли приложение. До новых встреч!")
        break
    elif command == "/all":
        show_notes()
    elif command == "/add":
        new_note(notes)
    elif command == "/edit":
        edit_note(notes)
    elif command == "/remove":
        remove_note(notes)
    elif command == "/sort":
        sort_notes(notes)
        show_notes()
    else:
        print('Ошибка ввода. Попробуйте снова.')
