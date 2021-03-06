from random import randint

class multiplication_problem():

	def __init__(self, size):
		self.size = size
		lower = pow(10, self.size - 1)
		upper = pow(10, self.size) - 1
		self.x = randint(lower, upper)
		self.y = randint(lower, upper)
		self.z = self.x * self.y

	def question(self):
		if(self.size <= 2):
			return "  " + '{:>2}'.format(self.x) + "\nX " + '{:>2}'.format(self.y)
		elif(self.size == 3):
			return "   " + '{:>3}'.format(self.x) + "\nX  " + '{:>3}'.format(self.y)
		else:
			return "    " + '{:>4}'.format(self.x) + "\nX   " + '{:>4}'.format(self.y)

	def answer(self):
		if(self.size <= 2):
			return '{:>4}'.format(self.z)
		elif(self.size == 3):
			return '{:>6}'.format(self.z)
		else:
			return '{:>8}'.format(self.z)

if __name__ == '__main__':
	problem = multiplication_problem(3)
	print(problem.question())
	print(problem.answer())

	problem = multiplication_problem(2)
	print(problem.question())
	print(problem.answer())

	problem = multiplication_problem(4)
	print(problem.question())
	print(problem.answer())
