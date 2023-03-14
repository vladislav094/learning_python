from datetime import datetime
arr_1 = [1, 2, 3, 4, 5, 1]
arr_2 = [1, [2, [3, [4, [5,[1, 1]]]]], 6,[[4, 1]], 1]

def my_recursion_for_sum(l: list):
	if len(l) == 0:
		return 0
	else:
		total = l[0] + my_recursion_for_sum(l[1:])
	return total
# print(my_recursion_for_sum(arr_1))


def my_recursion_for_all_inner_lists(l: list):
	total = 0
	for x in l:
		if not isinstance(x, list):
			total += x
		else:
			total += my_recursion_for_all_inner_lists(x)
	return total
# print(my_recursion_for_all_inner_lists(arr_2))


def outer(func):
	'''
	Decorator for calculating the time spent on the function
	:param func: self-made function
	:return: total spent time
	'''
	def inner(*args):
		start_time = datetime.now()
		_ = func(*args)
		stop_time = datetime.now()
		print(stop_time - start_time)
	return inner

@outer
def my_rec(func, arr: list):
	print(func(arr))
# my_rec(my_recursion_for_all_inner_lists, arr_2)


def check_recursion(l):
	total = 0
	arr = list(l)
	while arr:
		front = arr.pop(0)
		if not isinstance(front, list):
			total += front
		else:
			arr.extend(front)
	return total
# print(check_recursion(arr_2))


def my_recursion_find_count_of_number(l: list, digit: int):
	count = 0
	for x in l:
		if not isinstance(x, list):
			if x == digit:
				count += 1
		else:
			count += my_recursion_find_count_of_number(x, digit)
	return count
print(my_recursion_find_count_of_number(arr_2, 1))


def factorial(n):
	if n == 1:
		return 1
	return factorial(n-1) * n


def timer(func, *args):
	start = datetime.now()
	a = func(*args)
	print(a)
	stop = datetime.now()
	return stop - start

print(timer(factorial, 5))


print(factorial(5))