#1
card = '3456 9012 5678 1234'
def hide_card(card_number: str)-> str:
	card_number = card_number.replace(' ', '')
	card_number = '*' * 12 + card_number[12:]
	return card_number
print(hide_card(card))


