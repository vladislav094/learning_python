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
# arr = [list(map(int, input().split())) for _ in range(3)]
a = [2, 1, 3, 1, 1, 4]
position = [1, 2, 3, 4, 5, 6]
# arr1 = [[2, 1, 3, 1, 1, 4], [5, 5], [1, 4, 2, 5, 4, 2, 6, 3]]

tempt = []
small_temp = []
# for i in range(len(arr)):
# 	d_1 = arr[i]
# 	for j in range(i+1,len(arr)):
# 		d_2 = arr[j]
# 		if position[i] in small_temp or position[j] in small_temp:
# 			continue
# 		if abs(d_1 - d_2) == 1 or abs(d_1 - d_2) == 0:
# 			small_temp.append(position[i])
# 			small_temp.append(position[j])
# 			# if len(tempt) == 0:
# 			# 	tempt.append(small_temp)
# 			# else:
# 			# 	continue
# for elt in range(int(digit2/2)):
# 	print(small_temp[elt], small_temp[elt+1], end='\n')


for i in range(len(a)):
	d_1 = a[i]
	for j in range(i+1,len(a)):
		d_2 = a[j]
		if position[i] in small_temp or position[j] in small_temp:
			continue
		if abs(d_1 - d_2) == 1 or abs(d_1 - d_2) == 0:
			t1 = [position[i], position[j]]
			# small_temp.insert(i, t1)
			small_temp.append(position[i])
			small_temp.append(position[j])
			# if len(tempt) == 0:
			# 	tempt.append(small_temp)
			# else:
			# 	continue
	# print(small_temp)
	if len(small_temp) != 0:
		tempt.append(small_temp)
	small_temp = []
print(tempt)
# print(small_temp,tempt)




