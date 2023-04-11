# a = 86397
# b = 86399
# print(b - a)
# c = 53294
# d = 86398
# print(d - c)
# if c >= a and c <= b or d >= a and d <= b:
# 	print('YES')
# else:
# 	print('NO')


#
# t_range = []
# temp_test = []
# for _ in range(int(input('Count input with times: '))):
# 	arr = (list(map(int, input().replace('-', ':').split(':'))))
# 	temp_test.append(arr)
# for elt in temp_test:
# 	dig_1 = (elt[0] * 60 + elt[1]) * 60 + elt[2]
# 	dig_2 = (elt[3] * 60 + elt[4]) * 60 + elt[5]
# 	if dig_2 >= dig_1:
# 		arr_1 = [dig_1, dig_2]
# 		t_range.append(arr_1)
# flag = bool
# for elt in reversed(range(len(t_range))):
# 	elt_range = list(range(t_range[elt][0], t_range[elt][1]+1))
# 	for jey in range(len(t_range)):
# 		jey_range = list(range(t_range[jey][0], t_range[jey][1]+1))
# 		if elt != jey:
# 			for key in elt_range:
# 				if key in jey_range:
# 					print('NO')
# 					print(elt, jey, key, t_range[elt], t_range[jey])
# 					flag = False
# 					break
# 			if flag == False:
# 				break
# 		if flag == False:
# 			break
# 	if flag == False:
# 		break
			# if t_range[elt][0] >= t_range[j][0] and t_range[elt][0] <= t_range[j][1] or t_range[elt][1] >= t_range[j][0] and t_range[elt][1] <= t_range[j][1]:
			# 	print(j, t_range[elt][0], temp_test[elt], temp_test[j])
			# 	print('YOU right')
			# else:
			# 	print('You don"t right')
# print(temp_test)
# for i in temp_test:
# 	print(i)
# # print(t_range)
# for e in t_range:
# 	print(e)


# for _ in range(int(input())):
# 	flag_1 = True
# 	valid_numbers = True
# 	first_less_second = True
# 	t_range = []
# 	temp_test = []
# 	for _ in range(int(input())):
# 		arr = (list(map(int, input().replace('-', ':').split(':'))))
# 		temp_test.append(arr)
#
# 	for elt in range(len(temp_test)):
# 		if temp_test[elt][0] > 23 or temp_test[elt][3] > 23 or temp_test[elt][1] > 59 or temp_test[elt][4] > 59 or \
# 				temp_test[elt][2] > 59 or temp_test[elt][5] > 59:
# 			valid_numbers = False
# 			flag_1 = False
# 			break
# 	if valid_numbers == True:
# 		for elt in temp_test:
# 			dig_1 = (elt[0] * 60 + elt[1]) * 60 + elt[2]
# 			dig_2 = (elt[3] * 60 + elt[4]) * 60 + elt[5]
# 			if dig_2 >= dig_1:
# 				arr_1 = [dig_1, dig_2]
# 				t_range.append(arr_1)
# 			else:
# 				flag_1 = False
# 				first_less_second = False
# 				break
# 	else:
# 		flag_1 = False
#
# 	for elt in reversed(range(len(t_range))):
# 		elt_range = list(range(t_range[elt][0], t_range[elt][1] + 1))
# 		for jey in range(len(t_range)):
# 			jey_range = list(range(t_range[jey][0], t_range[jey][1] + 1))
# 			if elt != jey:
# 				for key in elt_range:
# 					if key in jey_range:
# 						print('NO')
# 						print(elt, jey, key, t_range[elt], t_range[jey])
# 						flag = False
# 						break
# 				if flag == False:
# 					break
# 			if flag == False:
# 				break
# 		if flag == False:
# 			break
#
# 	if flag_1:
# 		print('YES')
# 	else:
# 		print('NO')



def get(x):
	for i in range(x):
		yield i ** 2

a = get(6)
print(list(a))
