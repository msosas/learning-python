story = "Pizza was invented by a adj01 nac01 chef named person01. To make a pizza, you need to take a lump of noun01, and make a thin, round adj02 noun02. Then you cover it with adj03 sauce, adj04 cheese , and fresh chopped nouns. Next you have to bake it in a very hot noun03. When it is done, cut into num01 shapes. Some kids like food01 pizza the best, but my favourite is the food02 pizza. If I could, I eat pizza, num02 times a day!"

person01 = input("Enter a name\n")
adj01 = input("Enter an adjetive\n")
adj02 = input("Enter another adjetive\n")
adj03 = input("Enter another adjetive\n")
adj04 = input("Enter another adjetive\n")
nac01 = input("Enter a nacionality\n")
noun01 = input("Enter a noun\n")
noun02 = input("Enter another noun\n")
noun03 = input("Enter another noun\n")
num01 = input("Enter a number\n")
num02 = input("Enter another number\n")
shapes = input("Enter shapes\n")
nouns = input("Enter a noun in plurar\n")
food01 = input("Enter a food\n")
food02 = input("Enter another food\n")

'''person01 = "Cacho"
adj01 = "small"
adj02 = "big"
adj03 = "fat"
adj04 = "round"
nac01 = "Argentinian"
noun01 = "ball"
noun02 = "stick"
noun03 = "leaf"
num01 = "42"
num02 = "70"
shapes = "squared"
nouns = "waves"
food01 = "tacos"
food02 = "onions"
'''

story = story.replace("person01", person01)
story = story.replace("adj01", adj01)
story = story.replace("adj02", adj02)
story = story.replace("adj03", adj03)
story = story.replace("adj04", adj04)
story = story.replace("nac01", nac01)
story = story.replace("noun01", noun01)
story = story.replace("noun02", noun02)
story = story.replace("noun03", noun03)
story = story.replace("num01", num01)
story = story.replace("num02", num02)
story = story.replace("shapes", shapes)
story = story.replace("nouns", nouns)
story = story.replace("food01", food01)
story = story.replace("food02", food02)


print(story)