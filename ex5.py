my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
# So lets assume that %s can only work with words, statements. So because % my_name is, in its core, a statement this allows it to show in print?
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
# It seems likely that it maybe correct that %s works for statements with letters and %d is for numbers
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# %s it used twice. So what is assumed is that if you have two variables in () with %. It will show them in order that they appear in first
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
