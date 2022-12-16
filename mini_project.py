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


# def maximum_in_the_table(rows_digital: int, cols_digital: int) -> str:
# 	'''
# 	Максимум в таблице
#
# 	3 - rows int
# 	4 - cols int
# 	0 3 2 4
# 	2 3 5 5
# 	5 1 2 3
#
# 	https://stepik.org/lesson/416755/step/2?unit=406263
# 	'''
# 	maximum = -999
# 	rows = 0
# 	cols = 0
# 	matrix = []
# 	for _ in range(rows_digital):
# 		tmp = [int(x) for x in input().split()]
# 		matrix.append(tmp)
#
# 	for e in range(rows_digital):
# 		for j in range(cols_digital):
# 			if matrix[e][j] > maximum:
# 				maximum = matrix[e][j]
# 				rows = e
# 				cols = j
#
# 	return str(rows) + ' ' + str(cols)
#
# digital_1 = int(input())
# digital_2 = int(input())
# print(maximum_in_the_table(digital_1, digital_2))


# def column_swapping(rows: int, cols: int) -> list:
# 	'''
# 	Обмен столбцов
# 	3 - rows int
# 	4 - cols int
# 	11 12 13 14
# 	21 22 23 24
# 	31 32 33 34
# 	https://stepik.org/lesson/416755/step/3?unit=406263
# 	'''
# 	matrix = []
# 	for _ in range(rows):
# 		tmp = [int(x) for x in input().split()]
# 		matrix.append(tmp)
# 	digital = str(input()).split()
#
# 	for k in range(rows):
# 		matrix[k][int(digital[0])], matrix[k][int(digital[1])] = matrix[k][int(digital[1])], matrix[k][int(digital[0])]
#
# 	for elt in matrix:
# 		print(*elt)
#
# digital_1 = int(input())
# digital_2 = int(input())
# column_swapping(digital_1, digital_2)



# def symmetric_matrix(digit: int) -> bool:
# 	'''
# 	Симметричная матрица
#
# 	3 - int
# 	0 1 2 - string
# 	1 2 3 - string
# 	2 3 4 - string
#
# 	https://stepik.org/lesson/416755/step/4?unit=406263
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digit)]
# 	flag = False
# 	for k in range(digit):
# 		for j in range(1,digit):
# 			if matrix[k][j] == matrix[j][k]:
# 				flag = True
# 			else:
# 				flag = False
# 				break
# 		if flag == False:
# 			break
# 	return flag
#
# numb = int(input())
# print(symmetric_matrix(numb))


# def exchange_of_diagonals(digit: int):
# 	'''
# 	Обмен диагоналей
#
# 	3 - int
# 	1 2 3 - string
# 	4 5 6 - string
# 	7 8 9 - string
#
# 	https://stepik.org/lesson/416755/step/5?unit=406263
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digit)]
# 	for k in range(digit):
# 		matrix[k][digit - 1 - k], matrix[digit - 1 - k][digit - 1 - k] = matrix[digit - 1 - k][digit - 1 - k], matrix[k][digit - 1 - k]
#
# 	for elt in range(digit):
# 		for j in range(digit):
# 			print(matrix[elt][j], end=' ')
# 		print()
#
# numb = int(input())
# exchange_of_diagonals(numb)


# matrix = [[1, 2, 3],
# 		  [4, 5, 6],
# 		  [7, 8, 9]]

# def rot90(digit):
# 	'''
# 	Поворот матрицы
#
# 	3 - int
# 	7 4 1 - string
# 	8 5 2 - string
# 	9 6 3 - string
#
# 	https://stepik.org/lesson/416755/step/7?unit=406263
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digit)]
# 	new_matrix = [list(reversed(col)) for col in zip(*matrix)]
# 	for elt in range(3):
# 		for j in range(3):
# 			print(new_matrix[elt][j], end=' ')
# 		print()
# 	# # 2
# 	# for elt in range(digit):
# 	# 	for j in range(digit - 1, -1, -1):
# 	# 		print(matrix[j][elt], end=' ')
# 	# 	print()
#
#
# digital = int(input())
# rot90(digital)

# def knights_moves():
# 	n = 8
# 	matrix = [[0] * n for _ in range(n)]
#
# 	x, y = input()
# 	x = ord(x) - 97
# 	y = int(n - int(y))
#
# 	matrix[y][x] = 'N'
#
# 	for i in range(n):
# 		for q in range(n):
# 			matrix[i][q] = '.'
# 			matrix[y][x] = 'N'
# 			if abs(i - y) * abs(q - x) == 2:
# 				matrix[i][q] = '*'
# 			print(matrix[i][q], end=' ')
# 		print()
#
# knights_moves()


# matrix = [[8, 1, 6],
# 		  [3, 5, 7],
# 		  [ 4, 9, 2]]
# matrix = [['.'] * 10 for _ in range(10)]
# digit = 10
# for j in range(digit):
# 	matrix[j][digit - 1 - j] = '2'
# 	matrix[j][j] = '1'
# for e in range(digit):
# 	for k in range(digit):
# 		print(matrix[e][k], end=' ')
# 	print()



# def magic_square(digit: int) -> str:
# 	'''
# 	Магический квадрат
# 	Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n,
# 	 составленная из всех чисел 1, 2, 3, \ldots, n^21,2,3,…,n 2
#     так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
#     Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.
#
#     3 - int
#     8 1 6 - string
#     3 5 7 - string
#     4 9 2 - string
#
# 	https://stepik.org/lesson/416755/step/9?unit=406263
# 	'''
# 	matrix = [list(map(int, input().split())) for _ in range(digit)]
# 	digital = [elt for elt in range(1, digit * digit + 1)]
# 	new_matrix = []
# 	total_arr = []
# 	for elt in range(digit):
# 		for jei in range(digit):
# 			new_matrix.extend([matrix[elt][jei]])
# 	new_matrix.sort()
# 	if new_matrix == digital:
# 		for e in range(digit):
# 			total_1 = 0
# 			for j in range(digit):
# 				total_1 += matrix[e][j]
# 			total_arr.append(total_1)
# 		total_1 = 0
#
# 		for j in range(digit):
# 			total_1 += matrix[j][digit - 1- j]
# 		total_arr.append(total_1)
#
# 		total_1 = 0
# 		for j in range(digit):
# 			total_1 += matrix[j][j]
# 		total_arr.append(total_1)
#
# 		for j in range(digit):
# 			total_1 = 0
# 			for k in range(digit):
# 				total_1 += matrix[k][j]
# 			total_arr.append(total_1)
# 		res = all(x == total_arr[0] for x in total_arr)
# 		if res:
# 			return 'YES'
# 		else:
# 			return 'NO'
# 	else:
# 		return 'NO'
# numb = int(input())
# print(magic_square(numb))


# def chess_board():
# 	'''
# 	Шахматная доска
#
# 	3 4 - input
#
# 	:return
# 	. * . *
# 	* . * .
# 	. * . *
#
# 	https://stepik.org/lesson/416757/step/1?unit=406265
# 	'''
# 	var_1, var_2 = input().split()
# 	var_1 = int(var_1)
# 	var_2 = int(var_2)
# 	matrix = [['.'] * var_2 for _ in range(var_1)]
# 	for elt in range(var_1):
# 		for jei in range(var_2):
# 			if elt % 2 == 0 and jei % 2 != 0:
# 				matrix[elt][jei] = '*'
# 			if elt % 2 != 0 and jei % 2 == 0:
# 				matrix[elt][jei] = '*'
# 			print(matrix[elt][jei], end=' ')
# 		print()
#
# chess_board()


# def side_diagonal(digit: int):
# 	'''
# 	Побочная диагональ
# 	4 - int
#
# 	:return
# 	0 0 0 1
# 	0 0 1 2
# 	0 1 2 2
# 	1 2 2 2
# 	https://stepik.org/lesson/416757/step/2?unit=406265
# 	'''
# 	matrix = [[0] * digit for _ in range(digit)]
# 	count = 0
# 	for elt in range(digit):
# 		for key in range(digit):
# 			matrix[digit - 1 - key][key] = '1'
# 			if elt < key and elt > digit - 1 - key or elt > key and elt > digit - 1 - key:
# 				matrix[elt][key] = '2'
# 			if count >= digit/2 and elt == key:
# 				matrix[elt][key] = '2'
# 			print(matrix[elt][key], end=' ')
# 		count += 1
# 		print()
#
# numb = int(input())
# side_diagonal(numb)

# def filling_in_1():
# 	'''
# 	Заполнение 1
#
# 	3 4 - input
#
# 	:return:
# 	1  2  3  4
# 	5  6  7  8
# 	9  10 11 12
# 	https://stepik.org/lesson/416757/step/3?unit=406265
# 	'''
# 	# var_1, var_2 = input().split()
# 	# var_1, var_2 = int(var_1), int(var_2)
# 	var_1, var_2 = 3, 4
# 	matrix = [[0] * var_2 for _ in range(var_1)]
#
# 	for elt in range(var_1):
# 		for key in range(var_2):
# 			matrix[elt][key] = elt * var_2 + key + 1
# 			print(str(matrix[elt][key]).ljust(3), end=' ')
# 		print()
#
# filling_in_1()


# def filling_in_2():
# 	'''
# 	Заполнение 2
#
# 	3 4 - input
#
# 	:return:
# 	1  2  3  4
# 	5  6  7  8
# 	9  10 11 12
# 	https://stepik.org/lesson/416757/step/3?unit=406265
# 	'''
# 	var_1, var_2 = input().split()
# 	var_1, var_2 = int(var_1), int(var_2)
# 	matrix = [[0] * var_2 for _ in range(var_1)]
#
# 	# count = 1
# 	for elt in range(var_1):
# 		for key in range(var_2):
# 			matrix[elt][key] = key * var_1 + elt + 1
# 			print(str(matrix[elt][key]).ljust(3), end=' ')
# 			# count += 1
# 		print()
#
# filling_in_2()

# def filling_in_5():
# 	'''
# 	Заполнение 5
# 	3 4 - input
# 	:return:
# 	1   2   3   4   5   6   7
# 	2   3   4   5   6   7   1
# 	3   4   5   6   7   1   2
# 	https://stepik.org/lesson/416757/step/7?unit=406265
# 	'''
# 	digit, digit_1 = input().split()
# 	digit = int(digit)
# 	digit_1 = int(digit_1)
# 	matrix = [[i for i in range(1, digit_1+1)]  for _ in range(digit)]
#
# 	for k in range(digit):
# 		for v in range(digit_1):
# 			matrix[k][v] = (k+v) % digit_1 + 1
# 			print(str(matrix[k][v]).ljust(3), end=' ')
# 		print()
#
# filling_in_5()

# def filling_with_snake():
# 	'''
# 	Заполнение змейкой
# 	3 5 - input
# 	:return:
# 	1  2  3  4  5
# 	10 9  8  7  6
# 	11 12 13 14 15
# 	https://stepik.org/lesson/416757/step/8?unit=406265
# 	'''
# 	digit, digit_1 = input().split()
# 	digit = int(digit)
# 	digit_1 = int(digit_1)
# 	matrix = [[i for i in range(1, digit_1+1)] for _ in range(digit)]
# 	temp = []
# 	for k in range(digit):
# 		for v in range(digit_1):
# 			matrix[k][v] = k * digit_1 + v + 1
# 		if k % 2 == 0:
# 			temp.append(matrix[k])
# 		else:
# 			t = list(reversed(matrix[k]))
# 			temp.append(t)
#
# 	for k in range(digit):
# 		for v in range(digit_1):
# 			print(str(temp[k][v]).ljust(3), end=' ')
# 		print()
# filling_with_snake()

# def filling_with_diagonals():
# 	'''
# 	Заполнение диагоналями
#
# 	3 5 - input
# 	:return:
# 	1  2  4  7  10
# 	3  5  8  11 13
# 	6  9  12 14 15
# 	https://stepik.org/lesson/416757/step/9?unit=406265
# 	'''
# 	digit, digit_1 = input().split()
# 	digit = int(digit)
# 	digit_1 = int(digit_1)
# 	matrix = [[i for i in range(1, digit_1 + 1)] for _ in range(digit)]
# 	nm = 0
# 	for j in range(digit * digit_1):
# 		for k in range(digit):
# 			for v in range(digit_1):
# 				if k + v == j:
# 					nm += 1
# 					matrix[k][v] = nm
#
# 	for k in range(digit):
# 		for v in range(digit_1):
# 			print(str(matrix[k][v]).ljust(3), end=' ')
# 		print()
#
# filling_with_diagonals()


# def filling_with_spiral():
# 	'''
# 	Заполнение спиралью
# 	4 5 - input
# 	:return:
# 	1  2  3  4  5
# 	14 15 16 17 6
# 	13 20 19 18 7
# 	12 11 10 9  8
# 	https://stepik.org/lesson/416757/step/10?unit=406265
# 	'''
# 	digit, digit_1 = input().split()
# 	digit = int(digit)
# 	digit_1 = int(digit_1)
# 	matrix = [[0] * digit_1 for _ in range(digit)]
# 	i = 1
# 	x = 0
# 	y = -1
# 	d_row = 0 # -1 0 1
# 	d_column = 1 # -1 0 1
#
# 	while i <= digit*digit_1:
# 		if 0 <= x + d_row < digit and 0<= y + d_column < digit_1 and matrix[x+d_row][y+d_column] == 0:
# 			x += d_row
# 			y += d_column
# 			matrix[x][y] = i
# 			i += 1
# 		else:
# 			if d_column == 1:
# 				d_column = 0
# 				d_row = 1
# 			elif d_row == 1:
# 				d_row = 0
# 				d_column = -1
# 			elif d_column == -1:
# 				d_column = 0
# 				d_row = -1
# 			elif d_row == -1:
# 				d_row = 0
# 				d_column =1
#
#
# 	for k in range(digit):
# 		for v in range(digit_1):
# 			print(str(matrix[k][v]).ljust(3), end=' ')
# 		print()
#
# filling_with_spiral()


# def matrix_addition(digit: int, digit_2: int):
# 	matrix = [list(map(int, input().split())) for _ in range(digit)]
# 	input()
# 	matrix_2 =[list(map(int, input().split())) for _ in range(digit)]
# 	matrix_3 = [[0]* digit_2 for _ in range(digit)]
#
# 	for elt in range(digit):
# 		for key in range(digit_2):
# 			matrix_3[elt][key] = matrix[elt][key] + matrix_2[elt][key]
# 			print(matrix_3[elt][key], end=' ')
# 		print()
#
# numb, numb_2 = input().split()
# numb, numb_2 = int(numb), int(numb_2)
# matrix_addition(numb, numb_2)



def matrix_multiplication(digit: int,digit_3: int):
	'''
	Умножение матриц
	:param digit: 3 2
	2 5
	6 7
	1 8

	:param digit_3: 2 3
	1 2 1
	0 1 0

	:return:
	2 9 2
	6 19 6
	1 10 1

	https://stepik.org/lesson/416756/step/10?unit=406264
	'''
	matrix_a = [list(map(int, input().split())) for _ in range(digit)]
	matrix_b = [list(map(int, input().split())) for _ in range(digit_3)]

	matrix_res = [[0] * digit for _ in range(digit)]

	for elt in range(len(matrix_a)):
		for key in range(len(matrix_b[0])):
			f = 0
			for jet in range(len(matrix_a[elt])):
				d = matrix_a[elt][jet] * matrix_b[jet][key]
				f += d
			matrix_res[elt][key] = f

	for elt in range(digit):
		for key in range(digit):
			print(matrix_res[elt][key], end=' ')
		print()

numb, numb_2 = input('numb 1 and 2: ').split()
numb, numb_2 = int(numb), int(numb_2)
numb_3, numb_4 = input('numb 3 and 3: ').split()
numb_3, numb_4 = int(numb_3), int(numb_4)
matrix_multiplication(numb, numb_3)
