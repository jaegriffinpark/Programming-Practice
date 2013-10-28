# this line specifies the function and the two necessary arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

# here, the function is called using two direct number arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# this time, the function is called using arguments that are variables, defined first
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this example shows that the function can be called using evaluated math arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# finally, this example uses variable arguments, augmented by math notation
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def wine_glasses(number_of_glasses, wine_year):
	print "You have %d glasses of wine!" % number_of_glasses
	print "The wine is %d years old." % (2013 - wine_year)


wine_glasses (10, 1957)