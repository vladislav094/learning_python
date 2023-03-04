from functools import reduce
#1
# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f"""To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!"""
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))


#2
# def pretty_print(*data, side='-', delimiter='|'):
# 	s2 = delimiter + " " + f' {delimiter} '.join(map(str, *data)) + " " + delimiter
# 	s = " " + (len(s2) - 2) * side + " "
# 	print(s)
# 	print(s2)
# 	print(s)
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

#3
# def concat(*args, sep=' '):
# 	return list(map(lambda x: sep.join(map(str, args)), args))[0]
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

#4
# def product_of_odds(data):
# 	result = list(filter(lambda x: x % 2 == 1, data))
# 	result = reduce(lambda x,y: x*y, result, 1)
#
# 	# return reduce(lambda x, y: x * y, filter(lambda x: x % 2, data), 1)  # another example of solution
# 	return result
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(product_of_odds(arr))

#5
# words = 'the world is mine take a look what you have started'.split()
# print(*list(map(lambda x: '"'+ x + '"', words)))

#6
# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*list(filter(lambda x: str(x) != str(x)[::-1], numbers)))


#7
# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
# sorted_numbers = sorted(numbers, key=lambda x:sum(x) / len(x), reverse=True)
# print(sorted_numbers)

#8
# def mul7(x):
#     return x * 7
#
# def add2(x, y):
#     return x + y
#
# def add3(x, y, z):
#     return x + y + z
#
# def call(func, *value):
#     return func(*value)
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))


#9
# def add3(x):
#     return x + 3
#
# def mul7(x):
#     return x * 7
#
# def compose(func_1, func_2):
#     return lambda x: func_1(func_2(x))
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))

