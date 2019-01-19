def isItADozen(input): 
	if type(input) != int:
		result = "This is not a number"
	elif input == 12:
		result =  "Yup, it's a dozen!"
	elif input < 12 and input > 0:
		result = "Nope, you have less than a dozen"
	elif input > 12:
		result =  "You have more than a dozen here"
	elif input <=0:
		result =  "You don't have any at all!"
	return result