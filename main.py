from Display import * 
from Map import *
from Player import *
from Item import *

display = Display()
map_player = Map()
needle = Item("needle", 4, map_player)
map_player.put_item_on_map(needle)
ether = Item("ether", 5, map_player)
map_player.put_item_on_map(ether)
tube = Item("tube",6,map_player)
map_player.put_item_on_map(tube)
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

			elif event.key == pygame.K_q:
				if mac_gyver.player_rect.colliderect(needle.item_rect) :
					if needle.on_map:
						mac_gyver.retrieve_item(needle)
						needle.go_to_inventory()
						map_player.delete_item(needle)
						display.refresh(map_player)

				if mac_gyver.player_rect.colliderect(ether.item_rect) :
					if ether.on_map:
						mac_gyver.retrieve_item(ether)
						ether.go_to_inventory()
						map_player.delete_item(ether)
						display.refresh(map_player)


				if mac_gyver.player_rect.colliderect(tube.item_rect) :
					if tube.on_map:
						mac_gyver.retrieve_item(tube)
						tube.go_to_inventory()
						map_player.delete_item(tube)
						display.refresh(map_player)

			elif event.key == pygame.K_a:
				if mac_gyver.position_player_index == map_player.find_jailer():
					if len(mac_gyver.inventory) == 3:
						launched = False
