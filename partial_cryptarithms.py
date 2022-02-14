from determine_unique_digits import unique_digits
from generate_multiplication_problem import multiplication_problem
from generate_multiplication_cryptarithm_problem_container import multiplication_cryptarithm_problem_container
from str_is_digit_input import str_is_digit

difficulty_list = [0, 1, 2, 3, -1, 4, 5, 6, -1, -1, 7, 8, -1, -1, -1, 9]

def difficulty_to_digits(num):
	i = difficulty_list.index(num)
	digits = i % 4 + 1
	return digits

def difficulty_to_subs(num):
	i = difficulty_list.index(num)
	subs = int(i / 4) + 1
	return subs

def make_partial_cryptarithm(difficulty):

	difficulty = int(difficulty)
	digits = difficulty_to_digits(difficulty)
	subs = difficulty_to_subs(difficulty)

	partial_cryptarithm_container = multiplication_cryptarithm_problem_container(None, None, None, digits, None)
	digits1 = unique_digits(partial_cryptarithm_container.x)
	digits2 = unique_digits(partial_cryptarithm_container.y)

	digits12 = digits1.union(digits2)

	sub_dict = {}

	if (subs >= len(digits12)):
		subs = len(digits12)

	letters = {"a", "b", "c", "d"}

	for sub in range(subs):
		sub_dict[digits12.pop()] = letters.pop()

	str_problem_x = str(partial_cryptarithm_container.x)
	str_problem_y = str(partial_cryptarithm_container.y)
	str_problem_z = str(partial_cryptarithm_container.z)

	rep_str_problems = []

	str_problems = [str_problem_x, str_problem_y, str_problem_z]
	for str_problem in str_problems:
		for k, v in sub_dict.items():
			str_problem = str_problem.replace(k, v)
		rep_str_problems.append(str_problem)

	partial_cryptarithm_container.a = rep_str_problems[0]
	partial_cryptarithm_container.b = rep_str_problems[1]
	partial_cryptarithm_container.c = rep_str_problems[2]
	partial_cryptarithm_container.sub_dict = sub_dict

	return partial_cryptarithm_container

replay = True
while(replay):

	notset = True
	while notset:
		difficulty = input("Set difficulty (0-9): ")
		if(difficulty == 'q'):
			break
		if(str_is_digit(difficulty) == True):
			notset = False
		else:
			print("Type only a digit 0-9.")
	if(difficulty == 'q'):
		break

	partial_cryptarithm = make_partial_cryptarithm(difficulty)

	print()

	for v in partial_cryptarithm.sub_dict.values():
		print(v + " = ?")
		
	print()

	print(partial_cryptarithm.question_t())
	print(partial_cryptarithm.answer_t())

	print()

	if(input("Press return to reveal answer: \n") == 'q'):
		break

	for k, v in partial_cryptarithm.sub_dict.items():
		print(v + " = " + k)
	print()

	print(partial_cryptarithm.question())
	print(partial_cryptarithm.answer())

	print()

	if(input("Press q to quit or any key to replay: ") == 'q'):
		replay = False
