def count_digits(num):
	if num < 10:
		return num
	else:
		return (num%10)+count_digits(num//10)

count_digits(346)
