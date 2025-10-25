def factorial(num):
	if num == 0:
		return 1
	elif num == 1:
		return 1
	elif num > 1:
		total = 1
		set_num = num
		while set_num > 0:
			total *= set_num
			set_num -= 1
	return total


print(factorial(45))
