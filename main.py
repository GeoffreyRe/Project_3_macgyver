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
# loop wich keeps the program "open"
while launched:
	# events managements
	for event in pygame.event.get(): # we can retrieve events thanks to pygame.event.get() ( = a list)
		# if the user wants to close the program
		if event.type == pygame.QUIT:
			launched = False
		# if the player press a key of the keyboard
		if event.type == pygame.KEYDOWN:
			# if the player wants to go up
			if event.key == pygame.K_UP:
				mac_gyver.move_up(map_player)
				display.refresh(map_player)
			# to go down
			elif event.key == pygame.K_DOWN:
				mac_gyver.move_down(map_player)
				display.refresh(map_player)
			# to go left
			elif event.key == pygame.K_LEFT:
				mac_gyver.move_left(map_player)
				display.refresh(map_player)

			# to go right
			elif event.key == pygame.K_RIGHT:
				mac_gyver.move_right(map_player)
				display.refresh(map_player)
			# the user has to press "a" to retrieve an item
			elif event.key == pygame.K_q:
				if mac_gyver.player_rect.colliderect(needle.item_rect) : # the player can retrieve an item only if the player is close to the item
					if needle.on_map: # check if the item is on the map or not
						mac_gyver.retrieve_item(needle) # the player retrieve the item
						needle.go_to_inventory() #on_map = False
						map_player.delete_item(needle) # item disappears of the map_list
						display.refresh(map_player) #update of the display

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
			# the user can use "q" if he wants to finish the game
			elif event.key == pygame.K_a:
				#check if the player is next to the jailer
				if mac_gyver.position_player_index == map_player.find_jailer():
					# check if the player has 3 items
					if len(mac_gyver.inventory) == 3:
						launched = False # win the game !

