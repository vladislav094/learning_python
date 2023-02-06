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

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {numbers[k]: sorted([v for v in range(1, numbers[k]+1) if numbers[k] % v == 0]) for k in range(len(numbers))}
print(result)