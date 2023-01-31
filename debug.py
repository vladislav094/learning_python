a = 86397
b = 86399
print(b - a)
c = 53294
d = 86398
print(d - c)
if c >= a and c <= b or d >= a and d <= b:
	print('YES')
else:
	print('NO')

temp_test = []
for _ in range(int(input('Count input with times: '))):
	arr = (list(map(int, input().replace('-', ':').split(':'))))
	temp_test.append(arr)
for elt in range(len(temp_test)):
	temp = []
	sec_1 = int((arr[elt][0] * 60) + arr[elt][1]) * 60 + arr[elt][2]
	sec_2 = int((arr[elt][3] * 60) + arr[elt][4]) * 60 + arr[elt][5]
	temp = [sec_1, sec_2]

	dig_1 = (elt[0] * 60 + elt[1]) * 60 + elt[2]
	dig_2 = (elt[3] * 60 + elt[4]) * 60 + elt[5]
	t_range.append(temp)


print(temp_test)
arr_test = [[13, 45, 59, 19, 48, 11], [15, 57, 34, 17, 53, 40]]