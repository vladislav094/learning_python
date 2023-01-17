def general_figures(arr_set: list) -> list:
	"""
	:param arr_set:
	arr_set = [{'2', '4', '5', '1', '3'}, {'2', '3', '6'}, {'2', '4', '3', '5'}, {'0', '2', '3', '9'}]
	:return:
	2 3
	https://stepik.org/lesson/482377/step/16?unit=473680
	"""
	base_set = {'8', '9', '0', '4', '7', '6', '2', '5', '3', '1'}
	for elt in range(len(arr_set)):
		base_set.intersection_update(arr_set[elt])
	base_set = sorted(base_set)
	return base_set

# arr_of_set = [set(input()) for _ in range(int(input()))]
# print(*general_figures(arr_of_set))


def number_first_line(arr_of_str: list) -> list:
	"""
	:param arr_of_str:
	1 2 3 4 5
	1 2 3 4 6
	:return:
	5
	https://stepik.org/lesson/482377/step/15?unit=473680
	"""
	for elt in range(len(arr_of_str)):
		for _ in range(len(arr_of_str[elt])):
			arr_of_str[elt][_] = int(arr_of_str[elt][_])
	myset_1 = set(arr_of_str[0])
	myset_2 = set(arr_of_str[1])
	myset_3 = sorted(myset_1.difference(myset_2))
	return myset_3

# arr_of_str_with_number = [str(input()).split() for _ in range(2)]
# print(*number_first_line(arr_of_str_with_number))


def computer_science_lesson(digit_1: set, digit_2: set, digit_3: set) -> list:
	"""
	:param digit_1: 1 5 4 2 5 6 6 2 3 3 5 2
	:param digit_2: 2 3 5 1 2 1 2 6 7 1 1 6
	:param digit_3: 1 4 6 9 8 7 0 9 0 9 8 10
	:return: 5 3 2
	https://stepik.org/lesson/483114/step/10?unit=474427
	"""
	myset_1 = digit_1.intersection(digit_2)
	myset_2 = sorted(myset_1.difference(digit_3), reverse=True, key=int)
	return myset_2
