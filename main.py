from Display import * 
from Map import *
from Player import *

display = Display()
map_player = Map()
map_player.put_item_on_map()
mac_gyver = Player(map_player)
display.load_wall()
display.load_ground()
display.load_player_display()
display.load_jailer()
display.load_items()
display.refresh(map_player)


launched = True

while launched:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			launched = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				mac_gyver.move_up(map_player)
				display.refresh(map_player)

			elif event.key == pygame.K_DOWN:
				mac_gyver.move_down(map_player)
				display.refresh(map_player)

			elif event.key == pygame.K_LEFT:
				mac_gyver.move_left(map_player)
				display.refresh(map_player)

			elif event.key == pygame.K_RIGHT:
				mac_gyver.move_right(map_player)
				display.refresh(map_player)
