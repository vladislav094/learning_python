#1
# card = '3456 9012 5678 1234'
# def hide_card(card_number: str)-> str:
# 	card_number = card_number.replace(' ', '')
# 	card_number = '*' * 12 + card_number[12:]
# 	return card_number
# print(hide_card(card))

#2
# arr = [6, 0, 67, -7, 10, -20]
# def same_parity(numbers):
# 	result = []
# 	if len(numbers) == 0:
# 		return []
# 	else:
# 		x = numbers[0]
# 		for elt in numbers:
# 			if elt % 2 == x % 2:
# 				result.append(elt)
# 	return result
#
# print(same_parity(arr))

#3
# pin_code = '43 67'
# def is_valid(pin):
# 	if len(pin) >=4 and len(pin) <= 6 and pin.isdigit():
# 		return True
# 	else:
# 		return False
#
# print(is_valid(pin_code))


#4
# def print_given(*args, **kwargs):
# 	for elt in args:
# 		print(elt, type(elt))
# 	for k, v in sorted(kwargs.items()):
# 		print(k, v, type(v))
#
# print_given(1, [1, 2, 3], 'three', two=2)


#5
# def convert(string: str)-> str:
# 	low_letter = 0
# 	up_letter = 0
# 	for elt in string:
# 		if elt.isupper():
# 			up_letter += 1
# 		if elt.islower():
# 			low_letter += 1
# 	if low_letter >= up_letter:
# 		return string.lower()
# 	else:
# 		return string.upper()
#
# print(convert('BEEgeek'))
# print(convert('pi31415!'))
# print(convert('pyTHON'))


#6
# def filter_anagrams(word: str, words: list)-> list:
# 	my_dict = {}
# 	result = []
# 	for elt in word:
# 		my_dict[elt] = my_dict.get(elt, 0) + 1
#
# 	for elt in words:
# 		tempt_dict = {}
# 		for letter in elt:
# 			tempt_dict[letter] = tempt_dict.get(letter, 0) + 1
# 		if tempt_dict == my_dict:
# 			result.append(elt)
# 	return result
#
# w = 'abba'
# a = ['aabb', 'abcd', 'bbaa', 'dada']
# print(filter_anagrams(w, a))


#7
# def likes(names: list)-> str:
# 	if len(names) == 0:
# 		return "Никто не оценил данную запись"
# 	if len(names) == 1:
# 		return f"{names[0]} оценил(а) данную запись"
# 	if len(names) == 2:
# 		return f"{names[0]} и {names[1]} оценили данную запись"
# 	if len(names) > 3:
# 		names[2] = f"{len(names) - 2} других"
# 	return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
#
# print(likes([]))
# print(likes(['Тимур']))
# print(likes(['Тимур', 'Артур']))
# print(likes(['Тимур', 'Артур', 'Руслан']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))


#8
# def index_of_nearest(numbers, number):
# 	if len(numbers) == 0:
# 		return -1
# 	else:
# 		result = []
# 		my_indx = 0
# 		for elt in numbers:
# 			if elt > number:
# 				result.append(len(range(number, elt)))
# 			else:
# 				result.append(len(range(elt, number)))
# 		minimum = min(result)
# 		for elt in range(len(result)):
# 			if result[elt] == minimum:
# 				my_indx = elt
# 				break
# 		return my_indx
#
# arr = [7, 13, 3, 5, 18]
# num = 0


#9
# def spell(*args):
# 	my_dict = {}
# 	my_set = set()
# 	for elt in args:
# 		my_set.add(elt[0].lower())
# 	for s in my_set:
# 		my_dict[s] = max([len(x) for x in args if s == x[0].lower()])
# 	return my_dict
#
# w = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
# print(spell(*w))


#10
# def choose_plural(amount: int, declensions: tuple)-> str:
# 	str_amount = str(amount)
# 	if int(str_amount[-1]) == 1 and int(str_amount[-2]) != 1:
# 		return f'{amount} {declensions[0]}'
# 	if len(str_amount) >= 2 and int(str_amount[-2]) > 1 and int(str_amount[-1]) in [2, 3, 4] or amount in [2, 3, 4]:
# 		return f'{amount} {declensions[1]}'
# 	else:
# 		return f'{amount} {declensions[2]}'
#
# print(choose_plural(21, ('пример', 'примера', 'примеров')))
# print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
# print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
# print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
# print(choose_plural(512312, ('цент', 'цента', 'центов')))
# print(choose_plural(11, ('стул', 'стула', 'стульев')))
# print(choose_plural(2, ('пример', 'примера', 'примеров')))


#11
def get_biggest(numbers: list)-> int:
	if numbers:
		b = [str(x) for x in numbers]
		c = len(max(b, key=len))
		return abs(int(''.join(sorted(b, reverse=True, key=lambda x:str(x) * c))))
	else:
		return -1

print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
print(get_biggest([0, 0, 0, 0, 0, 0]))