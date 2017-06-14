x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
# Not 100% certain what %r is but I know it effects % x
print "I also said: '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
# This prints out what joke_evaluation means along with false afterwords. False due to %

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# variable w + e combine makes puts the statements together
