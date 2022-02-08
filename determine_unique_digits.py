from random import randint

def unique_digits(x):
	x_digit_list = set(str(x))
	return x_digit_list

if __name__ == '__main__':
	x = randint(100,999)
	print(unique_digits(x))
