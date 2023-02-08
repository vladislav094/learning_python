import random
import string


# ticket = int(input())
#
# result = []
# for _ in range(ticket):
# 	result.append(random.randint(1, 49))
# for _ in sorted(result):
# 	print(_)

# def generate_ip():
# 	ip = str(random.randint(100, 255)) + '.' + str(random.randint(100, 255)) + '.' + str(random.randint(1,9)) + '.' + str(random.randint(100, 255))
# 	return ip
#
# print(generate_ip())


# def generate_index():
# 	s1 = [x for x in random.sample(string.ascii_uppercase, 2)]
# 	s2 = [x for x in random.sample(string.digits, 2)]
# 	s3 = [x for x in random.sample(string.ascii_uppercase, 2)]
# 	number = s1 + s2 + ['_'] + s2 + s3
# 	return ''.join(number)
#
# print(generate_index())


# def shuffle():
# 	matrix = [[1, 2, 3, 4],
# 			  [5, 6, 7, 8],
# 			  [9, 10, 11, 12],
# 			  [13, 14, 15, 16]]
# 	random.shuffle(matrix)
# 	return  matrix
#
# print(shuffle())


# def ticket():
# 	arr = []
# 	while len(arr) < 100:
# 		arr.append(random.sample(string.digits[1:], 7))
# 	for elt in arr:
# 		print(''.join(elt))
# ticket()

# def anagramms():
# 	word = ' '.join(str(input())).split(' ')
# 	random.shuffle(word)
# 	word = str(''.join(word))
# 	print(word, type(word))
# anagramms()

a = [x for x in range(1, 76)]
print(a)
b = random.sample(a, 25)
b[13] = 0
print(b)
for elt in range(5):
	print(b[elt])
# arr = []
# while len(arr) < 5:
# 	tmp = []
# 	while len(tmp) < 5:
# 		rnd_dig = random.randint(1, 75)
# 		if rnd_dig not in tmp:
# 			tmp.append(rnd_dig)
# 	arr.append(tmp)
# arr[2][2] = 0
# for _ in range(len(arr)):
# 	d = arr[_]
# 	print(*d)