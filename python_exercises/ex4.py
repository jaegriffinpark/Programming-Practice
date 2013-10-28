#The total number of cars
cars = 100

#The maximum capacity of each car
space_in_a_car = 4.0

#The total number of drivers
drivers = 30

#The total number of passengers
passengers = 90

#The number of cars that cannot be driven
cars_not_driven = cars - drivers

#The number of cars driven
cars_driven = drivers

#The total number of individuals that can be transported
carpool_capacity = cars_driven * space_in_a_car

#The average number of passengers riding in each car
average_passengers_per_car = passengers / cars_driven


print "There are" , cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


print "Hey %s there." % "you"