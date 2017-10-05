import random

choice =  input("Rock, Paper or Scissors???\n")
options = ( 'rock','paper','scissors')
aiindex = random.randint(0,2)
aichoice = options[aiindex]

choice = choice.lower()

while choice not in options:
	print("That is not a valid option\n")
	choice =  input("Rock, Paper or Scissors???\n")
	choice = choice.lower()

if choice == "rock" and aichoice == "rock":
	print("It's a tie")
if choice == "rock" and aichoice == "paper":
	print("You lost!")
if choice == "rock" and aichoice == "scissors":
	print("You Won!")
if choice == "paper" and aichoice == "rock":
	print("You Won!")
if choice == "paper" and aichoice == "paper":
	print("It's a tie")
if choice == "paper" and aichoice == "scissors":
	print("You lost!")
if choice == "scissors" and aichoice == "rock":
	print("You lost!")
if choice == "scissors" and aichoice == "paper":
	print("You won!")
if choice == "scissors" and aichoice == "scissors":
	print("It's a tie!")	

print("----------------------------------------------")
print("The match was:\n" + choice + " vs " + aichoice)


