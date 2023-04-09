from abc import  ABCMeta, abstractmethod

class MixedNames:
	data = 'spam'
	def __init__(self, value):
		self.data = value

	def display(self):
		print(self.data, MixedNames.data)

x = MixedNames(1)
z = MixedNames(2)

x.display()
z.display()

class Super(metaclass=ABCMeta):
	def delegate(self):
		self.action()

	@abstractmethod
	def action(self):
		pass

class Sub(Super):
	def action(self):
		print('spam')
x = Sub()
x.delegate()




