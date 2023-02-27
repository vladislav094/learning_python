import random
import string
import itertools
import math
from operator import *
from functools import reduce
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


# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# digit = 3
#
# def comparator(x):
#     return x[digit-1]
#
# for elt in sorted(athletes, key=comparator):
#     print(*elt)


# def f1(x):
#     return x ** 2
#
# def f2(x):
#     return x ** 3
#
# def f3(x):
#     return x ** 0.5
#
# def f4(x):
#     return abs(x)
#
# def f5(x):
#     return math.sin(x)
#
# my_dict = {"квадрат": f1, "куб": f2, "корень": f3, "модуль": f4, "синус": f5}
# digit = int(input())
# word = str(input())
# list_functions = [f1, f2, f3, f4, f5]
# print(my_dict.get(word)(digit))


# inpt = str(input()).split()
# print(inpt)
# my_list = ['12', '14', '79', '7', '4', '123', '45', '90', '111']
# my_list = ['111', '14', '79', '7', '4', '123', '90', '45', '12', '171']
# my_list = sorted(my_list, key=int)
# def comparator(x):
#     s = 0
#     for elt in x:
#         s += int(elt)
#     return s
#
# print(*sorted(my_list, key=comparator))


# def f(x):
#     return str(x)
#
# old_list = [1, 2, 4, 9, 10, 25]
# new_list = []
# for item in old_list:
#     new_item = f(item)
#     new_list.append(new_item)
# print(new_list)

# def map(functions, items):
#     result = []
#     for item in items:
#         new_item = functions(item)
#         result.append(new_item)
#     return result
#
# def square(x):
#     return x**2
#
# def cube(x):
#     return x**3
#
# numbers = [1, 2, -3, 4, -5, 6, -9, 0]
# strings = map(cube, numbers)
# print(strings)
#
#
# numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']
# new_numbers = map(abs, map(int, numbers))
# print(new_numbers)

#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def is_greater10(num):
#     return num > 10
#
# numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]
#
# print(filter(is_greater10, numbers))
#
# def is_odd(num):
#     return num % 2
#
# def is_word_long(word):
#     return len(word) > 6
#
# numbers = list(range(15))
# words = ['В', 'новом', 'списке', 'останутся', 'только', 'длинные', 'слова']
#
# odd_numbers = filter(is_odd, numbers)
# large_words = filter(is_word_long, words)
#
# print(odd_numbers)
# print(large_words)

# numbers = [1, 2, 3, 4, 5]
#
# total = 0
# product = 1
# for num in numbers:
#     total += num
#     product *= num
#
# print(total)
# print(product)

# def reduce(operation, items, initials_value):
#     acc = initials_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def add(x, y):
#     return x+y
#
#
# def mult(x, y):
#     return x*y
#
#
# numbers = [1, 2, 3, 4, 5]
# print(reduce(add, numbers, 1))

#
# def high_order_function(func):
#     return func(10)
#
#
# def square(x):
#     return x**2
#
#
# def minus_one(x):
#     return x - 1
#
#
# num1 = high_order_function(square)
# num2 = high_order_function(minus_one)
#
# print(num1*num2)


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def f(x):
#     return round(x, 2)
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# new_numbers = map(f, numbers)
# for _ in new_numbers:
#     print(_)


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
#            1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289,
#            1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013,
#            898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336,
#            1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
#
# def separator(x):
#     if len(str(x)) == 3:
#         return x % 5 == 2
#
# def square(x):
#     return x ** 3
#
# numbers = filter(separator, numbers)
# numbers = map(square, numbers)
# for _ in numbers:
#     print(_)



# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def square(a, b):
#     return a + (b **2)
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
#            72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
#            7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# new_numbers = reduce(square, numbers, 0)
# print(new_numbers)


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
#            219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35
#     , 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187,
#            220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211,
#            5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79,
#            -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10,
#            250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
#
# def square(x):
#     return x ** 2
#
# def is_len_2(x):
#     return len(str(abs(x))) == 2
#
# def get_sep_7(x):
#     return x % 7 == 0
#
# new_numbers = filter(is_len_2, numbers)
# new_numbers = filter(get_sep_7, new_numbers)
# print(sum(map(square, new_numbers)))

# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
# def func_apply(operation, items):
#     result = []
#     for item in items:
#         x = operation(item)
#         result.append(x)
#     return result
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

# def gcdi(x,y):
#     return math.gcd(abs(x), abs(y))
# def lcmu(a, b):
#     return math.lcm(abs(a), abs(b))
# def som(a, b):
#     return a + b
# def maxi(a, b):
#     return max(a, b)
# def mini(a, b):
#     return min(a, b)
# def oper_array(fct, arr, init):
#     result = []
#     inc = init
#     for item in arr:
#         inc = fct(inc, item)
#         result.append(inc)
#     return result
# a = [18, 69, -90, -78, 65, 40]
#
# print(oper_array(gcdi, a, a[0]))
# print(oper_array(lcmu, a, a[0]))
# print(oper_array(som, a, 0))
# print(oper_array(mini, a, a[0]))
# print(oper_array(maxi, a, a[0]))


# lambda_function = lambda x, y, z: x * y + z
# print(lambda_function(12, 2, 3))


# def compare_by_second(point):
#     return point[1]
#
#
# def compare_by_sum(point):
#     return point[0] + point[1]
#
#
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points, key=lambda point: point[1] + point[0]))

#
# numbers = [-2, 0, 1, 2, 17, 4, 5, 6]
#
# new_numbers = list(map(lambda x: 'even' if x % 2 == 0 else 'add', numbers))
# print(new_numbers)


# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# obj = list(filter(lambda x: x % 2 == 1, obj))
# print(obj)

# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**3, 1), floats))
# filter_result = list(filter(lambda name: name if name == name[::-1] and len(name) > 4 else None, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
#
# new_data = list(filter(lambda x: x if x[1] > 10000000 and x[2] == 'primary' else None, data))
# new_data = list(map(lambda x: x[0], new_data))
# another_one_data = sorted(new_data)
# another_one_data_1 = list(reduce(lambda x, y: x+', '+ y, another_one_data[1:], 'Cities: ' + another_one_data[0]))
#
# print(''.join(another_one_data_1))


func = lambda x: True if x % 13 ==0 or x % 19 == 0 else False
print(func(20))