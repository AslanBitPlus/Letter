import file_func as file_func
import letter as letter
import user_interface as us_int

number = 6  # минимальное количество символов в тексте заметки


def ins_note(): # - 2 -
    note = us_int.create_note(number)
    array = file_func.read_file()
    for notes in array:
        if letter.Note.get_id(note) == letter.Note.get_id(notes):
            letter.Note.set_id(note)
    array.append(note)
    file_func.write_file(array, 'a')
    print('Заметка добавлена...')

def print_all_notes(): # - 1 -
    ind = True
    array = file_func.read_file()
    for notes in array:
        ind = False
        print(letter.Note.map_note(notes))
    if ind == True:
        print('Нет ни одной заметки...')

def upd_note(): # - 4 -
    id = input('Введите id для РЕДАКТИРОВАНИЯ заметки: ')
    array = file_func.read_file()
    ind = True
    for notes in array:
        if id == letter.Note.get_id(notes):
            ind = False
            note = us_int.create_note(number)
            letter.Note.set_title(notes, note.get_title())
            letter.Note.set_body(notes, note.get_body())
            letter.Note.set_date(notes)
            print('Заметка изменена...')
    if ind == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_func.write_file(array, 'a')

def del_note(): # - 3 -
    id = input('Введите id для УДАЛЕНИЯ заметки: ')
    array = file_func.read_file()
    ind = True
    for notes in array:
        if id == letter.Note.get_id(notes):
            ind = False
            array.remove(notes)
            print('Заметка удалена...')
    if ind == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_func.write_file(array, 'a')

def print_date_notes(): # - 5 -
    ind = True
    array = file_func.read_file()
    date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        ind = False
        if date in letter.Note.get_date(notes):
            print(letter.Note.map_note(notes))
    if ind == True:
        print('В списке заметок на дату <' + date + '> НЕТ ни одной заметки...')

def print_id_notes(): # - 6 -
    ind = True
    array = file_func.read_file()
    id = input('Введите id для поиска в заметках: ')
    for notes in array:
        ind = False
        if id in letter.Note.get_id(notes):
            print(letter.Note.map_note(notes))
    if ind == True:
        print('В списке заметок с ID <' + id + '> НЕТ ни одной заметки...')