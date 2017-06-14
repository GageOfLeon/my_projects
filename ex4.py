cars = 100
# car is a varaible. Variables can be given commands to do things. At the moment car is used to show 100.
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
# Cars - drivers boils down to what they mean as variables. So it's 100 - 30
cars_driven = drivers
# cars_driven is going to be the amount of drivers
carpool_capacity = cars_driven * space_in_a_car
# carpool_capacity is going to equal car_driven which is 30 multplied by space_in_a_car which is 4.0
average_passengers_per_car = passengers / cars_driven
# average_passengers_per_car is going to equal 90 divided by 30

print "There are", cars, "cars available."
print "There will be", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
# This will print out the variables and what they mean. 
