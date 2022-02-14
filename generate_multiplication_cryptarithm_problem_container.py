from generate_multiplication_problem import multiplication_problem

class multiplication_cryptarithm_problem_container(multiplication_problem):

	def __init__(self, crypt_a, crypt_b, crypt_c, size, sub_dict):
		self.a = crypt_a
		self.b = crypt_b
		self.c = crypt_c
		self.sub_dict = {}
		super().__init__(size)

	def question_t(self):
		if(self.size <= 2):
			return "  " + '{:>2}'.format(self.a) + "\nX " + '{:>2}'.format(self.b)
		elif(self.size == 3):
			return "   " + '{:>3}'.format(self.a) + "\nX  " + '{:>3}'.format(self.b)
		else:
			return "    " + '{:>4}'.format(self.a) + "\nX   " + '{:>4}'.format(self.b)

	def answer_t(self):
		if(self.size <= 2):
			return '{:>4}'.format(self.c)
		elif(self.size == 3):
			return '{:>6}'.format(self.c)
		else:
			return '{:>8}'.format(self.c)

if __name__ == '__main__':
	#Example 10 * 11 = 110; a = 0, b = 1
	string1 = "ab"
	string2 = "bb"
	string3 = "bba"
	container = multiplication_cryptarithm_problem_container(string1, string2, string3, 2, None)
	print(container.question_t())
	print(container.answer_t())

	string4 = "aba"
	string5 = "bab"
	string6 = "ababab"
	container2 = multiplication_cryptarithm_problem_container(string4, string5, string6, 3, None)
	print(container2.question_t())
	print(container2.answer_t())

	string7 = "abab"
	string8 = "baba"
	string9 = "abababab"
	container3 = multiplication_cryptarithm_problem_container(string7, string8, string9, 4, None)
	print(container3.question_t())
	print(container3.answer_t())

	string10 = "a"
	string11 = "b"
	string12 = "ab"
	container4 = multiplication_cryptarithm_problem_container(string10, string11, string12, 1, None)
	print(container4.question_t())
	print(container4.answer_t())
