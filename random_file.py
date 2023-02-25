import random
import string
import itertools
import math

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


# from math import gcd
# from fractions import Fraction
# n = int(input())
# result = []
# while n != 1:
#     for i in range(1, n):
#         if gcd(i, n) == 1:
#             result.append(f'{i}/{n}')
#     n -= 1
# answer = sorted(map(Fraction, result))
# print(*answer, sep='\n')


# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# # a1 = ["tarp", "mice", "bull"]
# # a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# def in_array(array1, array2):
#     temp = []
#     for elt in range(len(array1)):
#         for jet in range(len(array2)):
#             if array1[elt] in array2[jet] and array1[elt] not in temp:
#                 temp.append(array1[elt])
#     temp.sort()
#     return temp

# print(in_array(a1, a2))


# a = [1, 1, 3, 3, 7, 2 ,2, 2, 2]
# dig = 3
# b = [20, 37, 20, 21]
# digi_2 = 1
#
# def delete_nth(arr, digit):
#     temp = []
#     for elt in arr:
#         if temp.count(elt) < digit:
#             temp.append(elt)
#     return temp
# print(delete_nth(a, dig))
# print(delete_nth(b, digi_2))

# a = 'apple ban'
# b = 'you will win'
#
# def add_length(str_):
#     arr = str_.split()
#     result = []
#     for elt in arr:
#         t_str = str(elt) + ' ' + str(len(elt))
#         result.append(t_str)
#     return result
# print(add_length(a))




# def josephus_survivor(n,k):
#     '''
#     Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements,
#     like this:
#     josephus_survivor(7,3) => means 7 people in a circle;
#     one every 3 is eliminated until one remains
#     [1,2,3,4,5,6,7] - initial sequence
#     [1,2,4,5,6,7] => 3 is counted out
#     [1,2,4,5,7] => 6 is counted out
#     [1,4,5,7] => 2 is counted out
#     [1,4,5] => 7 is counted out
#     [1,4] => 5 is counted out
#     [4] => 1 counted out, 4 is the last element - the survivor!
#     :param n:
#     :param k:
#     :return:
#     '''
#     my_iter = [int(x) for x in range(1, n+1)]
#     while len(my_iter) > 1:
#         x = (k -1) % (len(my_iter))
#         my_iter = my_iter[x+1:] + my_iter[:x]
#     return my_iter[0]
# print(josephus_survivor(11, 19))

#
# def line_up(hints):
#     w = 'white'
#     b = 'black'
#     r = 'red'
#     g = 'green'



# color = ["white has black on his left",
#          "red has green on his right",
#          "black has green on his left"]
#
# temp = ['white', 'black', 'red', 'green']
# a = color[0].split()
# b = color[0].split()
# c = color[0].split()
# print(a, type(a))


# def strong_num(number):
#     arr = str(number)
#     total = 0
#     for elt in arr:
#         total += math.factorial(int(elt))
#     if total == int(number):
#         return 'STRONG!!!!'
#     else:
#         return 'Not Strong !!'
# print(strong_num(185))


# def give_change(money: int):
#     arr = []
#     for i in [100, 50, 20, 10, 5, 1]:
#         arr = [money // i] + arr
#         money -= arr[0] * i
#     return tuple(arr)
#
# print(give_change(365))

def sq_sum(*args):
    argss = 0
    for elt in args:
        argss += elt ** 2
    return argss

# print(sq_sum(1.5, 2.5))

def mean(*args):
    result = []
    for elt in args:
        if type(elt) is int or type(elt) is float:
            result.append(elt)
    if len(result) == 0:
        return 0.0
    else:
        return sum(result) / len(result)
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#
# def greet(name, *args):
#     result = f'Hello, {name}!'
#     if len(args) == 0:
#         return result
#     else:
#         return f"{result[:-1]} and {' and '.join(args)}!"
#
# print(greet(name="Timur"))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))


# def print_products(*args):
#     products = ['Бананы', 'Яблоки', 'Макароны']
#     result = []
#     for elt in args:
#         if type(elt) is str:
#             result.append(elt)
#     counter = 1
#     for _ in result:
#         if len(_) == 0:
#             result.remove(_)
#     if len(result) > 0:
#         for elt in result:
#             if elt in products:
#                 print(f"{str(counter)}) {elt}")
#                 counter += 1
#     else:
#         print("Нет продуктов")
#
# # print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# # print_products([4], {}, 1, 2, {'Beegeek'}, '')
#
# def print_products_2(*args):
#     counter = 1
#     flag = False
#     for elt in args:
#         if type(elt) is str and len(elt) > 0:
#             print(f"{counter}) {elt}")
#             flag = True
#             counter +=1
#     if flag == False:
#         print(f"Нет продуктов")
# print_products_2('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products_2([4], {}, 1, 2, {'Beegeek'}, '')
#
#
# def info_kwargs(**kwargs):
#     for k,v in sorted(kwargs.items()):
#         print(f"{k}: {v}")
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')


# def generator_square_polynom(a, b, c):
#     def square_polynom(x):
#         return a*x**2 + b*x + c
#     return square_polynom
#
# f = generator_square_polynom(a=1, b=2, c=1)
# print(f(1))
# print(input)

# def comparator(pair):
#     return pair[0] + pair[1]
#
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator, reverse=True)
# print(pairs)


# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# def comparator(x):
#     return sum(x) / len(x)
#
# print(min(numbers, key=comparator))
# print(max(numbers, key=comparator))
#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def comparator(x):
#     return ((x[0] ** 2) + (x[1] ** 2)) ** 0.5
#
# print(sorted(points, key=comparator))

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def comparator(x):
#     return max(x) +min(x)
#
# numbers.sort(key=comparator)
# print(numbers)


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

# digit = int(input())
digit = 3

def comparator(x):
    return x[digit-1]

for elt in sorted(athletes, key=comparator):
    print(*elt)

