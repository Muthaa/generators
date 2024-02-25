"""
Random character password generator.
Random choice of string.ascii_letters+string.digits+string.punctuation
Displays two randomly generated passwords 
The passwords are regeneratted on mouse click.
"""
import string
from random import *
import pygame
from pygame.locals import *

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.RESIZABLE)
pygame.display.set_caption('PassGen')
label_font = pygame.font.Font('rambling.ttf', 32)
medium_font = pygame.font.Font('Roboto-Regular.ttf', 30)

neonblue = (0, 255, 255)
gold = (212, 175, 55)

def charst():
	play_text = label_font.render("Random passwords are :", True, gold)
	screen.blit(play_text, (WIDTH - 450, HEIGHT - 340))

	mixchars = string.ascii_letters+string.digits+string.punctuation
	randompass = "".join(choice(mixchars) for x in range(randint(8, 16)))
	with open("urct.txt", 'a+') as file:
		file.seek(0)
		file.write(str(randompass)+"\n")

	play_text2 = medium_font.render(randompass, True, neonblue)
	screen.blit(play_text2, (WIDTH - 425 , HEIGHT -305))

	randompass2 = "".join(choice(mixchars) for x in range(randint(10, 16)))
	with open("urct.txt", 'a+') as file:
		file.write(str(randompass2)+"\n")
		
	play_text3 = medium_font.render(randompass2, True, neonblue)
	screen.blit(play_text3, (WIDTH - 425 , HEIGHT -275))
	#print ("Random password is :",randompass)
	#return ' '.join(Random.sample(mixchars, len))
# charst()
run = True
while run:
	for event in pygame.event.get():
		if event.type == QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONUP:
			screen = pygame.display.set_mode([WIDTH, HEIGHT],pygame.RESIZABLE)
			charst()
	pygame.display.flip()
pygame.quit()





