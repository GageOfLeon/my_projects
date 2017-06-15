tabby_cat = "\tI'm tabbed in."
#This variable's statement will be tabbed due to \t
persian_cat = "I'm split\non a line."
#This variable's statement will move half of it down due to \n
backslash_cat = "I'm \\ a \\ cat."
#Since '\' is used twice it will show only one backslash
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#Since it uses triple quotes, it can write as much as it wants.
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
#Prints the variable in order from top to bottom
