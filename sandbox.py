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
# def task_5():
#     count_iteration = int(input())
#     for _ in range(count_iteration):
#         count_numbers = int(input())
#         temp = (list(map(int, input().split())))
#         count_no = 0
#         my_set = set()
#         first = 0
#         second = 1
#         for _ in range(len(temp)-1):
#             if temp[first] == temp[second]:
#                 second += 1
#             else:
#                 if temp[second] in my_set:
#                     count_no += 1
#                 my_set.add(temp[first])
#                 first, second = second, second + 1
#         if count_no == 0:
#             print('YES')
#         else:
#             print('NO')
# task_5()

### task 6
# def task_6():
# 	"""
# 	1 input - count iteration
# 	2 input - count times
# 	3 input (list) - times
# 	17:53:39-20:20:02
# 	10:39:17-11:00:52
# 	08:42:47-09:02:14
# 	09:44:26-10:21:41
# 	00:46:17-02:07:19
# 	22:42:50-23:17:46
# 	:return:
# 	YES
# 	"""
# 	for _ in range(int(input())):
# 		flag_1 = True
# 		valid_numbers = True
# 		t_range = []
# 		temp_test = []
# 		for _ in range(int(input())):
# 			arr = (list(map(int, input().replace('-', ':').split(':'))))
# 			temp_test.append(arr)
#
# 		for elt in range(len(temp_test)):
# 			if temp_test[elt][0] > 23 or temp_test[elt][3] > 23 or temp_test[elt][1] > 59 or temp_test[elt][4] > 59 or \
# 					temp_test[elt][2] > 59 or temp_test[elt][5] > 59:
# 				valid_numbers = False
# 				flag_1 = False
# 				break
# 		if valid_numbers == True:
# 			for elt in temp_test:
# 				dig_1 = (elt[0] * 60 + elt[1]) * 60 + elt[2]
# 				dig_2 = (elt[3] * 60 + elt[4]) * 60 + elt[5]
# 				if dig_2 >= dig_1:
# 					arr_1 = [dig_1, dig_2]
# 					t_range.append(arr_1)
# 				else:
# 					flag_1 = False
# 					break
#
# 		t_range = sorted(t_range)
#
# 		for lst in range(len(t_range) - 1):
# 			if t_range[lst][1] >= t_range[lst + 1][0]:
# 				flag_1 = False
# 				break
# 		if flag_1:
# 			print('YES')
# 		else:
# 			print('NO')
# task_6()


general_arr = []
# test_arr = [['R.R.R.G'], ['.Y.G.G.'], ['B.Y.V.V']]
# test_arr = [['R', 'R', 'R', 'G'], ['', 'Y', 'G', 'G', ''], ['B', 'Y', 'V', 'V']]
# for _ in range(4):
# 	# arr = [str(x) for x in input().split('.')]
# 	arr = [ord(x) for x in input() if x != '.']
# 	general_arr.append(arr)
# print(general_arr)

valid_test_arr_ascii = [[82, 82, 82, 71],
						[89, 71, 71],
						[66, 89, 86, 86]]

invalid_test_arr_ascii = [[89, 82, 66, 66],
						  [82, 82, 66, 86],
						  [66, 82, 66, 82],
						  [66, 66, 82, 82]]

for lst in valid_test_arr_ascii:
	print(lst, end='\n')
print()
for lst in valid_test_arr_ascii:
	# x = set(lst)
	print(set(lst))
