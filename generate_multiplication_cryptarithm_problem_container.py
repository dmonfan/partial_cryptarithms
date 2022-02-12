class multiplication_cryptarithm_problem_container():

	def __init__(self, crypt_x, crypt_y, crypt_z, size):
		self.size = size
		self.x = crypt_x
		self.y = crypt_y
		self.z = crypt_z

	def f(self):
		if(self.size <= 2):
			return "  " + '{:>2}'.format(self.x) + "\nX " + '{:>2}'.format(self.y)
		elif(self.size == 3):
			return "   " + '{:>3}'.format(self.x) + "\nX  " + '{:>3}'.format(self.y)
		else:
			return "    " + '{:>4}'.format(self.x) + "\nX   " + '{:>4}'.format(self.y)

	def a(self):
		if(self.size <= 2):
			return '{:>4}'.format(self.z)
		elif(self.size == 3):
			return '{:>6}'.format(self.z)
		else:
			return '{:>8}'.format(self.z)

if __name__ == '__main__':
	#Example 10 * 11 = 110; a = 0, b = 1
	string1 = "ab"
	string2 = "bb"
	string3 = "bba"
	container = multiplication_cryptarithm_problem_container(string1, string2, string3, 2)
	print(container.f())
	print(container.a())

	string4 = "aba"
	string5 = "bab"
	string6 = "ababab"
	container2 = multiplication_cryptarithm_problem_container(string4, string5, string6, 3)
	print(container2.f())
	print(container2.a())

	string7 = "abab"
	string8 = "baba"
	string9 = "abababab"
	container3 = multiplication_cryptarithm_problem_container(string7, string8, string9, 4)
	print(container3.f())
	print(container3.a())
