#1
# card = '3456 9012 5678 1234'
# def hide_card(card_number: str)-> str:
# 	card_number = card_number.replace(' ', '')
# 	card_number = '*' * 12 + card_number[12:]
# 	return card_number
# print(hide_card(card))

#2

arr = [6, 0, 67, -7, 10, -20]
def same_parity(numbers):
	result = []
	if len(numbers) == 0:
		return []
	else:
		x = numbers[0]
		for elt in numbers:
			if elt % 2 == x % 2:
				result.append(elt)
	return result

print(same_parity(arr))


