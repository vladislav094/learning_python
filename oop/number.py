
# class Number:
# 	def __init__(self, sequence):
# 		self.sequence = sequence
# 		self._index = 0
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		if self._index < len(self.sequence):
# 			item = self.sequence[self._index]
# 			self._index += 1
# 			return item
# 		else:
# 			raise StopIteration
#
# a = Number([1, 2, 3, 4, 5])
# for item in a:
# 	print(item)

class Car:
	model = 'bmw'
	engine = 1.6

	def drive(self):
		print('Lets')

c = Car()
c.drive()