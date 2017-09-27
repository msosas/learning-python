import requests as req
import random

wordNumber = random.randint(0,2642)
words = req.get('https://www.randomlists.com/data/words.json').json()['data']
hangWord = words[wordNumber]

solution = hangWord
n = len(hangWord)
c = 0
lives = 10



userWord = ["" for i in range(0,n)]


print("Please enter a letter to guess\n")
while(c < n and lives > 0):
	letter = input()
	if letter in hangWord:
		userWord[hangWord.find(letter)] = letter
		c = c + 1 
		hangWord = hangWord.replace(letter,'$',1)
		print("Good! Guess the next one...\n")
		print("You have " + str(lives) + " lives\n")
		print(userWord)
	else:
		lives = lives - 1
		print("Bad luck, try again. You have " + str(lives) + " lives\n")

if c == n:
	print("Excelent, the solution was " + solution)
else:
	print("Sorry, you LOST. The solution was " +  solution + "\n")

		

