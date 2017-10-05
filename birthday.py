people = {
	"Pablo Magariños": "01-08-1986",
	"Cristian Caram": "01-06-1988",
	"Toni Tralice": "12-07-1986"
}

print("Welcome to the birthday dictionary. We know the birthdays of:\n")

for names in people:
	print(names)

selection = input("Who's birthday do you want to look up?\n")

print(selection + "'s birthday is on " + people[selection])