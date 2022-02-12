from random import randint

class multiplication_problem():

	def __init__(self, size):
		self.size = size
		lower = pow(10, self.size - 1)
		upper = pow(10, self.size) - 1
		self.x = randint(lower, upper)
		self.y = randint(lower, upper)
		self.z = self.x * self.y

	def f(self):
		return "   " + '{:>3}'.format(self.x) + "\nX  " + '{:>3}'.format(self.y)

	def a(self):
		return '{:>6}'.format(self.z)

if __name__ == '__main__':
	problem = multiplication_problem(3)
	print(problem.f())
	print(problem.a())

	problem = multiplication_problem(2)
	print(problem.f())
	print(problem.a())
