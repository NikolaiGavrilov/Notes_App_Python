# Приложение заметки (Python)

# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента. 

# Например:
# python notes.py add --title "новая заметка" –msg "тело новой заметки"

# Или так:
# python note.py
# Введите команду: add
# Введите заголовок заметки: новая заметка
# Введите тело заметки: тело новой заметки
# Заметка успешно сохранена
# Введите команду:

# При чтении списка заметок реализовать фильтрацию по дате.

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
        if notes_to_supplement[len(notes_to_supplement)-1][0]:
            id = str(int(notes_to_supplement[len(notes_to_supplement)-1][0]) + 1)
    else:
        id = 1
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
    for i in range(len(notes_to_remove_in)):
        note = notes_to_remove_in[i]
        if note[0] == id_of_note_to_remove:
            notes_to_remove_in.remove(notes_to_remove_in[i])
            break
    save_changes(notes_to_remove_in)
    print('Вы успешно удалили заметку')
    return notes_to_remove_in

def sort_notes(notes_to_sort):
    dates = list()
    for i in range(len(notes_to_sort)):
        dates.append(notes_to_sort[i][3])
    how_to_sort = int(input("Введите 1, если хотите отсортировать заметки от самой новой к самой старой.\n"+
                            "Введите 2, если хотите отсортировать заметки от самой старой к самой новой.\n"+
                            "Номер вашего выбора: "))
    try:
        if how_to_sort == 1:
            dates_sorted = sorted(dates, reverse=True)         
        elif how_to_sort == 2:
            dates_sorted = sorted(dates, reverse=False)
        for i in range(len(dates_sorted)):
                for j in range(len(notes_to_sort)):
                    if dates_sorted[i] == notes_to_sort[j][3]:
                        remember_me = notes_to_sort[i]
                        notes_to_sort[i] = notes_to_sort[j]
                        notes_to_sort[j] = remember_me           
                save_changes(notes_to_sort)
                return notes_to_sort 
    except:
        print("Ошибка ввода, для стабильного продолжения работы программа сортирует заметки по умолчанию.\n")
        
    


id = 1
notes = [["1", "Покупки", "Молоко, яйца, корень имбиря, лимон, кошачьи пакетики, что-нибудь к чаю", "2022-11-29 18:02:57"], 
         ["2", "Кино для просмотра", "Бункер, Как приручить дракона 2, Притворись моей женой", "2021-10-30 15:07:51"],
         ["3", "ВАЖНО", "Отвезти кота к ветеринару в 12.00 завтра, клиника Кит, Сходня", "2023-10-31 01:12:52"],
         ["4", "не забудь про дверь", "Дождаться звонка от установщиков двери, договориться о дате", "2023-10-30 09:44:52"]]

while True:
    notes = load_notes()
    command = input("Введите команду:")
    if command == "/start":
        print("Добро пожаловать в приложение 'Ваши заметки'!\n")
        print("Вы можете использовать следующие команды: \n"+ 
                "/all - для показа всех заметок\n"+
                "/add - для добавления новой заметки\n" +
                "/edit - для изменения вашей заметки\n" +
                "/remove - для удаления вашей заметки\n" + 
                "/sort - для сортировки ваших заметок по дате\n" +
                "/stop - для выхода из приложения\n")
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
