#use of len() in any form is prohibited
#Create a function that takes a number num and returns its length.

#my original solution
def number_length(num):
	num_str = str(num)
	count = 0
	for digit in num_str:
		count += 1
	
	return count

#another possible solution
def number_length2(num):
	return sum([1 for i in str(num)])
    #add ones to a new a list, then add all the ones