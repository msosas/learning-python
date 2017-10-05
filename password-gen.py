import random

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','?','@','#','%','$']
c = 0

password = ""
passwordlen = 8
print("How strong your password should be?\n")

strength = int(input("1 - 2 - 3\n"))


if strength == 1:
	passwordlen = 4
	complexity = 24
if strength == 2:
	passwordlen = 8
	complexity = 59
if strength == 3:
	passwordlen = 10
	complexity = 65

while (c < passwordlen):
	c = c + 1
	index = random.randint(0,complexity)
	password = password + characters[index]	

print(password)
