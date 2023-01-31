## task 1
# def task_1():
# 	count = [list(map(int, input().split())) for _ in range(int(input()))]
# 	for elt in range(len(count)):
# 		return(count[elt][0] + count[elt][1])
# print(task_1())

## task 2
# def task_2():
# 	for _ in range(int(input())):
# 		digit = int(input())  # This input don't use in function, but he was need for task by requirements for interpreter
# 		# arr = [int(input()) for _ in range(int(input()))]  		# You can use this option
# 		arr = list(map(int, input().split()))						# You also can use this option
# 		dict1 = {}
# 		for elt in arr:
# 			dict1[elt] = dict1.get(elt, 0) + 1
# 		count = 0
# 		for elt in range(len(dict1)):
# 			v = int(list(dict1.values())[elt])
# 			d = int(list(dict1.values())[elt]) // 3
# 			first_less_second = int(list(dict1.keys())[elt])
# 			count += (v - d) * first_less_second
# 		return count
# print(task_2())


## task 2
# def task_3()-> None:
# 	# """
# 	# a = [[2, 1, 3, 1, 1, 4], [5, 5], [1, 4, 2, 5, 4, 2, 6, 3]]
# 	# position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, + ...]
# 	# :return: [[1, 2, 3, 6, 4, 5], [1, 2], [1, 3, 2, 5, 4, 7, 6, 8]]
# 	# """
# 	tempt = []
# 	small_temp = []
# 	position = list(range(1,1001))
# 	digit1 = int(input('Count iteration: '))
# 	for _ in range(digit1):
# 		digit2 = int(input('Count numbers in string: '))
# 		b = (list(map(int, input('Numbers: ').split())))
# 		a = b.copy()
# 		for i in range(len(a)):
# 			d_1 = a[i]
# 			w = 0
# 			while w != 100:
# 				for j in range(i+1,len(a)):
# 					d_2 = a[j]
# 					if position[i] in small_temp or position[j] in small_temp:
# 						continue
# 					if abs(d_1 - d_2) == w:
# 						small_temp.append(position[i])
# 						small_temp.append(position[j])
# 						del_1 = a[i]
# 						del_2 = a[j]
# 						if del_1 in b and del_2 in b:
# 							b.remove(del_1)
# 							b.remove(del_2)
# 					if len(small_temp) == 2 and small_temp not in tempt:
# 						tempt.append(small_temp)
# 				w += 1
# 		small_temp = []
# 	for elt in tempt:
# 		for jey in range(len(elt)):
# 			if jey % 2 == 0:
# 				print(elt[jey], elt[jey+1])
# 		print()
# 	tempt = []

# task_3()

## task 4
# def task_4():
#     """
#     count_iteration = int (3 for example)
#     count_int = list: [4, 3] ([0] number of columns; [1] number of rows)
#     arr_input = [[3, 4, 1],
#                     [2, 2, 5],
#                     [2, 4, 2],
#                     [2, 2, 1]]
#
#     count_position = 3 (len of list position)
#     position = list: [2, 1, 3] (position to filter columns with number)
#     :return: [[3, 4, 1],
#               [2, 2, 5],
#               [2, 4, 2],
#               [2, 2, 1]]
#     all flow of sorting: [
#                            [3, 4, 1], [2, 2, 5], [2, 2, 5], [2, 2, 1],
#                            [2, 2, 5], [2, 2, 1], [2, 2, 1], [3, 4, 1],
#                            [2, 4, 2], [3, 4, 1], [2, 4, 2], [2, 4, 2],
#                            [2, 2, 1], [2, 4, 2], [3, 4, 1], [2, 2, 5]
#                         ]
#     """
#     count_iteration = int(input('Count iteration: '))
#     for _ in range(count_iteration):
#         empty_input = str(input('Empty input: '))
#         count_int = (list(map(int, input('Numbers: ').split())))
#         arr_input = [[int(x) for x in input('Lists of numbers: ').split()] for _ in range(count_int[0])]
#         count_position = int(input('Count position: '))
#         position = (list(map(int, input('List with position: ').split())))
#         for elt in position:
#             temp = []
#             result = {}
#             p = elt
#             for elt in range(len(arr_input)):
#                 temp.append(arr_input[elt][p-1])
#
#             for elt in range(len(temp)):
#                 result[elt] = temp[elt]
#
#             t = []
#             for first_less_second, v in result.items():
#                 tup = (first_less_second, v)
#                 t.append(tup)
#
#             for elt in range(len(t)):
#                 t[elt] = t[elt][::-1]
#             t = sorted(t)
#
#             b = []
#             for elt in range(len(t)):
#                 b.append(t[elt][1])
#
#             new_arr = []
#             for elt in range(len(arr_input)):
#                 indx = b[elt]
#                 new_arr.append(arr_input[indx])
#             arr_input = new_arr
#
#         for elt in arr_input:
#             print(*elt)
#         print()


## task 5

# arr = [1, 2, 3, 4, 5]
# arr = [1, 2, 3, 1]
# arr = [2, 3, 4, 8, 5, 5, 5, 5]
# arr = [1, 1, 3, 2, 2]
# arr = [1, 1, 2, 3, 2]
# arr = [1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]
# arr = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# arr = [5, 5, 5, 5, 5, 5, 6]
# arr = [8, 10, 10, 4, 1, 5, 7, 2, 1, 3]

# def task_5():
# 	flag = bool
# 	d1 = 0
# 	d2 = 1
# 	count_iteration = int(input())
# 	for _ in range(count_iteration):
# 		temp = []
# 		count_numbers = int(input())
# 		arr = (list(map(int, input().split())))
# 		while len(arr) > 2:
# 			if arr[d1] == arr[d2]:
# 				del arr[d1]
# 			if arr[d1] != arr[d2]:
# 				temp.append(arr[d1])
# 				del arr[d1]
#
# 		if len(arr) == 1:
# 			temp.append(arr[0])
# 		elif len(arr) == 2 and arr[0] == arr[1]:
# 			temp.append(arr[0])
# 		else:
# 			temp.extend(arr)
#
# 		for elt in temp:
# 			if temp.count(elt) > 1:
# 				flag = 'NO'
# 				break
# 			else:
# 				flag = 'YES'
# 		print(flag)
# task_5()


# temp_test = [[18, 12, 49, 18, 22, 0],
# 			[10, 4, 37, 10, 15, 21],
# 			[22, 18, 53, 22, 39, 39],
# 			[16, 29, 56, 16, 31, 34],
# 			[14, 18, 22, 14, 28, 15],
# 			[11, 30, 57, 11, 57, 13],
# 			[2, 42, 35, 2, 48, 36],
# 			[3, 38, 22, 4, 21, 26],
# 			[16, 7, 27, 16, 26, 43],
# 			[7, 58, 10, 8, 0, 21],
# 			[0, 33, 25, 0, 35, 36],
# 			[1, 18, 27, 2, 32, 19],
# 			[18, 22, 19, 18, 40, 13],
# 			[6, 21, 43, 6, 59, 50],
# 			[7, 12, 36, 7, 14, 43],
# 			[1, 10, 54, 1, 16, 5],
# 			[5, 57, 44, 6, 20, 29],
# 			[4, 55, 2, 5, 2, 36],
# 			[17, 45, 1, 18, 6, 50],
# 			[23, 20, 45, 23, 57, 49],
# 			[5, 11, 24, 5, 11, 24],
# 			[21, 30, 47, 21, 42, 10],
# 			[14, 38, 54, 14, 40, 59],
# 			[13, 48, 1, 13, 48, 1],
# 			[11, 14, 32, 23, 43, 48],
# 			[8, 4, 16, 8, 16, 6],
# 			[19, 11, 13, 19, 22, 34],
# 			[11, 24, 23, 11, 26, 42],
# 			[17, 0, 18, 17, 7, 22],
# 			[13, 41, 4, 13, 41, 16],
# 			[12, 22, 21, 12, 51, 26],
# 			[22, 49, 40, 23, 10, 15],
# 			[4, 29, 27, 4, 46, 34],
# 			[14, 42, 36, 14, 42, 50],
# 			[14, 52, 57, 15, 49, 8],
# 			[20, 49, 8, 21, 25, 8],
# 			[9, 12, 28, 9, 16, 7],
# 			[10, 49, 23, 11, 22, 40],
# 			[18, 45, 41, 18, 59, 4],
# 			[0, 17, 48, 0, 22, 34]]


####    1
arr = [[2, 46, 0, 3, 14, 59]]
#

####    2
# arr = [[23, 59, 59, 23, 59, 59],
# 			[0, 0, 0, 23, 59, 58]]
#
####    3
# arr = [[23, 59, 58, 23, 59, 59],
# 			   [0, 0, 0, 23, 59, 58]]
#
###    4
arr = [[23, 59, 59, 23, 59, 58],
			 [0, 0, 0, 23, 59, 57]]
#
###    5
# arr = [[17, 53, 39, 18, 20, 2],
# 	[10, 39, 17, 11, 0, 52],
# 	[8, 42, 47, 9, 2, 14],
# 	[9, 44, 26, 10, 21, 41],
# 	[0, 46, 17, 2, 7, 19],
# 	[22, 42, 50, 23, 17, 46]]
# #

####    6
# arr = [[24, 0, 0, 23, 59, 59]]



for _ in range(int(input('Count iterations: '))):
	flag_1 = True
	valid_numbers = True
	first_less_second = True
	t_range = []
	temp_test = []
	for _ in range(int(input('Count input with times: '))):
		arr = (list(map(int, input().replace('-', ':').split(':'))))
		temp_test.append(arr)

	for elt in range(len(temp_test)):
		if temp_test[elt][0] > 23 or temp_test[elt][3] > 23 or temp_test[elt][1] > 59 or temp_test[elt][4] > 59 or temp_test[elt][2] > 59 or temp_test[elt][5] > 59:
			valid_numbers = False
			flag_1 = False
			break

	if valid_numbers == True:
		for elt in temp_test:
			dig_1 = (elt[0] * 60 + elt[1]) * 60 + elt[2]
			dig_2 = (elt[3] * 60 + elt[4]) * 60 + elt[5]
			if dig_2 >= dig_1:
				arr_1 = [dig_1, dig_2]
				t_range.append(arr_1)
			else:
				flag_1 = False
				first_less_second = False
				break                                               
	else:
		flag_1 = False


	for elt in reversed(range(len(t_range))):
		for j in range(len(t_range)):
			if elt != j:
				if t_range[elt][0] >= t_range[j][0] and t_range[elt][0] <= t_range[j][1] or t_range[elt][1] >= t_range[j][0] and t_range[elt][1] <= t_range[j][1]:
					flag_1 = False
					break
				else:
					flag_1 = True
		if flag_1 == False:
			break

	if flag_1:
		print('YES')
	else:
		print('NO')



