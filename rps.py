# Shane Mckisson
# Rock, Paper, Scissors
#--------------------------------------#
import random

pScore = 0
cScore = 0
ties = 0
cChoices = ["Rock", "Paper", "Scissors"]


print("Welcome to Rock. Paper, Scissors")
playerName = input("What is your name? ")



def printScore():
	print("Score: ")
	print(playerName + ": " + str(pScore))
	print("Computer Score: " + str(cScore))
	print("Ties: " + str(ties))

while True:
	printScore()
	pChoice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors, or 'q' to quit. ")
	cChoice = random.choice(cChoices)

	if pChoice == "q":
		break

	if pChoice == "r":
		print("You picked rock.")
		if cChoice == "rock":
			print("Computer picked rock.")
			print("This is a tie.")
			ties = ties + 1
	    
		elif cChoice == "paper":
			print("Computer picked paper.")
			print("Paper beats rock.")
			cScore = cScore + 1
		else:
			print("Computer picked scissors.")
			print("Rock beats scissors.")
			pScore = pScore + 1

	if pChoice == "p":
	 	print("You picked paper.")
	 	if cChoice == "paper":
	 		print("Computer picked paper.")
	 		print("This is a tie.")
	 		ties = ties + 1

		elif cChoice == "scissors":
	    	print("Computer picked scissors.")
			print("Scissors beats paper.")
			cScore = cScore + 1
	     
		else:
	    	print("Computer picked rock.")
	    	print("Paper beats rock.")
	    	pScore = pScore + 1

	if pChoice == "s":
	 	print("You picked scissors.")
	 	if cChoice == "scissors":
	 		print("Computer picked scissors.")
	 		print("This is a tie.")
	 		ties = ties + 1
	    
		if cChoice == "rock":
			print("Computer picked rock.")
			print("Rock beats scissors.")
			cScore = cScore + 1
	     
		else:
	    	print("Computer picked paper.")
	    	print("Scissors beats paper.")
	    	pScore = pScore + 1

else:
		 print("You something not on the list.")