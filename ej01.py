import random 
import sys

userInput = int(input("Guess the number \n"))
min = int(sys.argv[1])
max = int(sys.argv[2])
number = random.randint(min,max)
while (number != userInput):
	userInput = int(input("Try Again \n"))

print("CORRECT!")
