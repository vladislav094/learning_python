import random



ticket = int(input())

result = []
for _ in range(ticket):
	result.append(random.randint(1, 49))
for _ in sorted(result):
	print(_)