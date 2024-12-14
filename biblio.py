# библиотека книжная
# вывод информации о всех книгах
# вывод книги по автору, по названию
#
# вывод информации о книге по введенному с клавиатуры номеру
# вывод количества книг, старше введённого года
# удалении книги по номеру
library = [{"id": 12,\
            "title" : "Граф Монте-Кристо",\
            "author" : "Александр Дюма"},\
            {"id": 1335,\
            "title": "Три мушкетера",\
            "author":"Александр Дюма"},\
            {"id":144,\
            "title": "Отцы и дети",\
            "author":"Иван Тургенев"},\
            {"id": 15,\
            "title" : "Война и мир",\
            "author": "Лев Толстой"},
            {"id": 1665,\
            "title" : "Простой Python. Современный стиль программирования. 2-е изд.",\
            "author": "Любанович Билл"},
            {"id": 1724,\
            "title" : "Изучаем Python: программирование игр, визуализация данных, веб-приложения. 3-е изд.",\
            "author": "Мэтиз Эрик"}
]
# def full_lib():
#     print(library)
#

# def listAll(x):
#     for i in range(len(library)):
#         el =  '{},{},{}'.format(library[i].get('id'),\
#             library[i].get('title'),\
#             library[i].get('author'))
#         return el
# def listall(x):
#     for i in range(len(library)):
#         #print(library[i]['title'])
#         if library[i]['title'] == x:
#             print(library[i])
#             # Выводим
#             print(F'\nКод книги(ид):   {library[i]['id']}')
#             # Выводим
#             print(F'\tНаименование:   {library[i]['title']}')
#             # Выводим
#             print(F'\tАвтор:   {library[i]['author']}')
#     return
# с именованными параметрами, по умолчанию пусто
def print_book(i):
    print(F'\tКод книги(ид):   {library[i]['id']}')
    print(F'\tНаименование:   {library[i]['title']}')
    print(F'\tАвтор:   {library[i]['author']}')
def list_find(ids = None, titles = None , autors = None): #
    for i in range(len(library)):
        # print(library[i]['title'])
        #print(titles)
        # или по Наименованию или по Автору или по ИД книги
        if library[i]['id'] == ids:
            # print(library[i])
            # print('{},{},{}'.format(library[i].get('id'), library[i].get('title'), library[i].get('author')))
                # Выводим
            print_book(i)
            # print(F'\tКод книги(ид):   {library[i]['id']}')
            # print(F'\tНаименование:   {library[i]['title']}')
            # print(F'\tАвтор:   {library[i]['author']}')
        #elif ids is None:
        # else:
        #     print("ПО ТАКОМУ ID КНИГА НЕ НАЙДЕНА")


        if library[i]['title'] == titles:
            # Выводим
            print_book(i)
            # print(F'\tНаименование:   {library[i]['title']}')
            # print(F'\tАвтор:   {library[i]['author']}')
            # print(F'\tКод книги(ид):   {library[i]['id']}')
        # elif titles is not None:
        #     print("КНИГА НЕ НАЙДЕНА")
        #     return
        if library[i]['author'] == autors:
                # Выводим
            print_book(i)
            # print(F'\tАвтор:   {library[i]['author']}')
            # print(F'\tКод книги(ид):   {library[i]['id']}')
            # print(F'\tНаименование:   {library[i]['title']}')
        # elif autors is not None:
        #     print("АВТОР НЕ НАЙДЕН")
        #     return
        # else:
        #     print("НЕТ КНИГИ")
        #     break

    return
def qwerty(): # функция выводит книги по Названию
    # 1й способ
    for i in range(len(library)):
         print(library[i]['title'])
    # 2й способ
    for i in library:
        title = i.get('title')
        print(title)
    # 3й способ
    title = [item['title'] for item in library]  # ввиде списка []
    print(title)
    return

#qwerty()
    #for i in range(len(library)):
    #     #if x == tuple(library[i].items()):
    #        print(i)
    #         print(tuple(library[i].items()))
    #         print(library[i])
    #         print(library[i].values())
    #         print(library[i].keys())
    #         print(library[i].items())
    # return


print(list_find(titles ="Война и мир")) # ищем по названию книги
print(list_find(autors ="Мэтиз Эрик")) # ищем по автору
print(list_find(ids=12)) # ищем по ИД
#print(list_find(titles ="Маша и медведь")) # нет книги
