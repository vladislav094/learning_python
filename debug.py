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


# temp_test = [[23, 59, 57, 23, 59, 59], [14, 48, 14, 23, 59, 58]]
# my_arr = [[[86397, 86399], [53294, 86398]]]
# temp_test = [[18, 12, 49, 18, 22, 0], [10, 4, 37, 10, 15, 21], [22, 18, 53, 22, 39, 39], [16, 29, 56, 16, 31, 34], [14, 18, 22, 14, 28, 15], [11, 30, 57, 11, 57, 13], [2, 42, 35, 2, 48, 36], [3, 38, 22, 4, 21, 26], [16, 7, 27, 16, 26, 43], [7, 58, 10, 8, 0, 21], [0, 33, 25, 0, 35, 36], [1, 18, 27, 2, 32, 19], [18, 22, 19, 18, 40, 13], [6, 21, 43, 6, 59, 50], [7, 12, 36, 7, 14, 43], [1, 10, 54, 1, 16, 5], [5, 57, 44, 6, 20, 29], [4, 55, 2, 5, 2, 36], [17, 45, 1, 18, 6, 50], [23, 20, 45, 23, 57, 49], [5, 11, 24, 5, 11, 24], [21, 30, 47, 21, 42, 10], [14, 38, 54, 14, 40, 59], [13, 48, 1, 13, 48, 1], [11, 14, 32, 23, 43, 48], [8, 4, 16, 8, 16, 6], [19, 11, 13, 19, 22, 34], [11, 24, 23, 11, 26, 42], [17, 0, 18, 17, 7, 22], [13, 41, 4, 13, 41, 16], [12, 22, 21, 12, 51, 26], [22, 49, 40, 23, 10, 15], [4, 29, 27, 4, 46, 34], [14, 42, 36, 14, 42, 50], [14, 52, 57, 15, 49, 8], [20, 49, 8, 21, 25, 8], [9, 12, 28, 9, 16, 7], [10, 49, 23, 11, 22, 40], [18, 45, 41, 18, 59, 4], [0, 17, 48, 0, 22, 34]]

t_range = []
temp_test = []
for _ in range(int(input('Count input with times: '))):
	arr = (list(map(int, input().replace('-', ':').split(':'))))
	temp_test.append(arr)
for elt in temp_test:
	dig_1 = (elt[0] * 60 + elt[1]) * 60 + elt[2]
	dig_2 = (elt[3] * 60 + elt[4]) * 60 + elt[5]
	if dig_2 >= dig_1:
		arr_1 = [dig_1, dig_2]
		t_range.append(arr_1)

for elt in reversed(range(len(t_range))):
	for j in range(len(t_range)):
		if elt != j:
			if t_range[elt][0] >= t_range[j][0] and t_range[elt][0] <= t_range[j][1] or t_range[elt][1] >= t_range[j][0] and t_range[elt][1] <= t_range[j][1]:
				print(j, t_range[elt][0], temp_test[elt], temp_test[j])
				print('YOU right')
			else:
				print('You don"t right')

# print(temp_test)
print(t_range)
arr_test = [[13, 45, 59, 19, 48, 11], [15, 57, 34, 17, 53, 40]]