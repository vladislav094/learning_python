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

