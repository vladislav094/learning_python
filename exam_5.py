# https://stepik.org/lesson/416759/?unit=406267
# 1
# text = input().split()
# d = int(input())
# matrix = [[] for _ in range(d)]
# for elt in range(d):
# 	matrix.append(text[elt::d])
#
# print(matrix[d:])

# 2
# d = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(d)]
# total = 0
#
# for elt in range(d):
# 	if total < matrix[elt][d - 1 -elt]:
# 		total = matrix[elt][d - 1 -elt]
# 	for key in range(d):
# 		if elt < key and elt > d - 1 - key or elt > key and elt > d - 1 - key:
# 			if total < matrix[elt][key]:
# 				total = matrix[elt][key]
# 	if elt >= d / 2:
# 		if total < matrix[elt][elt]:
# 			total = matrix[elt][elt]
# print(total)


# 3
# d = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(d)]
# for elt in range(d):
# 	for key in range(d):
# 		print(matrix[key][elt], end=' ')
# 	print()

# 4
# d = int(input())
# matrix = [['.'] * d for _ in range(d)]
# for elt in range(d):
# 	matrix[elt][elt] = '*'
# 	matrix[elt][d - 1 -elt] = '*'
# 	for key in range(d):
# 		if elt == d // 2:
# 			matrix[elt][key] = '*'
# 		if key == d // 2:
# 			matrix[elt][key] = '*'
# 		print(matrix[elt][key], end=' ')
# 	print()

# 5
# def symmetric_matrix(digit: int) -> str:
#     matrix = [list(map(int, input().split())) for _ in range(digit)]
#     matrix = matrix[::-1]
#     flag = ''
#     for first_less_second in range(digit):
#         for j in range(1,digit):
#             if matrix[first_less_second][j] == matrix[j][first_less_second]:
#                 flag = 'YES'
#             else:
#                 flag = 'NO'
#                 break
#         if flag == 'NO':
#             break
#     return flag
#
# numb = int(input())
# print(symmetric_matrix(numb))

#6
# d = int(input())
# matrix_1 = [[int(x) for x in input().split()] for _ in range(d)]
# matrix = [int(x) for x in range(1, d+1)]
# flag = False
#
# for elt in range(d):
#     if sorted(matrix_1[elt]) == matrix:
#         flag = True
#     else:
#         flag = False
#         break
#     temp = []
#     for key in range(d):
#         temp.append(matrix_1[key][elt])
#     if sorted(temp) == matrix:
#         flag = True
#     else:
#         flag = False
#         break
#
# if flag:
#     print('YES')
# else:
#     print('NO')

# 7
# n = 8
# matrix = [['.'] * n for _ in range(n)]
# x, y = input()
# x = ord(x) - 97
# y = int(n - int(y))
# matrix[y][x] = 'Q'
# for elt in range(n):
# 	for key in range(n):
# 		if abs(elt - y) == abs(key - x) or elt == y or key == x:
# 			matrix[elt][key] = '*'
# 		matrix[y][x] = 'Q'
# 		print(matrix[elt][key], end=' ')
# 	print()


#8
d = int(input())
matrix = [[0] * d for _ in range(d)]
print(matrix)
for elt in range(d):
	for key in range(d):
		matrix[elt][key] = abs(elt - key)
		print(matrix[elt][key], end=' ')
	print()