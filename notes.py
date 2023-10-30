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
    with open("notes.json", "r", encoding="utf-8") as notes_json:
        return json.load(notes_json)

def save_changes(notes_to_save):
    with open("notes.json", "w", encoding="utf-8") as notes_json:
        notes_json.write(json.dumps(notes, ensure_ascii=False))
    with open("notes.json", "r", encoding="utf-8") as notes_json:
        notes_to_save = json.load(notes_json)
    return notes_to_save

def new_note(notes_to_supplement):
    find_previous_id_list = notes_to_supplement.keys()
    id = len(find_previous_id_list) + 1
    notes_to_supplement[id] = {}
    title = input("Введите заголовок заметки:")
    notes_to_supplement[id]["Заголовок"] = title
    body = input("Введите текст заметки: ")
    notes_to_supplement[id]["Тело заметки"] = body
    date_of_creation = datetime.datetime.now()
    date_of_creation_str = date_of_creation.strftime("%Y-%m-%d %H:%M:%S") 
    notes_to_supplement[id]["Дата создания"] = date_of_creation_str
    notes_to_supplement[id]["Дата изменения"] = date_of_creation_str
    save_changes(notes_to_supplement)
    print("Новая заметка успешно создана!")
    return notes_to_supplement
    
def show_notes():
    print(load_notes())

def edit_note(notes_to_edit):
    id_to_edit = input('Введите ID заметки, которую вы хотите отредактировать: ')
    title = input("Введите новый заголовок заметки:")
    notes_to_edit[id_to_edit]["Заголовок"] = title
    body = input("Введите новый текст заметки: ")
    notes_to_edit[id_to_edit]["Тело заметки"] = body
    notes_to_edit[id_to_edit]["Дата изменения"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_changes(notes_to_edit)
    print("Заметка успешно изменена!")
    return notes_to_edit

def remove_note(notes_to_remove_in):
    note_to_remove = input('Введите ID заметки, которую вы хотите удалить: ')
    del notes_to_remove_in[note_to_remove]
    save_changes(notes_to_remove_in)
    print('Вы успешно удалили заметку')
    return notes_to_remove_in

id = 1
notes = {id: {"Заголовок": "Покупки", "Тело заметки": "Молоко, яйца, корень имбиря, лимон, кошачьи пакетики, что-нибудь к чаю", "Дата создания": "2023-10-30 18:02:57", "Дата изменения": "2023-10-30 18:02:57"}}

while True:
    notes = load_notes()
    command = input("Введите команду:")
    if command == "/start":
        print("Добро пожаловать в приложение 'Ваши заметки'!")
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
    else:
        print('Ошибка ввода. Попробуйте снова.')
