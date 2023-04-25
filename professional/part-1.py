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
def filter_anagrams(word: str, words: list)-> list:
	my_dict = {}
	result = []
	for elt in word:
		my_dict[elt] = my_dict.get(elt, 0) + 1

	for elt in words:
		tempt_dict = {}
		for letter in elt:
			tempt_dict[letter] = tempt_dict.get(letter, 0) + 1
		if tempt_dict == my_dict:
			result.append(elt)
	return result

w = 'abba'
a = ['aabb', 'abcd', 'bbaa', 'dada']
print(filter_anagrams(w, a))