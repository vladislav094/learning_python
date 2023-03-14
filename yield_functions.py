def gensquares(n):
	for i in range(n):
		yield i ** 2

c = (i**2 for i in range(1, 6))
print(dir(c))


def f1():
	for i in [43, 55, 53]:
		yield i

s = f1()
print(next(s))
print(next(s))
print(next(s))


def factor(x):
	fr = 1
	for i in range(1, x+1):
		fr *= i
		yield fr

a = '12345'
b = map(int, a)
print(list(b))


def yie(x):
	for i in range(x):
		yield i
		yield i*2

print(list(yie(7)))


def permute(seq):
	if not seq:
		return [seq]
	else:
		res = []
		for i in range(len(seq)):
			rest = seq[:i] + seq[i+1:]
			for x in permute(rest):
				res.append(seq[i:i+1] + x)
		return res

l = [1, 2, 3, 4, 5]
print(permute(l))


def my_map_with_yield(func, sequence):
	return (func(elt) for elt in sequence)

l = '12345'
b = my_map_with_yield(str, l)
print(list(b))