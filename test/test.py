"""
import pygame
import time

window_screen = pygame.display.set_mode((840,675))

spritesheet_right = []
imagesheet_right = pygame.image.load("animation_right.png")
window_screen.fill((0,0,0))
imagesheet_left = pygame.image.load("animation_left.png")
image_face = pygame.image.load("perso_de_face.png")
face_sheet = pygame.image.load("perso_face.png")
dos_sheet = pygame.image.load("perso_dos.png")
i=7
while i < 463:
	image = imagesheet_right.subsurface(i,0,26,50)
	spritesheet_right.append(image)
	i +=64

spritesheet_left= []

i = 0 
while i < 463:
	image = imagesheet_left.subsurface(i,0,28,49)
	spritesheet_left.append(image)
	i +=64

spritesheet_face = []

i = 0
while i <463:
	image = face_sheet.subsurface(i,0,28,50)
	spritesheet_face.append(image)
	i+=64
spritesheet_dos = []

i = 0
while i <463:
	image = dos_sheet.subsurface(i,0,28,50)
	spritesheet_dos.append(image)
	i+=64



x= 0
y = 50

launched = True 
touche = 0

while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				if touche == pygame.K_LEFT:
					time.sleep(.07)
					window_screen.fill((0,0,0))
					window_screen.blit(image_face,(x,y))
					pygame.display.flip()
				for sprite in spritesheet_right:
					time.sleep(.07)
					window_screen.fill((0,0,0))
					window_screen.blit(sprite, (x,y))
					x += 7
					pygame.display.flip()
					print(x)

			if event.key == pygame.K_LEFT:
				if touche == pygame.K_RIGHT:
					time.sleep(.07)
					window_screen.fill((0,0,0))
					window_screen.blit(image_face,(x,y))
					pygame.display.flip()
				for sprite in spritesheet_left:
					time.sleep(.07)
					window_screen.fill((0,0,0))
					window_screen.blit(sprite, (x,y))
					x -= 7
					pygame.display.flip()
			if event.key == pygame.K_DOWN:
				if touche == pygame.K_UP:
					time.sleep(.07)
					window_screen.fill((0,0,0))
					window_screen.blit(spritesheet_right[0],(x,y))
					pygame.display.flip()
				for sprite in spritesheet_face:
					time.sleep(.07)
					window_screen.fill((0,0,0))
					window_screen.blit(sprite, (x,y))
					y += 7
					pygame.display.flip()

			if event.key == pygame.K_UP:
				if touche == pygame.K_DOWN:
					time.sleep(.07)
					window_screen.fill((0,0,0))
					window_screen.blit(spritesheet_left[0],(x,y))
					pygame.display.flip()
				for sprite in spritesheet_dos:
					time.sleep(.07)
					window_screen.fill((0,0,0))
					window_screen.blit(sprite, (x,y))
					y -= 7
					pygame.display.flip()


			touche = event.key

"""

def fonction(a,b,c):
	if a == 2:
		print("a = 2")

	else: 
		print("coucou")


fonction(2,2,3)







