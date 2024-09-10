#A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

#Create a function that determines whether a number is a Disarium or not.

#examples
#is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

def is_disarium(n):
	sum = 0
	for idx,digit in enumerate(str(n)):
		sum = sum + int(digit) ** (idx + 1)
	
	return sum == n