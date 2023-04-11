class Employee:
	def __init__(self, name, salary=0):
		self.name = name
		self.salary = salary

	def give_raise(self, pecent):
		self.salary = self.salary + (self.salary * pecent)

	def work(self):
		print(self.name, 'does stuff')

	def __repr__(self):
		return f"<Employee: name={self.name}, salary={self.salary}>"


class Chef(Employee):
	def __init__(self, name):
		Employee.__init__(self, name, 50000)

	def work(self):
		print(self.name, 'makes food')

class Server(Employee):
	def __init__(self, name):
		Employee.__init__(self, name, 40000)

	def work(self):
		print(self.name, 'interfaces with customer')

class PizzaRobot(Chef):
	def __init__(self, name):
		Chef.__init__(self, name)

	def work(self):
		print(self.name, 'maes pizza')

class Customer:
	def __init__(self, name):
		self.name = name

	def order(self, server):
		print(self.name, 'orders from', server)

	def pay(self, server):
		print(self.name, 'pay for item to', server)

class Oven:
	def bake(self):
		print('oven bakes')

class PizzaShop:
	def __init__(self):
		self.server = Server('Pat')
		self.chef = PizzaRobot('Bob')
		self.oven = Oven()

	def order(self, name):
		customer = Customer(name)
		customer.order(self.server)
		self.chef.work()
		self.oven.bake()
		customer.pay(self.server)

scene = PizzaShop()
scene.order('Homer')
print('...')
scene.order('Shaggy')