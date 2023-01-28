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


# s1 = '02:46:00-03:14:59'
# s1 = s1.replace('-', ':')
# print(s1.split(':'))
# print(b[0][1])
# temp = []
# for elt in range(1):
# 	a = (list(map(int, input().replace('-', ':').split(':'))))
# 	temp.append(a)
# for _ in temp:
# 	print(_, end='\n')

####    1
# temp_test = [[2, 46, 0, 3, 14, 59]]
#

####    2
# temp_test = [[23, 59, 59, 23, 59, 59],
# 			[0, 0, 0, 23, 59, 58]]
#
####    3
# temp_test = [[23, 59, 58, 23, 59, 59],
# 			   [0, 0, 0, 23, 59, 58]]
#
###    4
# temp_test = [[23, 59, 59, 23, 59, 58],
# 			 [0, 0, 0, 23, 59, 57]]
#
###    5
# temp_test = [[17, 53, 39, 20, 20, 2],
# 	[10, 39, 17, 11, 0, 52],
# 	[8, 42, 47, 9, 2, 14],
# 	[9, 44, 26, 10, 21, 41],
# 	[0, 46, 17, 2, 7, 19],
# 	[22, 42, 50, 23, 17, 46]]
#

####    6
# temp_test = [[24, 0, 0, 23, 59, 59]]
# flag = bool
# first_less_second = bool
# valid_numbers = True
# for elt in range(len(temp_test)):
# 	# print(temp_test[elt])
# 	# first_less_second = bool
# 	# valid_numbers = bool
# 	if temp_test[0][0] > 23 or temp_test[0][3] > 23 or temp_test[0][1] > 59 or temp_test[0][4] > 59 or temp_test[0][2] > 59 or temp_test[0][5] > 59:
# 		valid_numbers = False
# 		flag = False
# 		break
# 	# print(valid_numbers)
# 	if valid_numbers == True:
# 		for elt in temp_test:
# 			if elt[0] > elt[3]:
# 				first_less_second = False
# 				break
# 			if elt[0] == elt[3] and elt[1] > elt[4]:
# 				first_less_second = False
# 				# break
# 			if elt[0] == elt[3] and elt[1] == elt[4] and elt[2] > elt[5]:
# 				first_less_second = False
# 				break
# 	else:
# 		# print('NO')
# 		flag = False
# 		break
# 	# print('first_less_second:', first_less_second, ';', 'valid_numbers:', valid_numbers)
#
# 	if first_less_second == False:
# 		# print('NO')
# 		flag = False
# 		break
# 	else:
#
# 		h1 = list(range(temp_test[0][0], temp_test[0][3]+1))
# 		if len(h1) == 0:
# 			h1 = [temp_test[0][0]]
# 		m1 = list(range(temp_test[0][1], temp_test[0][4]))
# 		if len(m1) == 0:
# 			m1 = [temp_test[0][1]]
# 		s1 = list(range(temp_test[0][2], temp_test[0][5]+1))
# 		if len(s1) == 0:
# 			s1 = [temp_test[0][2]]
# 		# flag = bool
# 		# for elt in temp_test:
# 		# 	print(elt, end='\n')
# 		# print('hours: ', h1)
# 		# print('min: ', m1)
# 		# print('sec: ', s1)
# 		answer = ''
# 		if len(temp_test) > 1:
# 			for elt in range(1,len(temp_test)):
# 				# print(temp_test[elt])
# 				if temp_test[elt][0] in h1:
# 					if temp_test[elt][0] > h1[0]:
# 						flag = False
# 						break
# 					if temp_test[elt][0] == h1[0]:
# 						if temp_test[elt][1] in m1:
# 							if temp_test[elt][1] > m1[0]:
# 								flag = False
# 								break
# 							if temp_test[elt][1] == m1[0]:
# 								if temp_test[elt][2] in s1:
# 									flag = False
# 									break
#
# 				if temp_test[elt][3] in h1:
# 					if temp_test[elt][3] > h1[0]:
# 						flag = False
# 						break
# 					if temp_test[elt][3] == h1[0]:
# 						if temp_test[elt][4] in m1:
# 							if temp_test[elt][4] > m1[0]:
# 								flag = False
# 								break
# 							if temp_test[elt][4] == m1[0]:
# 								if temp_test[elt][5] in s1:
# 									flag = False
# 									break
#
# 		else:
# 			for elt in range(1, len(temp_test)):
# 				print(temp_test[elt])
# 				if temp_test[elt][0] in h1:
# 					if temp_test[elt][0] > h1[0]:
# 						flag = False
# 						break
# 					if temp_test[elt][0] == h1[0]:
# 						if temp_test[elt][1] in m1:
# 							if temp_test[elt][1] > m1[0]:
# 								flag = False
# 								break
# 							if temp_test[elt][1] == m1[0]:
# 								if temp_test[elt][2] in s1:
# 									flag = False
# 									break
#
# 				if temp_test[elt][3] in h1:
# 					if temp_test[elt][3] > h1[0]:
# 						flag = False
# 						break
# 					if temp_test[elt][3] == h1[0]:
# 						if temp_test[elt][4] in m1:
# 							if temp_test[elt][4] > m1[0]:
# 								flag = False
# 								break
# 							if temp_test[elt][4] == m1[0]:
# 								if temp_test[elt][5] in s1:
# 									flag = False
# 									break
#
# if first_less_second == False or valid_numbers == False:
# 	print('NO')
# else:
# 	if flag:
# 		answer = 'YESs'
# 	else:
# 		answer = 'NOs'
# 	print(answer)


count_iteration = int(input('Count interations: '))
for elt in range(count_iteration):
	# temp = []
	count_times = int(input('Count times: '))
	answer = ''
	count = 0
	for elt in range(count_times):
		temp_test = []
		temp = (list(map(int, input().replace('-', ':').split(':'))))
		temp_test.append(temp)
		# print(temp, temp_test)
		flag = bool
		first_less_second = bool
		valid_numbers = True
		for elt in range(len(temp_test)):
			# print(temp_test[elt])
			# first_less_second = bool
			# valid_numbers = bool
			if temp_test[0][0] > 23 or temp_test[0][3] > 23 or temp_test[0][1] > 59 or temp_test[0][4] > 59 or temp_test[0][
				2] > 59 or temp_test[0][5] > 59:
				valid_numbers = False
				flag = False
				count += 1
				# break
			# print(valid_numbers)
			if valid_numbers == True:
				for elt in temp_test:
					if elt[0] > elt[3]:
						first_less_second = False
						# break
						count += 1
					if elt[0] == elt[3] and elt[1] > elt[4]:
						first_less_second = False
						# break
						count +=1
					if elt[0] == elt[3] and elt[1] == elt[4] and elt[2] > elt[5]:
						first_less_second = False
						# break
						count += 1

			else:
				# print('NO')
				flag = False
				count += 1
				# break
			# print('first_less_second:', first_less_second, ';', 'valid_numbers:', valid_numbers)

			if first_less_second == False:
				# print('NO')
				flag = False
				count += 1
				# break

			h1 = list(range(temp_test[0][0], temp_test[0][3] + 1))
			if len(h1) == 0:
				h1 = [temp_test[0][0]]
			m1 = list(range(temp_test[0][1], temp_test[0][4] +1))
			if len(m1) == 0:
				m1 = [temp_test[0][1]]
			s1 = list(range(temp_test[0][2], temp_test[0][5] + 1))
			if len(s1) == 0:
				s1 = [temp_test[0][2]]

			# answer = ''
			if len(temp_test) > 1:
				print('1')
				for elt in range(1, len(temp_test)):
					print(temp_test[elt])
					if temp_test[elt][0] in h1 and temp_test[elt][0] > h1[0]:
						flag = False
						count += 1
						# break
					if temp_test[elt][0] == h1[0] and temp_test[elt][1] in m1 and temp_test[elt][1] > m1[0]:
						flag = False
						count += 1
						# break
					if temp_test[elt][1] == m1[0] and temp_test[elt][2] in s1:
						flag = False
						count +=1
						# break

					if temp_test[elt][3] in h1 and temp_test[elt][3] > h1[0]:
						flag = False
						count +=1
						# break
					if temp_test[elt][3] == h1[0] and temp_test[elt][4] in m1 and temp_test[elt][4] > m1[0]:
						flag = False
						count +=1
						# break
					if temp_test[elt][4] == m1[0] and temp_test[elt][5] in s1:
						flag = False
						count += 1
						# break

			else:
				for elt in range(len(temp_test)):
					print(temp_test[elt])
					if temp_test[elt][0] in h1:
						if temp_test[elt][0] > h1[0]:
							flag = False
							count +=1
							# break
						if temp_test[elt][0] == h1[0] and temp_test[elt][1] in m1:
							if temp_test[elt][1] > m1[0]:
								flag = False
								count +=1
								# break
						if temp_test[elt][1] == m1[0] and temp_test[elt][2] in s1:
							flag = False
							count +=1
							# break

					if temp_test[elt][3] in h1:
						if temp_test[elt][3] > h1[0]:
							flag = False
							count +=1
							# break
						if temp_test[elt][3] == h1[0] and temp_test[elt][4] in m1:
							if temp_test[elt][4] > m1[0]:
								flag = False
								count +=1
								# break
							if temp_test[elt][4] == m1[0] and temp_test[elt][5] in s1:
								flag = False
								count +=1
								# break
		print(temp_test)
		if first_less_second == False or valid_numbers == False:
			# print('NO')
			answer = 'NO'
			count += 1
			# break
		else:
			if flag:
				answer = 'YESs'
			else:
				answer = 'NOs'
	if count == 0:
		print('YES')
	else:
		print('NO')
	# print(answer)