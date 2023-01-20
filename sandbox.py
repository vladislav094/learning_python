## task 1
def task_1():
	count = [list(map(int, input().split())) for _ in range(int(input()))]
	for elt in range(len(count)):
		return(count[elt][0] + count[elt][1])
print(task_1())

## task 2
def task_2():
	for _ in range(int(input())):
		digit = int(input())  # This input don't use in function, but he was need for task by requirements for interpreter
		# arr = [int(input()) for _ in range(int(input()))]  		# You can use this option
		arr = list(map(int, input().split()))						# You also can use this option
		dict1 = {}
		for elt in arr:
			dict1[elt] = dict1.get(elt, 0) + 1
		count = 0
		for elt in range(len(dict1)):
			v = int(list(dict1.values())[elt])
			d = int(list(dict1.values())[elt]) // 3
			k = int(list(dict1.keys())[elt])
			count += (v - d) * k
		return count
print(task_2())
