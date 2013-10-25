import random

def fillDoors():
	doors = [0,0,0]
	doors[random.randint(0,2)] = 1
	return doors

def chooseGuess():
	return random.randint(0,2)

def revealDoor(d,g):
	for i in range(0,3):
		if d[i] != 1 and i != g:
			return i 

def changeGuess(g,o):
	for i in range(0,3):
		if i != g and i != o:
			return i

def checkGuess(d,g):
	if d[g] == 1:
		return True
	else: 
		return False

def main():
	TRIES = 10000
	WINS = 0
	LOSSES = 0
	for x in range(0,TRIES):
		DOORS = fillDoors()
		GUESS = chooseGuess()
		OPEN = revealDoor(DOORS,GUESS)
		NEW_GUESS = changeGuess(GUESS,OPEN)
		CORRECT = checkGuess(DOORS,NEW_GUESS)
		# print DOORS
		# print "Guess is door", GUESS
		# print "Host opens door", OPEN
		# print "Changing guess to", NEW_GUESS
		if CORRECT:
			WINS += 1
			# print "Winner!"
		else:
			LOSSES += 1
			# print "Loser"
	winRate = float(WINS) / float(TRIES) * 100
	print TRIES, "tries ||", WINS, "wins", LOSSES, "losses", "||", winRate, "%"


main()
