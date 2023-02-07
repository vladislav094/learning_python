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
#
# # def string_representation(number: int):
# #     dict1 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
# #     digit = str(number)
# #     new_arr = [int(x) for x in digit]
# #     for elt in new_arr:
# #         if elt in dict1:
# #             print(dict1[elt], end=' ')
# # digit = int(input())
# # string_representation(digit)
#
#
# def lear_course():
#     dict1 = [
#         {'Номер курса': 'CS101', 'Номер аудитории': '3004', 'Преподаватель': 'Хайнс', 'Время': '8:00'},
#         {'Номер курса': 'CS102', 'Номер аудитории': '4501', 'Преподаватель': 'Альварадо', 'Время': '9:00'},
#         {'Номер курса': 'CS103', 'Номер аудитории': '6755', 'Преподаватель': 'Рич', 'Время': '10:00'},
#         {'Номер курса': 'NT110', 'Номер аудитории': '1244', 'Преподаватель': 'Берк', 'Время': '11:00'},
#         {'Номер курса': 'CM241', 'Номер аудитории': '1411', 'Преподаватель': 'Ли', 'Время': '13:00'}
#     ]
#     number_course = str(input())
#     b = ''
#     for elt in range(len(dict1)):
#         if number_course in dict1[elt].values():
#             a = list(dict1[elt].items())
#             print(a)
#             b = f"{number_course}: {a[1][1]}, {a[2][1]}, {a[3][1]}"
#     print(b)
# # lear_course()
#
#
# def set_of_message(phrase: str):
#     number_keyword = {".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#         "A":'2', "B":'22', "C":'222',
#         "D":'3', "E":'33', "F":'333',
#         "G":'4', "H":'44', "I":'444',
#         "J":'5', "K":'55', "L":'555',
#         "M":'6', "N":'66', "O":'666',
#         "P":'7', "Q":'77', "R":'777', "S": '7777',
#         "T":'8', "U":'88', "V":'888',
#         "W":'9', "X":'99', "Y":'999', "Z": '9999',
#         " ":'0'
#     }
#     my_string = phrase.upper()
#     for elt in my_string:
#         if elt in number_keyword.keys():
#             print(number_keyword[elt], end='')
#
# # word = str(input())
# # set_of_message(word)
#
#
# def morse_code(word: str):
#     text = word.upper()
#     letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
#     morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#              '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#              '...--', '....-', '.....', '-....', '--...', '---..', '----.']
#
#     dict1 = dict(zip(letters, morse))
#     for elt in text:
#         if elt in letters:
#             print(dict1[elt], end=' ')
#
# # some_word = str(input())
# # morse_code(some_word)
#
# def update_several_dictionaries():
#     dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
#     dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#     result = {}
#     dict3 = {}
#     for elt in dict1:
#         if elt in dict2:
#             numb = dict1[elt] + dict2[elt]
#             dict3[elt] = numb
#     dict1.update(dict2)
#     dict1.update(dict3)
#     result.update(dict1)
#     return result
#
# # print(update_several_dictionaries())
#
# def count_duplicate():
#     text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
#     result = {}
#     for elt in text:
#         result[elt] = result.get(elt, 0) +1
#     return result
#
# # print(count_duplicate())
#
# def max_count_duplicate_sorted_by_lexicographic():
#     s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange' \
#         ' barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot ' \
#         'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate ' \
#         'barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot ' \
#         'currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant' \
#         ' orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
#     ss = s.split()
#     dict1 = {}
#
#     for elt in ss:
#         dict1[elt] = dict1.get(elt, 0) + 1
#     max_duplicate = max(dict1.values())
#     for elt in dict1.copy():
#         if dict1[elt] < max_duplicate:
#             dict1.pop(elt)
#     return sorted(dict1.keys())[0]
# # print(max_count_duplicate_sorted_by_lexicographic())
#
# def count_dog_in_owner():
#     pets = [('Hatiko', 'Parker', 'Wilson', 50),
#             ('Rusty', 'Josh', 'King', 25),
#             ('Fido', 'John', 'Smith', 28),
#             ('Butch', 'Jake', 'Smirnoff', 18),
#             ('Odi', 'Emma', 'Wright', 18),
#             ('Balto', 'Josh', 'King', 25),
#             ('Barry', 'Josh', 'King', 25),
#             ('Snape', 'Hannah', 'Taylor', 40),
#             ('Horry', 'Martha', 'Robinson', 73),
#             ('Giro', 'Alex', 'Martinez', 65),
#             ('Zooma', 'Simon', 'Nevel', 32),
#             ('Lassie', 'Josh', 'King', 25),
#             ('Chase', 'Martha', 'Robinson', 73),
#             ('Ace', 'Martha', 'Williams', 38),
#             ('Rocky', 'Simon', 'Nevel', 32)]
#     result = {}
#
#
#     for elt in range(len(pets)):
#         result[pets[elt][1:]] = result.get(pets[elt][1:], []) + [pets[elt][0]]
#     return result
# # print(count_dog_in_owner())
#
# def the_rarest_word(text: str)-> str:
#     """
#     https://stepik.org/lesson/446696/step/15?unit=437002
#     Самое редкое слово 🌶️
#     На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
#     без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#     :param text: 'home sweet home sweet.'
#     :return: 'home'
#     """
#     new_text = ''
#     for elt in text:
#         if elt.isalpha() or elt == ' ':
#             new_text += elt
#     new_text = list(new_text.split())
#     result = {}
#     for elt in new_text:
#         result[elt] = result.get(elt, 0) + 1
#     min_count = min(result.values())
#     for elt in result.copy():
#         if result[elt] > min_count:
#             result.pop(elt)
#     return sorted(result.keys())[0]
#
# # some_text = str(input()).lower()
# # print(the_rarest_word(some_text))
#
# def fixing_duplicates(letters: list)-> str:
#     """
#     https://stepik.org/lesson/446696/step/16?unit=437002
#     Исправление дубликатов 🌶️
#     На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так,
#      чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам
#      постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
#     :param letters: 'a b c a a d c'
#     :return: 'a b c a_1 a_2 d c_1'
#     """
#     result = {}
#     text = ''
#     for elt in letters:
#         if elt not in result:
#             result[elt] = 1
#             text += elt + ' '
#         else:
#             result[elt] += 1
#             text += elt + f'_{result.get(elt)-1}' + ' '
#
#     return text.rstrip()

# some_letters = str(input()).split()
# print(fixing_duplicates(some_letters))

# def programmer_dictionary(digit_1: int, digit_2: int):
# 	"""
# 	https://stepik.org/lesson/488831/step/1?unit=480067
# 	:param digit_1: 5
# 	Змея: язык программирования Python
# 	Баг: от англ. bug — жучок, клоп, ошибка в программе
# 	Конфа: конференция
# 	Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
# 	Бета: бета-версия, приложение на стадии публичного тестирования
#
# 	:param digit_2: 3
# 	Змея
# 	Жаба
# 	костыль
# 	:return:
# 	язык программирования Python
# 	Не найдено
# 	код, который нужен, чтобы исправить несовершенство ранее написанного кода
# 	"""
# 	temp_dict = {}
# 	for _ in range(digit_1):
# 		temp_input = str(input()).split(':')
# 		temp_dict[temp_input[0].lower()] = temp_input[1].lstrip()
#
# 	for _ in range(digit_2):
# 		key = str(input().lower())
# 		print(temp_dict.get(key, 'не найдено'))
#
# quantity_iterations = int(input())
# quantity_keys = int(input())
# programmer_dictionary(quantity_iterations, quantity_keys)


# def anagrams(word_1: str, word_2: str) -> str:
# 	"""
# 	https://stepik.org/lesson/488831/step/2?unit=480067
# 	:param word_1: thing
# 	:param word_2: night
# 	:return: YES
# 	"""
# 	result_1 = {}
# 	result_2 = {}
# 	for elt in word_1:
# 		result_1[elt] = result_1.get(elt, 0) + 1
#
# 	for elt in word_2:
# 		result_2[elt] = result_2.get(elt, 0) + 1
#
# 	if result_1 == result_2:
# 		return 'YES'
# 	else:
# 		return 'NO'
#
# input_1 = str(input())
# input_2 = str(input())
# print(anagrams(input_1, input_2))


# def anagrams_2(word_1: str, word_2: str) -> str:
# 	"""
# 	https://stepik.org/lesson/488831/step/3?unit=480067
# 	:param word_1: Вижу зверей	| Когда увидимся
# 	:param word_2: Живу резвей	| тогда и свидимся
# 	:return: YES				| NO
# 	"""
# 	spec_character = ['.', ',', '!', '?', ':', ';', '-']
# 	new_word_1 = ''
# 	new_word_2 = ''
# 	for elt in word_1:
# 		if elt in spec_character:
# 			new_word_1 += ''
# 		else:
# 			new_word_1 += elt
#
# 	for elt in word_2:
# 		if elt in spec_character:
# 			new_word_2 += ''
# 		else:
# 			new_word_2 += elt
# 	result_1 = {}
# 	result_2 = {}
# 	for elt in new_word_1:
# 		result_1[elt] = result_1.get(elt, 0) + 1
#
# 	for elt in new_word_2:
# 		result_2[elt] = result_2.get(elt, 0) + 1
#
# 	if result_1 == result_2:
# 		return 'YES'
# 	else:
# 		return 'NO'
#
# first_word = str(input()).lower().replace(' ', '')
# second_word = str(input()).lower().replace(' ', '')
# print(anagrams_2(first_word, second_word))

#
# def dictionary_synonyms() -> str:
# 	"""
# 	https://stepik.org/lesson/488831/step/4?unit=480067
# 	dict_synonyms:  Awful Terrible
# 					Beautiful Pretty
# 					Great Excellent
# 					Generous Bountiful
# 	word: 			Pretty
# 	:return:		Beautiful
# 	"""
# 	dict_synonyms = {}
# 	for _ in range(int(input())):
# 		line = str(input()).split()
# 		dict_synonyms[line[0]] = line[1]
# 	word = str(input())
# 	for k, v in dict_synonyms.items():
# 		if word == v:
# 			return k
# 		if word == k:
# 			return v
#
# # print(dictionary_synonyms())
#
# # dict_country = {'Германия': ['Берлин', 'Мюнхен', 'Гамбург', 'Дортмунд'], 'Нидерланды': ['Амстердам', 'Гаага', 'Роттердам', 'Алкмар']}
# def country_and_cities() -> str:
# 	"""
# 	https://stepik.org/lesson/488831/step/5?unit=480067
# 	country_and_city: Германия Берлин Мюнхен Гамбург Дортмунд
# 					  Нидерланды Амстердам Гаага Роттердам Алкмар
# 	city:			  Амстердам
# 					  Алкмар
# 					  Гамбург
# 					  Гаага
# 	:return:		  Нидерланды
# 					  Нидерланды
# 					  Германия
# 					  Нидерланды
# 	"""
# 	dict_country = {}
# 	for _ in range(int(input())):
# 		country_and_city = str(input()).split()
# 		dict_country[country_and_city[0]] = country_and_city[1:]
#
# 	for _ in range(int(input())):
# 		city = str(input())
# 		for k, v in dict_country.items():
# 			if city in v:
# 				return k
# # print(country_and_cities())
#
# def phone_book():
# 	"""
# 	https://stepik.org/lesson/488831/step/6?unit=480067
# 	3
# 	79184219577 Женя
# 	79194249271 Руслан
# 	79281234567 Женя
# 	3
# 	Руслан
# 	женя
# 	Рустам
# 	:return:
# 	"""
# 	s = {i: j.lower() for _ in range(int(input())) for i, j in [input().split()]}
# 	f = {}
# 	a = [input().lower() for _ in range(int(input()))]
# 	for j in a:
# 		if j not in f:
# 			for key, val in s.items():
# 				if j == val:
# 					f.setdefault(val, []).append(key)
# 	for i in a:
# 		if i not in f:
# 			print('абонент не найден')
# 		else:
# 			print(*f[i])
# phone_book()
#
# def secret_word(code: list, dict_encoding: dict) -> str:
# 	"""
# 	https://stepik.org/lesson/488831/step/7?unit=480067
# 	:param code: *!*!*?
# 	:param dict_encoding: а: 3
# 						  н: 2
# 						  с: 1
# 	:return: ананас
# 	"""
# 	new_word = ''
# 	for elt in code:
# 		letter = code.count(elt)
# 		for k, v in dict_encoding.items():
# 			if letter == int(v):
# 				new_word += k
# 	return new_word
#
# my_input = str(input())
# arr_input = list(my_input)
# my_dict = {}
# for _ in range(int(input())):
# 	key_value = str(input().replace(':', '')).split()
# 	my_dict[key_value[0]] = key_value[1]
#
# print(secret_word(arr_input,my_dict))

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {k: numbers[k]**2 for k in range(len(numbers))}
#
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
# result = {k: colors[k] for k in colors if colors[k] != None}
#
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# result = {k: favorite_numbers[k] for k in favorite_numbers if len(str(favorite_numbers[k])) == 2}
#
#
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# result = {v: k for k, v in months.items()}
#
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# result = {int(k): v for k, v in [a.split(':') for a in s.split()]}

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {numbers[k]: sorted([v for v in range(1, numbers[k]+1) if numbers[k] % v == 0]) for k in range(len(numbers))}
# print(result)


# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {words[k]: [ord(v) for v in words[k]] for k in range(len(words))}
# print(result)


# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
# 		   10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
# 		   19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {k: v for k,v in letters.items() if k not in remove_keys}
# print(result)


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
# 			'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
# 			'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
# 			'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {k:v for k,v in students.items() if v[0] > 167 and v [1] < 75}
# print(result)


# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result = {tuples[k][0]: tuples[k][1:] for k in range(len(tuples))}
# print(result)


# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
# 				 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# # result = [{k: {value2:value3}} for k, value2, value3 in zip(student_ids,student_names, student_grades)]
# # print(result)
#
# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
# 		   'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
# 		   'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
#
#
# my_dict = {k: [v for v in my_dict[k] if v < 20] for k in my_dict}
# print(my_dict)


# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#
# new_email = []
# for k, v in emails.items():
# 	for _ in v:
# 		if v == emails[k]:
# 			email = str(_) + '@' + str(k)
# 			new_email.append(email)
#
# new_email.sort()
# for _ in new_email:
# 	print(_)


# a = list(str(input()))
# # print(a)
# a = ['A', 'C', 'T', 'G']
# dnk = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# new_dnk = ''
# for _ in a:
# 	new_dnk += dnk[_]
# print(new_dnk)


# line = 'прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон'.split()
# print(line)
#
# my_dict = {}
# answer = ''
# for elt in line:
# 	my_dict[elt] = my_dict.get(elt, 0) +1
# 	print(my_dict[elt])
# 	answer += str(my_dict[elt]) + ' '
# print(answer.rstrip())



# a = 'DANSER'
#
# dict1 = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
#
#
# count = 0
# for elt in a:
# 	for k, v in dict1.items():
# 		for _ in v:
# 			if elt == _:
# 				count += k
# print(count)


# d1 = {'sport': 'hockey', 'game': 2, 'time': 17}
#
# def build_query_string(params):
# 	arr = []
# 	for k,v in params.items():
# 		n = str(k) + '=' + str(v)
# 		arr.append(n)
# 	arr.sort()
# 	return '&'.join(arr)
#
# print(build_query_string(d1))


#
# def merge(values):      # values - это список словарей
# 	result = {}
# 	for elt in values:
# 		for k, v in elt.items():
# 			result.setdefault(k, set()).add(v)
# 	return result
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# temp = []
# for _ in range(int(input())):
# 	arr = str(input())
# 	temp.append(arr.split())
# print(temp)
# temp_comand = []
# for _ in range(int(input())):
# 	arr = str(input())
# 	temp_comand.append(arr.split())
# print(temp_comand)



# temp_file = [['my_pycode.exe', 'W', 'X'], ['log_n', 'X', 'W', 'R'], ['ave', 'R'], ['lucky_m', 'W', 'R'], ['dnsss.py', 'W']]
# temp_comand = [['execute', 'ave'], ['read', 'dnsss.py'], ['write', 'log_n'], ['execute', 'log_n'], ['read', 'ave'], ['write', 'my_pycode.exe']]
# # result = {}
# # dict_operations = {'X': 'execute', 'R': 'read', 'W': 'write'}
# # for _ in range(int(input())):
# # 	x = input().split()
# # 	result[x[0]] = [dict_operations[i] for i in x[1:]]
# #
# # for _ in range(int(input())):
# # 	x = input().split()
# # 	if x[0] in result[x[1]]:
# # 		print('OK')
# # 	else:
# # 		print('Access denied')



# result = {}
# for _ in range(int(input())):
# 	name, product, count = input().split()
# 	result.setdefault(name, {})
# 	result[name][product] = result[name].get(product, 0) + int(count)
#
# for key, value in sorted(result.items()):
# 	print(f"{key}:")
# 	for i in sorted(value):
# 		print(i, value[i])
#

table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
count = 0

difference = 0
s = "MCMXCIV"
for _ in s:
	count += table[_]


if 'CM' in s or 'CD' in s:
	count -= table['C'] * 2
if 'IV' in s or 'IX' in s:
	count -= table['I'] * 2
if 'XL' in s or 'XC' in s:
	count -= table['X'] * 2

print(count)