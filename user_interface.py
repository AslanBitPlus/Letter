import letter as letter


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return letter.Note(title=title, body=body)


def menu():
    print("\n" +
          "---------- 'Заметки' ---------- \n" +
          "1 - Печать всех заметок\n" +
          "2 - Добавить заметку\n" +
          "3 - Удалить заметку\n" +
          "4 - Редактировать заметку\n" +
          "5 - Печать заметок по дате\n" +
          "6 - Печать заметок по id\n" +
          "7 - Выход из программы\n\n" +
          "Введите команду: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def exit():
    print("Вы вышли из программы!")