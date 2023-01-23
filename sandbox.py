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
# 			k = int(list(dict1.keys())[elt])
# 			count += (v - d) * k
# 		return count
# print(task_2())


# digit1 = int(input())
# digit2 = int(input())
# arr = [list(map(int, input().split())) for _ in range(2)]
# arr = []
# for elt in range(3):
# 	d = int(input())
# 	arr.append(list(map(int, input().split())))
# 	print(d)
# print(arr)
# arr1 = [[123, 1, 123133, 44, 123, 55], [1231, 123, 99, 0], [5, 5]]
# arr1 = [[2, 1, 3, 1, 1, 4], [5, 5], [1, 4, 2, 5, 4, 2, 6, 3]]
# for elt in range(len(arr1)):
# 	for jey in range(len(arr1[elt])):
# 		if jey % 2 == 0:
# 			print(arr1[elt][jey], arr1[elt][jey+1])
# 	print()

# a = [2, 1, 3, 1, 1, 4]
position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
a = [[2, 1, 3, 1, 1, 4], [5, 5], [1, 4, 2, 5, 4, 2, 6, 3]]
tempt = []
small_temp = []
arr = []
for e in a:
	# d = int(input())
	# 	arr.append(list(map(int, input().split())))
	for i in range(len(e)):
		# print(e)
		d_1 = e[i]
		for j in range(i+1,len(e)):
			d_2 = e[j]
			# print(d_1, d_2)
			print(position[i], position[j])
			if position[i] in small_temp or position[j] in small_temp:
				continue
			if abs(d_1 - d_2) == 1 or abs(d_1 - d_2) == 0:
				# print(position[i], position[j])
				small_temp.append(position[i])
				small_temp.append(position[j])
		if len(small_temp) != 0 and small_temp not in tempt:
			tempt.append(small_temp)
		# print(small_temp)
	# print(tempt)
	small_temp = []

# for i in range(len(a)):
# 	d_1 = a[i]
# 	for j in range(i+1,len(a)):
# 		d_2 = a[j]
# 		if position[i] in small_temp or position[j] in small_temp:
# 			continue
# 		if abs(d_1 - d_2) == 1 or abs(d_1 - d_2) == 0:
# 			small_temp.append(position[i])
# 			small_temp.append(position[j])
# 	if len(small_temp) != 0 and small_temp not in tempt:
# 		tempt.append(small_temp)
#
# 	# if len(tempt[i]) == len(arr[i]) and i+1 == len(arr[i]):
# 	# 	for key in range(len(arr)):
# 	# 		for jey in range(len(arr[key])):
# 	# 			if jey % 2 == 0:
# 	# 				print(arr1[key][jey], arr1[key][jey + 1])
# 	# 		print()

print(tempt)
# print(small_temp,tempt)




