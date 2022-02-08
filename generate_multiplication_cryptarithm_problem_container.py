class multiplication_cryptarithm_problem_container():

	def __init__(self, crypt_x, crypt_y, crypt_z):
		self.x = crypt_x
		self.y = crypt_y
		self.z = crypt_z

	def f(self):
		return "   " + '{:>3}'.format(self.x) + "\nX  " + '{:>3}'.format(self.y)

	def a(self):
		return '{:>6}'.format(self.z)

if __name__ == '__main__':
	#Example 10 * 11 = 110; a = 0, b = 1
	string1 = "ab"
	string2 = "bb"
	string3 = "bba"
	container = multiplication_cryptarithm_problem_container(string1, string2, string3)
	print(container.f())
	print(container.a())