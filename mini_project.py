# def ave_caesar(word: str) -> str:
# 	new_word = []
# 	for elt in word.split():
# 		ss = ''
# 		x = len([c for c in elt if c.isupper() or c.islower()])
# 		for j in elt:
# 			if j.isupper():
# 				ss += chr((ord(j) + x - 65) % 26 + 65)
# 			elif j.islower():
# 				ss += chr((ord(j) + x - 97) % 26 + 97)
# 			else:
# 				ss += j
# 		new_word.append(ss)
# 	return ' '.join(new_word)
# word = input()
# print(ave_caesar(word))

# def hexadecimal_to_decimal(text: str, system: int) -> int:
# 	x = system
# 	count = 0
# 	lenght = len(bin_digit)-1
# 	d = lenght
# 	for elt in range(lenght+1):
# 		if text[elt].isdigit():
# 			count += int(text[elt]) * (x ** d)
# 			print('1',count, text[d], d, elt)
# 			d -= 1
# 		else:
# 			count += (ord(text[elt]) - 55)  * (x ** d)
# 			print('2',count, text[d], d, elt)
# 			d -= 1
# 	return count
#
# bin_digit = '1AF2'
# system = 16
# print(hexadecimal_to_decimal(bin_digit, system))

# def decimal_to_binary(digital: int) -> str:
# 	b = ''
# 	digit = digital
# 	while digit > 0:
# 		b = str(digit % 2) + b
# 		digit = digit // 2
# 	return b
# n = int(input())
# print(decimal_to_binary(n))


def output(digital: int):
	b = bin(digital)
	x = hex(digital).upper()
	o = oct(digital)
	arr = [int(b[2:]), int(o[2:]), x[2:]]
	for elt in arr:
		print(elt)

n = int(input())
output(n)