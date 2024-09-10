#Create a function that takes two arguments: 
# the original price and the discount percentage as integers 
# and returns the final price after the discount,
# rounded to two decimal places.
def dis(price, discount):
	new_price = price - price * (discount / 100)
	return round(new_price, 2)
