cities = {'CA': 'San Franciso', 'MI': 'Detroit', 'FL': 'Jacksonville'}


cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."

# OK pay attention!
cities['_find'] = find_city

while True:
	print "State? (ENTER TO QUIT)",
	state = raw_input("> ")

	if not state: break

	#this line is most important ever! Study!
	city_found = cities['_find'](cities, state)
	print city_found