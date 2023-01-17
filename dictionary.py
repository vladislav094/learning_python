# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# temp = []
# for elt in users:
# 	if 'email' not in elt or elt['email'] == '':
# 		temp.append(elt['name'])
# print(*sorted(temp))

# def string_representation(number: int):
#     dict1 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
#     digit = str(number)
#     new_arr = [int(x) for x in digit]
#     for elt in new_arr:
#         if elt in dict1:
#             print(dict1[elt], end=' ')
# digit = int(input())
# string_representation(digit)


def lear_course():
    dict1 = [
        {'Номер курса': 'CS101', 'Номер аудитории': '3004', 'Преподаватель': 'Хайнс', 'Время': '8:00'},
        {'Номер курса': 'CS102', 'Номер аудитории': '4501', 'Преподаватель': 'Альварадо', 'Время': '9:00'},
        {'Номер курса': 'CS103', 'Номер аудитории': '6755', 'Преподаватель': 'Рич', 'Время': '10:00'},
        {'Номер курса': 'NT110', 'Номер аудитории': '1244', 'Преподаватель': 'Берк', 'Время': '11:00'},
        {'Номер курса': 'CM241', 'Номер аудитории': '1411', 'Преподаватель': 'Ли', 'Время': '13:00'}
    ]
    number_course = str(input())
    b = ''
    for elt in range(len(dict1)):
        if number_course in dict1[elt].values():
            a = list(dict1[elt].items())
            print(a)
            b = f"{number_course}: {a[1][1]}, {a[2][1]}, {a[3][1]}"
    print(b)
# lear_course()


def set_of_message(phrase: str):
    number_keyword = {".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
        "A":'2', "B":'22', "C":'222',
        "D":'3', "E":'33', "F":'333',
        "G":'4', "H":'44', "I":'444',
        "J":'5', "K":'55', "L":'555',
        "M":'6', "N":'66', "O":'666',
        "P":'7', "Q":'77', "R":'777', "S": '7777',
        "T":'8', "U":'88', "V":'888',
        "W":'9', "X":'99', "Y":'999', "Z": '9999',
        " ":'0'
    }
    my_string = phrase.upper()
    for elt in my_string:
        if elt in number_keyword.keys():
            print(number_keyword[elt], end='')

# word = str(input())
# set_of_message(word)
