# # объявление функции
"""Палиндром"""
# def is_palindrome(text):
# 	string2 = ' ,.!?-'
# 	list1 = []
# 	for elt in range(len(text)):
# 		if text[elt] not in string2:
# 			list1.append(text[elt])
# 	string3 = ''.join(list1).lower()
#
# 	if string3 == string3[::-1]:
# 		return True
# 	else:
# 		return False
#
# # считываем данные
# txt = input()
#
# вызываем функцию
# print(is_palindrome(txt))


# объявление функции
"""BEEGEEK"""
# def is_valid_password(password):
# 	all_count = 0
# 	list_tmp = password.split(':')
# 	digital0 = list_tmp[0]
# 	digital1 = int(list_tmp[1])
# 	digital2 = int(list_tmp[2])
# 	if len(list_tmp) == 3:
# 		if digital0 == digital0[::-1]:
# 			all_count += 1
#
# 		count = 0
# 		for elt in range(digital1, 0, -1):
# 			if digital1 % elt == 0:
# 				count += 1
# 		if count == 2:
# 			all_count +=1
#
# 		if digital2 % 2 == 0:
# 			all_count += 1
#
# 		if all_count == 3:
# 			return True
# 		else:
# 			return False
# 	else:
# 		return False
#
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))


# # объявление функции
# """Правильная скобочная последовательность"""
# def is_correct_bracket(text):
#     count = 0
#     for elt in range(len(text)):
#         if text[elt] == '(':
#             count += 1
#         else:
#             count -= 1
#         if count < 0:
#             break
#         else:
#             continue
#     if count == 0:
#         return True
#     else:
#         return False
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))


# объявление функции
# """Змеиный регистр"""
# def convert_to_python_case(string1):
#     s = ''
#     for elt in range(len(string1)):
#         if elt != 0 and string1[elt].isupper():
#             s += '_'
#             s += string1[elt]
#         else:
#             s += string1[elt]
#     return s.lower()
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))


# объявление функции
# """Середина отрезка"""
# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# import math
# # объявление функции
# # """Площадь и длина"""
# def get_circle(radius):
#     p = math.pi
#     length = 2 * p * radius
#     square = p * radius ** 2
#     return length, square
# # считываем данные
# r = float(input())
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)


# объявление функции
# """Корни уравнения"""
# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     x1 = (-b - d ** 0.5) / (2 * a)
#     x2 = (-b + d ** 0.5) / (2 * a)
#     return min(x1, x2), max(x1, x2)
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)


# объявление функции
# def is_magic(date):
#     pass
#
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))

# объявление функции
# def is_pangram(text):
# 	s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
# 		 'first_less_second', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
# 		 'u', 'v', 'w', 'x', 'y', 'z']
# 	text = text.replace(' ', '')
# 	text = text.lower()
# 	for elt in text:
# 		if elt not in s:
# 			return False
# 	return True
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))

