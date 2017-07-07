from sys import exit

def Trap_room():
	print "This room is seemingly empty, not a soul in sight.""You see something...'Checkout'?"

	next = raw_input("> ")
	if next == "Checkout" or next == "checkout":
		dead("Stepping closer you felt a sharp pain where your arm was.")
	elif next == "Leave" or next == "leave":
		first_room()
	else:
		Trap_room()		

def Tree_room():
	print "The door slam shut behind you"
	print "This room is odd."
	print "There is grass, a single tree in the middle, and rope tied on the tree. Should probably 'checkout'"
	rope_key = True
	while True:	
		next = raw_input("> ")
		if next == "Checkout " or next == "checkout":
			print "The trunk of the tree is rotten."
			print "It's front resemables that of a man's face"
			print "Screaming as it seems. A key is tied to the rope. Maybe 'Take key'?"

		elif next == "Take key" or next == "take key":
			print "Can not, tied to rope. Try to 'untie rope'"				
		elif next == "untie rope" or next == "Untie rope":
			check = True
			print "Rope is untied"
			print "The face shaped trunk seems to be laughing"
			print "You grabed the key"
			rope_key = False
			print "A code is written on the side: 1134 "
			print "Should now 'leave' the room"
	
		elif next == "leave" or next == "Leave":
				print "Leaving room"
				first_room()	
		else:
			print "You hear whispers"
			next

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
		
def dead(gameover):
	print gameover, "'Rip in peace'"
	exit(0)

def start():
	print "A storm is brewing"
	print "If you stay out you'll likely get tossed and turned by the raging wind"
	print "You stumble to what seems to be an abandon Mansion."
	print "Green and moss grow on its sides"
	print "Best to go in."
	print "Upon entering shows three doors. One up a flight of steps, the other down, and one towards the left."
	first_room()

def first_room():
	print "Up, down, or left where will you go?"
	next = raw_input("> ")
	if next == "up":
		Trap_room()
	elif next == "down":
		Dread_room()
	elif next == "left":
		print "Door seems to be locked by a code."
		next = raw_input("> ")
		if next == "1134": #Doesn't work if it's elif
			graveyard()
		else:
			print "That's not right..."
			first_room()
	else:
		first_room()

start()
