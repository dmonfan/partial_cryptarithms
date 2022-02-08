from random import randint

class multiplication_problem:

	def __init__(self):
		self.x = randint(100,999)
		self.y = randint(100,999)
		self.z = self.x * self.y

	def f(self):
		return "   " + '{:>3}'.format(self.x) + "\nX  " + '{:>3}'.format(self.y)

	def a(self):
		return '{:>6}'.format(self.z)

if __name__ == '__main__':
	problem = multiplication_problem()
	print(problem.f())
	print(problem.a())
