import random

with open ("Qfile", 'r') as file:
	lines= [line.rstrip() for line in file]

quote = random.choice(lines)
print (quote)