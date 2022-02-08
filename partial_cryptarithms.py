from determine_unique_digits import unique_digits
from generate_multiplication_problem import multiplication_problem
from generate_multiplication_cryptarithm_problem_container import multiplication_cryptarithm_problem_container
from random import choice


problem = multiplication_problem()
digits1 = unique_digits(problem.x)
digits2 = unique_digits(problem.y)

digits12 = digits1.union(digits2)

sub1 = digits12.pop()
sub2 = digits12.pop()

str_problem_x = str(problem.x)
str_problem_y = str(problem.y)
str_problem_z = str(problem.z)

rep_str_problems = []

str_problems = [str_problem_x, str_problem_y, str_problem_z]
for str_problem in str_problems:
	rep_string1 = str_problem.replace(sub1, "a")
	rep_string2 = rep_string1.replace(sub2, "b")
	rep_str_problems.append(rep_string2)

partial_cryptarithm = multiplication_cryptarithm_problem_container(rep_str_problems[0],rep_str_problems[1],rep_str_problems[2])

print("\nWhat are a and b?\n")

print(partial_cryptarithm.f())
print(partial_cryptarithm.a())

print()

input("Press return to reveal answer: \n")

print("a = " + str(sub1) + "\tb = " + str(sub2) + "\n")

print(problem.f())
print(problem.a())

print()
