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

arr_of_set = [set(input()) for _ in range(int(input()))]
print(*general_figures(arr_of_set))




