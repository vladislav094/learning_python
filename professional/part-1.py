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
def print_given(*args, **kwargs):
	for elt in args:
		print(elt, type(elt))
	for k, v in sorted(kwargs.items()):
		print(k, v, type(v))

print_given(1, [1, 2, 3], 'three', two=2)
