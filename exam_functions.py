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
def product_of_odds(data):
	result = list(filter(lambda x: x % 2 == 1, data))
	result = reduce(lambda x,y: x*y, result, 1)
	return result
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(product_of_odds(arr))