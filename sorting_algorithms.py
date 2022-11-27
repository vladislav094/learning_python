a = [-2, 5, 0, 33, 71, 128, -9, 33]
l = len(a)
b = [-2, 5, 0, 33, 71, 128, -9, 33]
print(a)

# def bubble_sort(unsorted_list: list, len_list: int) -> list:
# 	for _ in range(len_list - 1):
# 		flag = True
# 		for j in range(len_list - 1):
# 			if unsorted_list[j] > unsorted_list[j+1]:
# 				unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
# 				flag = False
# 		if flag:
# 			break
# 	return unsorted_list
# print(bubble_sort(a, l))

# def inserts_sort(unsorted_list: list, len_list: int) -> list:
# 	for _ in range(len_list):
# 		d = unsorted_list[_]
# 		while _ > 0 and unsorted_list[_ - 1] > d:
# 			unsorted_list[_] = unsorted_list[_ - 1]
# 			_ -= 1
# 		unsorted_list[_] = d
# 	return unsorted_list
# print(inserts_sort(a, l))


# def select_sort(unsorted_list: list, len_list: int) -> list:
# 	for elt in range(len_list-1):
# 		dig = elt
# 		for j in range(elt + 1, len_list):
# 			if unsorted_list[j] < unsorted_list[dig]:
# 				dig = j
# 		unsorted_list[elt], a[dig] = a[dig], unsorted_list[elt]
# 	return unsorted_list
# print(select_sort(a, l))