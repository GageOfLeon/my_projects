from sys import exit

def Trap_room():
	print "This room is seemingly empty, not a soul in sight.""You see something...'Checkout'?"

	next = raw_input("> ")
	if next == "Checkout" or next == "checkout":
		dead("Stepping closer you felt a sharp pain where your arm was.")
	elif next == "Leave" or next == "turn around":
		first_room()
	else:
		Trap_room()		

def Dread_room():
	print "The door slam shut behind you"
	print "This room is odd."
	print "There is grass, a single tree in the middle, and rope tied on the tree. Should  probably 'checkout '"
	rope_key = True

	while True:
	
		next = raw_input("> ")
		if next == "Checkout " or next == "checkout":
			print "From where you are standing, it would be diffcult to investagate the tree. Should walk to tree"
		elif next == "Checkout room" or next == "checkout room":
			print "The room is dark, the tree is colored by light gray shadows"
		elif next == "Walk to tree" or next == "walk to tree":
			print "In front of the tree. Can now 'Checkout' "
			check = False
			while check == False:
				next = raw_input("> ")
				if next == "checkout" or next == "Checkout":
					check = True
					print "The trunk of the tree is rotten."
					print "It's front resemables that of a man's face"
					print "Screaming as it seems. A key is tied to the rope. Maybe 'Take key'?"
	
			check = False
			while check == False:
				next = raw_input("> ")
				if next == "Take key" or next == "take key":
					print "Can not, tied to rope. Try to 'untie rope'"				
				elif next == "untie rope" or next == "Untie rope":
					check = True
					print "Rope is untied"
					print "The face shaped trunk seems to be laughing"
					print "You grabed the key"
					rope_key = False
					print "A code is written on the side: 1134 "
					print "Should now 'leave' the room"
					next = raw_input("> ")
					if next == "leave" or next == "Leave":
						print "Leaving room"
						first_room()	
					else:
						print "You hear whispers"



def graveyard():
	print "Tombstones line up as if waiting to whatever is at the end of this room"
	print "A figure stands at the end. Hunched over waving. 'Go to him'?"
	next = raw_input('> ')
	if next == "leave":
		dead("As soon as you turned your back, you felt weightless. As you fall you spot a familar headless body. Fall, fall, sleep, sleep.")
	elif next == "Go to him" or next == "go to him'":
		print "As you approach the strange old man, he smiles and says time to wake up"
		print "You wake up at your bed. You survive a strange nightmare."
		exit(0)
	else:
		print "Indecision is never a good thing,"
		graveyard()
		




def dead(why):
	print why, "'Rip in peace'"
	exit(0)

def start():
	print "A storm is brewing"
	print "If you stay out you'll likely get tossed and turned by the raging wind"
	print "You stumble to what seems to be an abandon Mansion."
	print "Green and moss grow on its sides"
	print "Best to go in."
	print "Upon entering shows three doors. One up a flight of steps, the other down, and one towards the left."
	print "Where do you go, up, down, or left?"

	next = raw_input("> ")
	if next == "up":
		Trap_room()
	elif next == "down":
		Dread_room()
	elif next == "left":
		print "Door seems to be locked by a code."
		next = raw_input("> ")
		if next == "1134":
			graveyard()
		else:
			print "That's not right..."
			first_room()
	else:
		first_room()

def first_room():
	print "Back at the first room. Up, down, or left where will you go?"
	next = raw_input("> ")
	if next == "up":
		Trap_room()
	elif next == "down":
		Dread_room()
	elif next == "left":
		print "Door seems to be locked by a code."
		next = raw_input("> ")
		if next == "1134":
			graveyard()
		else:
			print "That's not right..."
			first_room()
	else:
		first_room()

start()


