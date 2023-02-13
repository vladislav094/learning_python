def matrix(n=1, m=4, value=0):
	arr = []
	if n == 1:
		return [[0]]
	else:
		arr = [[value for _ in range(m)] for _ in range(n)]
		return arr


print(matrix(3, 4, 9))

