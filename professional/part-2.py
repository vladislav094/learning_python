#1
# def new_course(a: int, b: int, c: int)-> int:
# 	min_value = a + b + c
# 	if (a * 2) + (b * 2) < min_value:
# 		min_value = (a * 2) + (b * 2)
# 	if (b * 2) + (c * 2) < min_value:
# 		min_value = (b * 2) + (c * 2)
# 	if (a * 2) + (c * 2) < min_value:
# 		min_value = (a * 2) + (c * 2)
# 	return min_value
#
# print(new_course(100, 33, 34))
# print(new_course(789, 101112, 131415))
# print(new_course(27485716, 99999999, 35182))


#2
# def similar_letter(a: str, b: str, c: str)-> str:
# 	input_data = [x.lower() for x in (a, b, c)]
# 	eng_letters = list(range(97, 123))
# 	counter = 0
# 	for elt in input_data:
# 		if ord(elt) in eng_letters:
# 			counter += 1
# 	if counter == 3:
# 		return 'en'
# 	if counter == 0:
# 		return 'ru'
# 	else:
# 		return 'mix'
#
# print(similar_letter('Р', 'О', 's'))


#3
def revers(a, b, c, d, e):
	...


#4
# def more_that_one(seq: str)-> str:
# 	arr_seq = [int(x) for x in seq.split()]
# 	result = set(x for x in arr_seq if arr_seq.count(x) > 1)
# 	my_arr = []
# 	for _ in result:
# 		my_arr.append(str(_))
# 	my_arr.sort(key=int)
# 	return ' '.join(my_arr)
#
# print(more_that_one('3 1 3 2 3 11 4 3 5 3 6 3 7 3 8 3 9 3 10 3 11 3 3 12 13 1'))


#5
# def max_len_of_group(number: int) -> int:
# 	my_arr = [str(x) for x in range(1, number + 1)]
# 	my_dict = dict.fromkeys(list(range(1, int(my_arr[-1]))), [])
# 	result = []
# 	for elt in range(len(my_arr)):
# 		a = ' '.join(my_arr[elt])
# 		a = sum([int(x) for x in a.split()])
# 		result.append(a)
# 	for k, v in my_dict.items():
# 		my_dict[k] = result.count(k)
# 	a = max(my_dict.values())
# 	return a
#
# print(max_len_of_group(1337))

#6
# a = [['испанский', 'португальский', 'эсперанто', 'французский'],
# 	 ['французский', 'испанский', 'эсперанто'],
# 	 ['португальский', 'эсперанто', 'французский', 'испанский'],
# 	 ['французский', 'английский', 'болгарский', 'испанский', 'эсперанто'],
# 	 ['эсперанто', 'английский', 'русский', 'испанский', 'французский'],
# 	 ['python', 'испанский', 'эсперанто', 'латышский', 'польский', 'французский']]

a = [input().split(', ') for _ in range(int(input()))]
result_dict = {}
result_list = []

for elt in a:
	for _ in elt:
		result_dict.setdefault(_, 0)

for k, v in result_dict.items():
	for elt in a:
		result_dict[k] += elt.count(k)

for k, v in result_dict.items():
	if v == len(a):
		result_list.append(k)
result_list.sort()

if len(result_list):
	print(', '.join(result_list))

else:
	print('Сериал снять не удастся')




