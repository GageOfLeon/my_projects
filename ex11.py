print "How old are you?",
age = raw_input ()
print "How tall are you?",
height = raw_input ()
print "How much do you weigh?",
weight = raw_input ()
# the variables are determined by user input. The command raw_input() allows the user to input what they desire

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
# %r is connected with the variables. It seems to print out the raw_input that the user had typed up. % performs a string format
