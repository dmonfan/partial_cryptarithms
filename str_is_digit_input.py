'''Test if String is a Digit'''
def str_is_digit(x):
	'''Throw out non-digit length strings'''
	if len(x) > 1:
		return False

	#Check if number and change type
	try:
		x = int(x)

	except ValueError:
		return False

	#Redundant code as a number that is length 1 is a digit
	if(0 <= x and x < 10):
		return True

	return False

#string, non-digit, float, integer, digit, symbol
test_list = ["a","10","1.1","-1","4", "+"]

for test in test_list:
	print(str_is_digit(test))

print("\n")

test_range = []

for x in range(10):
	test_range.append(str(x))

for test in test_range:
	print(str_is_digit(test))