def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('homework8.py\\book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('homework8.py\\book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


# def find_data() -> None:
#     """Печатает результат поиска по справочнику."""
#     with open('template_for_homework8\\book.txt', 'r', encoding='utf-8') as file:
#         data = file.read()
#     contact_to_find = input('Введите, что хотите найти: ')
#     result = search(data, contact_to_find)
#     print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('homework8.py\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        
    fio_to_find = input('Введите ФИО, которое нужно найти: ')
    result = search(data, fio_to_find)
    
    if result:
        for i, contact in enumerate(result):
            print(f"{i+1}. {contact}")
        
        choice = input('Введите номер контакта, который нужно изменить или удалить: ')
        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(result):
            choice = input('Некорректный ввод. Введите номер контакта: ')
        choice = int(choice)
        
        phone_num = input('Введите новый номер телефона (нажмите Enter, чтобы оставить без изменений): ')
        if phone_num:
            new_data = data.replace(result[choice-1].split(' | ')[1], phone_num)
        else:
            new_data = data
        
        delete_choice = input('Хотите ли вы удалить этот контакт? (y/n): ')
        while delete_choice not in ['y', 'n']:
            delete_choice = input('Некорректный ввод. Введите "y" или "n": ')
        
        if delete_choice == 'y':
            new_data = new_data.replace(result[choice-1]+'\n', '')
            print(f'Контакт "{result[choice-1].split(" | ")[0]}" удален.')
        else:
            print(f'Номер телефона для контакта "{result[choice-1].split(" | ")[0]}" успешно изменен.')
        
        with open('homework8.py\\book.txt', 'w', encoding='utf-8') as file:
            file.write(new_data)
            
    else:
        print(f'Контакт с ФИО "{fio_to_find}" не найден.')