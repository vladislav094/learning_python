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
def max_len_of_group(number: int) -> int:
	my_arr = [str(x) for x in range(1, number + 1)]
	result = []
	was = []
	for elt in range(len(my_arr)):
		temp = []
		a = ' '.join(my_arr[elt])
		a = sum([int(x) for x in a.split()])
		temp.append(my_arr[elt])
		if int(my_arr[elt]) < 10:
			for jey in range(elt + 1, len(my_arr)):
				b = ' '.join(my_arr[jey])
				b = sum([int(x) for x in b.split()])
				if a == b:
					temp.append(my_arr[jey])
			result.append(temp)
	for _ in result:
		for j in _:
			was.append(j)
	for item in my_arr:
		if item not in was:
			t = [item]
			result.append(t)
	x = max([len(x) for x in result])
	return x

print(max_len_of_group(20))
print(max_len_of_group(1337))
