tabby_cat = "\tI'm tabbed in."
persian_cat="I'm split\n on a line"
backsplash_cat="I'm \\a\\cat"

fat_cat="""
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backsplash_cat)
print(fat_cat)

while True:
	for i in["/","-","|","\\","|"]:
		print("%s\r" %i,)