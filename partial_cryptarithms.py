from determine_unique_digits import unique_digits
from generate_multiplication_problem import multiplication_problem
from generate_multiplication_cryptarithm_problem_container import multiplication_cryptarithm_problem_container
from random import choice

difficulty_list = [0, 1, 2, 3, -1, 4, 5, 6, -1, -1, 7, 8, -1, -1, -1, 9]

def difficulty_to_digits(num):
	i = difficulty_list.index(num)
	digits = i % 4 + 1
	return digits

def difficulty_to_subs(num):
	i = difficulty_list.index(num)
	subs = int(i / 4) + 1
	return subs

difficulty = input("Set difficulty (0-9): ")
difficulty = int(difficulty)
digits = difficulty_to_digits(difficulty)
subs = difficulty_to_subs(difficulty)

problem = multiplication_problem(digits)
digits1 = unique_digits(problem.x)
digits2 = unique_digits(problem.y)

digits12 = digits1.union(digits2)

sub_dict = {}

if (subs >= len(digits12)):
	subs = len(digits12)

letters = {"a", "b", "c", "d"}

for sub in range(subs):
	sub_dict[digits12.pop()] = letters.pop()

str_problem_x = str(problem.x)
str_problem_y = str(problem.y)
str_problem_z = str(problem.z)

rep_str_problems = []

str_problems = [str_problem_x, str_problem_y, str_problem_z]
for str_problem in str_problems:
	for k, v in sub_dict.items():
		str_problem = str_problem.replace(k, v)
	rep_str_problems.append(str_problem)

partial_cryptarithm = multiplication_cryptarithm_problem_container(rep_str_problems[0],rep_str_problems[1],rep_str_problems[2], digits)

print()

for v in sub_dict.values():
	print(v + " = ?")
	
print()

print(partial_cryptarithm.f())
print(partial_cryptarithm.a())

print()

input("Press return to reveal answer: \n")

for k, v in sub_dict.items():
	print(v + " = " + k)
print()

print(problem.f())
print(problem.a())

print()
