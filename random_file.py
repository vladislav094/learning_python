import random
import string


# ticket = int(input())
#
# result = []
# for _ in range(ticket):
# 	result.append(random.randint(1, 49))
# for _ in sorted(result):
# 	print(_)

# def generate_ip():
# 	ip = str(random.randint(100, 255)) + '.' + str(random.randint(100, 255)) + '.' + str(random.randint(1,9)) + '.' + str(random.randint(100, 255))
# 	return ip
#
# print(generate_ip())


# def generate_index():
# 	s1 = [x for x in random.sample(string.ascii_uppercase, 2)]
# 	s2 = [x for x in random.sample(string.digits, 2)]
# 	s3 = [x for x in random.sample(string.ascii_uppercase, 2)]
# 	number = s1 + s2 + ['_'] + s2 + s3
# 	return ''.join(number)
#
# print(generate_index())


# def shuffle():
# 	matrix = [[1, 2, 3, 4],
# 			  [5, 6, 7, 8],
# 			  [9, 10, 11, 12],
# 			  [13, 14, 15, 16]]
# 	random.shuffle(matrix)
# 	return  matrix
#
# print(shuffle())


# def ticket():
# 	arr = []
# 	while len(arr) < 100:
# 		arr.append(random.sample(string.digits[1:], 7))
# 	for elt in arr:
# 		print(''.join(elt))
# ticket()

# def anagramms():
# 	word = ' '.join(str(input())).split(' ')
# 	random.shuffle(word)
# 	word = str(''.join(word))
# 	print(word, type(word))
# anagramms()

# arr = [*range(1, 76)]
# random.shuffle(arr)
# arr = random.sample(arr, 25)
# bingo = [[str(arr.pop()).ljust(3) for _ in range(5)] for _ in range(5)]
# bingo[2][2] = str(0)
# for i in bingo:
# 	for j in i:
# 		print(str(j).ljust(3), end='')
# 	print()


# def sattolo_cycle():
# 	general_list = ['Djaja Bings', 'Tom Brankock', 'Ada Swarovsky']
# 	# general_list = []
# 	# for _ in range(int(input())):
# 	# 	general_list.append(str(input()))
# 	general_list_copy = general_list.copy()
# 	i = len(general_list_copy)
# 	while i > 1:
# 		i = i - 1
# 		j = random.randrange(i)
# 		general_list_copy[j], general_list_copy[i] = general_list_copy[i], general_list_copy[j]
# 	for elt in range(len(general_list_copy)):
# 		print(f"{general_list[elt]} - {general_list_copy[elt]}")



# cc = int(input())
# ll = int(input())
# def generate_password(l: int):
# 	up_alpha = string.ascii_uppercase
# 	low_alpha = string.ascii_lowercase
# 	digits = string.digits
# 	chracters_to_delet = ['l', 'I', '1', 'o', 'O', '0']
# 	for elt in chracters_to_delet:
# 		if elt in up_alpha:
# 			up_alpha = up_alpha.replace(elt, '')
# 		if elt in low_alpha:
# 			low_alpha = low_alpha.replace(elt, '')
# 		if elt in digits:
# 			digits = digits.replace(elt, '')
#
# 	password = list(random.choice(up_alpha) + ''.join(random.sample(low_alpha, l-2)) + random.choice(digits))
# 	random.shuffle(password)
# 	password = ''.join(password)
# 	return password
#
# def generate_passwords(count, length):
# 	arr = [generate_password(length) for _ in range(count)]
# 	for x in arr:
# 		print(x)
# #
# generate_passwords(cc, ll)



# n = 10**6       # количество испытаний
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)     # случайное число с плавающей точкой от 0 до 1
#     y = random.uniform(-2, 2)     # случайное число с плавающей точкой от 0 до 1
#
#     if x ** 3 + y ** 4 + 2 >= 0 and (3 * x) + y ** 2 <= 2:                # если попадает в нужную область
#         k += 1
#
# print((k/n)*s0)

from decimal import *
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 ' \
# 	'0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 ' \
# 	'7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 ' \
# 	'5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
#
# arr = [Decimal(x) for x in s.split()]
# print(Decimal(sum(arr)))
# arr.sort()
#
# iteration = 0
# while iteration < 5:
# 	print(arr.pop(), end=' ')
# 	iteration += 1



# num = str(Decimal(input())).replace('.', '')
# new_num = ''
# for elt in num:
# 	if elt.isdigit():
# 		new_num += elt
# arr = list(' '.join(new_num).split())
# print(int(max(arr)) + int(min(arr)))

# d = Decimal(1.1)
# d = Decimal(input())
# print(Decimal.exp(d) + Decimal.ln(d) + Decimal.log10(d) + Decimal.sqrt(d))



from fractions import Fraction
from math import factorial
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29',
# 		   '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62',
# 		   '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25',
# 		   '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# for elt in numbers:
# 	print(f"{elt} = {Fraction(elt)}")



# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46' \
# 	' 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 ' \
# 	'9.60 8.86 2.73 5.83 6.50 0.123 0.00021'.split()
#
# s = [Fraction(x) for x in s]
# print(max(s) + min(s))

# first = input()
# second = input()
# print(f"{first} + {second} = {Fraction(first) + Fraction(second)}")
# print(f"{first} - {second} = {Fraction(first) - Fraction(second)}")
# print(f"{first} * {second} = {Fraction(first) * Fraction(second)}")
# print(f"{first} / {second} = {Fraction(first) / Fraction(second)}")


from math import gcd
from fractions import Fraction
n = int(input())
result = []
while n != 1:
    for i in range(1, n):
        if gcd(i, n) == 1:
            result.append(f'{i}/{n}')
    n -= 1
answer = sorted(map(Fraction, result))
print(*answer, sep='\n')

