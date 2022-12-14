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


# def output(digital: int):
# 	b = bin(digital)
# 	x = hex(digital).upper()
# 	o = oct(digital)
# 	arr = [int(b[2:]), int(o[2:]), x[2:]]
# 	for elt in arr:
# 		print(elt)
#
# n = int(input())
# output(n)


# def cost_string(text: str) -> str:
# 	return str(len(text.split()))
#
# text = 'Я собираюсь сделать ему предложение, от которого он не сможет отказаться.'
# print(cost_string(text))
#
#
# def zodiac(year: int) -> str:
# 	arr = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца", ]
# 	x = year % 12
# 	return arr[x]
#
# dig = 2020
# print(zodiac(dig))


# def revers_nuber(digit: int) -> int:
# 	string_of_digit = str(digit)
# 	if len(string_of_digit) > 5:
# 		sub_string = string_of_digit[1:]
# 		new_digit = string_of_digit[0] + sub_string[::-1]
# 	else:
# 		new_digit = string_of_digit[::-1]
# 	return int(new_digit)
#
# print(revers_nuber(987654))


# def decimal_separator(digit: int) -> str:
# 	return '{:,}'.format(digit)
#
# x = int(input())
# print(decimal_separator(x))


# def task_flavius(arr: int, digit: int) -> int:
# 	count = 0
# 	for elt in range(1, arr +1):
# 		count = (count + digit) % elt
# 	return count+1
#
# arr = int(input())
# digit = int(input())
# print(task_flavius(arr,digit))


# def coordinate_quarters(dot_count: int) -> str:
# 	I = 0
# 	II = 0
# 	III = 0
# 	IV = 0
# 	count = dot_count
# 	while count != 0:
# 		arr = str(input()).split()
# 		x = int(arr[0])
# 		y = int(arr[1])
# 		if x > 0 and y > 0:
# 			I += 1
# 		elif x < 0 and y > 0:
# 			II += 1
# 		elif x < 0 and y < 0:
# 			III += 1
# 		elif x > 0 and y < 0:
# 			IV += 1
# 		count -= 1
# 	return f"Первая четверть: {I} \nВторая четверть: {II} \nТретья четверть: {III} \nЧетвертая четверть: {IV}"
#
# dot_count = int(input())
# print(coordinate_quarters(dot_count))



# def back_forward_versa(string_1: str) -> str:
# 	arr = string_1.split()
# 	if len(arr) % 2 != 0:
# 		for _ in range(len(arr) - 1):
# 			if arr.index(arr[_]) % 2 == 0:
# 				arr[_], arr[_ + 1] = arr[_ + 1], arr[_]
# 	else:
# 		for j in range(0, len(arr) - 1, 2):
# 			arr[j], arr[j + 1] = arr[j + 1], arr[j]
# 	return ' '.join(arr)
#
# string_1 = '216 39 87 0 0 1 0'
# print(back_forward_versa(string_1))



# def shift_in_development(string_1: str) -> str:
# 	arr = string_1.split()
# 	d = arr[len(arr) -1]
# 	del arr[len(arr) -1]
# 	digital = list(d)
# 	digital += arr
# 	return ' '.join(digital)
#
# string_1 = str(input())
# print(shift_in_development(string_1))


# def different_elements(string_1: str) -> int:
# 	a = string_1.split()
# 	count = 1
# 	for elt in range(len(a) - 1):
# 		if int(a[elt]) != int(a[elt + 1]):
# 			count += 1
# 	return count
#
# string_1 = str(input())
# print(different_elements(string_1))


# def product_of_numbers():
#     arr = [int(input()) for _ in range(int(input()))]
#     digital = int(input())
#     true = False
#     for elt in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[elt] * arr[j] == digital and elt != j:
#                 true = True
#                 break
#     if true:
#         return 'ДА'
#     else:
#         return 'НЕТ'
#
# print(product_of_numbers())


# def rock_scissors(word_1: str, word_2: str):
#     a = 'ножницыбумагакаменьящерицаСпокножницыящерицабумагаСпоккаменьножницы'
#     if word_1 == word_2:
#         return 'ничья'
#     elif word_1 + word_2 in a:
#         return 'Тимур'
#     else:
#         return 'Руслан'
# word_1 = str(input())
# word_2 = str(input())
# print(rock_scissors(word_1, word_2))


# def heads_and_tails(word: str) -> int:
#     arr = word.split('О')
#     return len(max(arr))
#
# text_1 = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
# print(heads_and_tails(text_1))



# def silicon_valley(count_iter: int):
#     arr = []
#     for _ in range(1, count_iter+1):
#         word = str(input())
#         count = len(word)
#         new_word = ''
#         for elt in range(count):
#             if new_word == '' and word[elt] == 'a':
#                 new_word += word[elt]
#             if new_word == 'a' and word[elt] == 'n':
#                 new_word += word[elt]
#             if new_word == 'an' and word[elt] == 't':
#                 new_word += word[elt]
#             if new_word == 'ant' and word[elt] == 'o':
#                 new_word += word[elt]
#             if new_word == 'anto' and word[elt] == 'n':
#                 new_word += word[elt]
#         if new_word == 'anton':
#             arr.append(str(_))
#     return ' '.join(arr)
#
# count_iter = int(input())
# print(silicon_valley(count_iter))



# def denied_access(word: str):
#     b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
#          'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#     text = word + ' запретил букву'
#     for elt in range(len(b)):
#         text = ' '.join(text.split())
#         if b[elt] in text:
#             print(text, b[elt])
#             text = text.replace(b[elt], '')
#
# text = 'яндекс'
# denied_access(text)


# объявление функции
# def func(num1, num2):
#     if num1 % num2 == 0:
#         return True
#     else:
#         return False
#
# # считываем данные
# num1, num2 = int(input()), int(input())
#
# # вызываем функцию
# if func(num1, num2):
#     print('делится')
# else:
#     print('не делится')

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for elt in list1:
# 	d = max(elt)
# 	if d > maximum:
# 		maximum = d
#
# print(maximum)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for elt in list1:
# 	counter += len(elt)
# 	for j in elt:
# 		total += j
# print(counter, total)


# my_list = []
# for _ in range(4):
# 	elem = [int(i) for i in input().split()]
# 	my_list.append(elem)
# print(my_list)


# def output_list(dig: int):
# 	arr = [x for x in range(1, dig+1)]
# 	for _ in range(dig):
# 		print(arr)
#
# digital = int(input())
# output_list(digital)

# def nested_list(digit: int):
# 	arr = []
# 	for elt in range(1, digit+ 1):
# 		temp = []
# 		for j in range(elt):
# 			temp.append(j + 1)
# 		arr.insert(elt, temp)
# 	for row in arr:
# 		print(row, end=' ')
# 		print()
# dig = int(input())
# nested_list(dig)

# arr = [[x for x in range(1, 4)] for _ in range(1,4)]


# import math
# def pascal(n: int) -> list:
# 	arr = []
# 	count = 1
# 	for i in range(n+1):
# 		arr.append(int(math.factorial(n) / (math.factorial(i) * math.factorial(n - i))))
# 		# print(arr)
# 	return arr
#
# digit = int(input())
# # print(pascal(digit))
# for i in range(digit):
# 	print(*pascal(i))


# def packing_duplicates(text: str) -> list:
# 	d = []
# 	tmp = []
# 	for elt in text:
# 		if len(tmp) == 0:
# 			tmp.append(elt)
# 		else:
# 			if tmp[-1] == elt:
# 				tmp.append(elt)
# 			if tmp[-1] != elt:
# 				d.append(list(tmp))
# 				tmp.clear()
# 				tmp.append(elt)
# 	if len(tmp) != 0:
# 		d.append(list(tmp))
# 	return d
#
# string1 = str(input()).replace(' ','')
# print(packing_duplicates(string1))



# def chunked(word1: list, digit: int) -> list:
# 	main_list = []
# 	for _ in range(len(word1)):
# 		if len(word1) > 0:
# 			main_list.append(word1[:digit])
# 			word1 = word1[digit:]
# 	return main_list
#
# word = str(input()).split()
# numb = int(input())
# print(chunked(word, numb))


# def sub_list(input_list: list) -> list:
# 	output_list = [[]]
# 	additional_list = []
# 	for _ in range(len(input_list)):
# 		for __ in range(len(input_list)):
# 			additional_list = input_list[__:_ + __ + 1]
# 			if len(additional_list) == _ + 1:
# 				output_list.append(additional_list)
# 	return output_list
#
#
# text = str(input()).split()
# print(sub_list(text))



# n = 5
# matrix = [[0]*n for _ in range(n)]
#
# # for r in range(8):
# # 	for c in range(8):
# # 		print(matrix[r][c], end=' ')
# # 	print()
#
# for i in range(5):
# 	matrix[i][i] = 1
# 	matrix[i][5 - i - 1] = 2
#
# for r in range(5):
# 	for c in range(5):
# 		print(matrix[r][c], end=' ')
# 	print()


# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)



# rows = int(input())
# cols = int(input())
# matrix = []
#
# for r in range(rows):
# 	row = []
# 	for c in range(cols):
# 		row.append(input())
# 	matrix.append(row)
#
#
# for j in range(rows):
# 	for k in range(cols):
# 		print(matrix[j][k], end=' ')
# 	print()
#
# print()
#
# for k in range(cols):
# 	for j in range(rows):
# 		print(matrix[j][k], end=' ')
# 	print()



# matrix = [[int(input()) for _ in range(digital)] for elt in range(digital)]
# matrix = [list(map(int, input().split())) for _ in range(digital)]
# matrix = [[1, 2, 3, 4], [5, 6, 3, 15], [0, 2, 3, 1], [5, 2, 8, 5]]

# def matrix_trace(digital: int) -> int:
# 	'''
# 	След матрицы
#
# 	3 - int
# 	1 2 3 - string_1
# 	4 5 6 - string_2
# 	7 8 9 - string_3
#
# 	https://stepik.org/lesson/416754/step/10?unit=406262
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digital)]
# 	d = 0
# 	for r in range(digital):
# 		d += matrix[r][r]
# 	return d
#
# numb = int(input())
# print(matrix_trace(numb))
#
# def more_than_average(digital: int):
# 	'''
# 	Больше среднего
#
# 	4 - int
# 	1 2 3 4 - string_1
# 	5 6 3 15 - string_2
# 	0 2 3 1 - string_3
# 	5 2 8 5 - string_4
#
# 	https://stepik.org/lesson/416754/step/11?unit=406262
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digital)]
# 	for r in range(digital):
# 		d = 0
# 		count = 0
# 		for c in range(digital):
# 			d += matrix[r][c]
# 			l = d / len(matrix[r])
#
# 		for _ in range(digital):
# 			if matrix[r][_] > l:
# 				count += 1
# 		print(count)
#
# numb = int(input())
# more_than_average(numb)



# matrix = [[1, 4, 5],
# 		  [6, 7, 8],
# 		  [1, 7, 6]]

# matrix = [[-50, -10, -20],
# 		  [-19, -78, -70],
# 		  [-11, -12, -19]]

# matrix = [[1, 9, 5, 8],
# 		  [6, 7, 8, 6],
# 		  [1, 1, 6, 2],
# 		  [2, 7, 4, 6]]



# def maximum_in_area_1(digital: int) -> int:
# 	'''
# 	Максимальный в области 1
#
# 	1 - int
# 	1 4 5 - string_1
# 	6 7 8 - string_2
# 	1 1 6 - string_3
#
# 	https://stepik.org/lesson/416754/step/12?unit=406262
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digital)]
# 	maximum = -9999
# 	for j in range(digital):
# 		if matrix[j][j] > maximum:
# 			maximum = matrix[j][j]
#
# 	for w in range(digital):
# 		for e in range(digital):
# 			if w > e:
# 				if matrix[w][e] > maximum:
# 					maximum = matrix[w][e]
#
# 	return maximum
# numb = int(input())
# print(maximum_in_area_1(numb))


# def maximum_in_area_2(digital: int) -> int:
# 	'''
# 	Максимальный в области 2
#
# 	3 - int
# 	1 4 5 -string_1
# 	6 7 8 - string_2
# 	1 1 6 - string_3
#
# 	https://stepik.org/lesson/416754/step/13?unit=406262
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digital)]
# 	maximum = -9999
# 	for j in range(digital):
# 		if matrix[j][j] > maximum:
# 			maximum = matrix[j][j]
# 	for _ in range(digital):
# 		if matrix[_][digital - 1 - _] > maximum:
# 			maximum = matrix[_][digital - 1 - _]
#
# 	for w in range(digital):
# 		for e in range(digital):
# 			if w > e and w < digital - 1 - e:
# 				if matrix[w][e] > maximum:
# 					maximum = matrix[w][e]
# 			if w < e and w > digital - 1 - e:
# 				if matrix[w][e] > maximum:
# 					maximum = matrix[w][e]
# 	return maximum
#
#
# numb = int(input())
# print(maximum_in_area_2(numb))



# def sums_of_quarters(digital: int):
# 	'''
# 	Суммы четвертей
#
# 	4 - int
# 	1 2 3 4 - string
# 	5 6 7 8 - string
# 	3 4 5 6 - string
# 	1 2 3 4 - string
#
# 	https://stepik.org/lesson/416754/step/14?unit=406262
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digital)]
# 	top = 0
# 	right = 0
# 	down = 0
# 	left = 0
# 	for w in range(digital):
# 		for e in range(digital):
# 			if w > e and w < digital - 1 - e:
# 				left += matrix[w][e]
# 			if w < e and w > digital - 1 - e:
# 				right += matrix[w][e]
# 			if w < e and w < digital - 1 - e:
# 				top += matrix[w][e]
# 			if w > e and w > digital -1 - e:
# 				down += matrix[w][e]
# 	top_quartes = f"Верхняя четверть: {top}"
# 	right_quartes = f"Правая четверть: {right}"
# 	down_quartes = f"Нижняя четверть: {down}"
# 	left_quartes = f"Левая четверть: {left}"
# 	temp = [top_quartes, right_quartes, down_quartes, left_quartes]
# 	for elt in temp:
# 		print(elt)
#
# numb = int(input())
# sums_of_quarters(numb)


# def multiplication_table(rows: int, cols: int):
# 	'''
# 	Таблица умножения
#
# 	4 - rows
# 	6 - cols
#
# 	0 0 0 0 0 0
# 	0 1 2 3 4 5
# 	0 2 4 6 8 10
# 	0 3 6 9 12 15
#
# 	https://stepik.org/lesson/416755/step/1?unit=406263
# 	'''
# 	matrix = [[_ for _ in range(cols)] for elt in range(rows)]
# 	for j in range(rows):
# 		for k in range(cols):
# 			matrix[j][k] = j * k
# 			print(str(matrix[j][k]).ljust(3), end=' ')
# 		print()
#
# digital_1 = int(input())
# digital_2 = int(input())
# multiplication_table(digital_1, digital_2)


