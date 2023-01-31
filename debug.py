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
				print('YOU right')
			else:
				print('You don"t right')

print(temp_test)
print(t_range)
arr_test = [[13, 45, 59, 19, 48, 11], [15, 57, 34, 17, 53, 40]]