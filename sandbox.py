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


# e = [1, 4, 2, 5, 4, 2, 6, 3]
# aa = [2, 1, 3, 1, 1, 4]

tempt = []
small_temp = []
arr = []
position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = [[2, 1, 3, 1, 1, 4], [5, 5], [1, 4, 2, 5, 4, 2, 6, 3]]
digit1 = int(input())
for e in range(digit1):
	digit2 = int(input())
	b = (list(map(int, input().split())))
	a = b.copy()
	for i in range(len(a)):
		d_1 = a[i]
		for j in range(i+1,len(a)):
			d_2 = a[j]
			if position[i] in small_temp or position[j] in small_temp:
				continue
			if abs(d_1 - d_2) == 0:
				small_temp.append(position[i])
				small_temp.append(position[j])
				del_1 = a[i]
				del_2 = a[j]
				if del_1 in b and del_2 in b:
					b.remove(del_1)
					b.remove(del_2)
			if len(small_temp) == 2 and small_temp not in tempt:
				tempt.append(small_temp)
		for j in range(i+1,len(a)):
			d_2 = a[j]
			if position[i] in small_temp or position[j] in small_temp:
				continue
			if abs(d_1 - d_2) == 1:
				small_temp.append(position[i])
				small_temp.append(position[j])
				del_1 = a[i]
				del_2 = a[j]
				if del_1 in b and del_2 in b:
					b.remove(del_1)
					b.remove(del_2)
			if len(small_temp) == 2 and small_temp not in tempt:
				tempt.append(small_temp)
		for j in range(i+1, len(a)):
			d_2 = a[j]
			if position[i] in small_temp or position[j] in small_temp:
				continue
			if abs(d_1 - d_2) >1:
				small_temp.append(position[i])
				small_temp.append(position[j])
				del_1 = a[i]
				del_2 = a[j]
				if del_1 in b and del_2 in b:
					b.remove(del_1)
					b.remove(del_2)
			if len(small_temp) == 2 and small_temp not in tempt:
				tempt.append(small_temp)
	small_temp = []
	for elt in tempt:
		for jey in range(len(elt)):
			if jey % 2 == 0:
				print(elt[jey], elt[jey+1])
		print()
	tempt = []
