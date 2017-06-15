from sys import argv

script, filename = argv

txt = open(filename)
# this variable will open a file that will be placed since argv is active

print "Here's your file %r:" % filename
print txt.read ()
#reads the txt file and if inputed again it will read it again

print "Here's your file %r:" % filename
file_again = raw_input ("> ")

txt_again = open(file_again)

print txt_again.read() 
