#Write a function that takes a list of numbers and returns a list with two elements:

#The first element should be the sum of all even numbers in the list.
#The second element should be the sum of all odd numbers in the list.

def sum_odd_and_even(lst):
	odd_even = [0,0]
	for item in lst:
		if(item % 2 == 0):
			odd_even[0] = odd_even[0] + item
		else:
			odd_even[1] = odd_even[1] + item
	return odd_even

#alternate solution, use sum() and list comprehension

def sum_odd_even(lst):
	return [sum([i for i in lst if not i%2]), sum([i for i in lst if i%2])]
