print(' 1. Открыть файл\n '
      '2. Сохранить файл\n '
      '3. Показать все контакты\n'
      ' 4. Создать контакт\n '
      '5. Изменить контакт\n '
      '6. Найти контакт\n '
      '7. Удалить контакт\n '
      '8. Выход')

phone_book = []
path = 'name.txt.'


def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)


def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')


def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))


def search_contact(phone_book):
    search = input('Введите ключевой элемент : ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)
            else:
                print('Такого контакта нет')


while True:
    number = int(input('Введите пункт меню: '))

    match number:
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        case 2:
            pass
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact(phone_book)
        case 5:
            search_contact(phone_book)
        case 8:
            break

print('Досвидания')
