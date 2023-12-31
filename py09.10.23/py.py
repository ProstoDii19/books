def sort_books():
    # открываю файл с названиями книг
    with open('books.txt', 'r') as file:
        # считываю все строки из файла
        lines = file.readlines()

    # создаю список книг из считанных строк
    books = [line.strip() for line in lines]

    # сортирую список книг по алфавиту
    sorted_books = sorted(books)

    # открываю файл для записи отсортированного списка
    with open('sorted_books.txt', 'w') as file:
        # записываю каждую книгу из отсортированного списка на отдельной строке
        for book in sorted_books:
            file.write(book + '\n')

# вызываю функцию для выполнения задачи
sort_books()

# Задание 1.
"""В текстовом файле 'books.txt' с новой строки хранятся названия книг.
Создать список книг из этих названий.
Отсортировать его по алфавиту с использованием sorted и key
Выгрузить отсортированный список в файл 'sorted_books.txt'
Отправить в ЭлЖур не поздней 9.55
"""