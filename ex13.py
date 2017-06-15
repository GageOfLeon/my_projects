from sys import argv
# The first line allows use to add features from the python feature set. argv is the "arguement variable" It holds arguements that is pass to the script
script, first, second, third = argv
# The inputs here are saved until called on since its an argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
# Inputs that were stored are now printed out due to the print command
