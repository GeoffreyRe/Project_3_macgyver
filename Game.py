from Display import * 
from Map import *
from Player import *
from Item import *
class Game(object):
	def __init__(self):
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
		self.items_in_game = [needle,ether,tube]
		self.keyboard_list_movements = [pygame.K_UP, pygame.K_DOWN,pygame.K_LEFT, pygame.K_RIGHT]
		self.keyboard_functions = [mac_gyver.move_up, mac_gyver.move_down, mac_gyver.move_left, mac_gyver.move_right]

	def press_keyboard_movement(self,player,map_player,keyboard_value,display):
		for index, k in enumerate(self.keyboard_list_movements):
			if k == keyboard_value:
				player.self.keyboard_functions[index](map_player)
				display.refresh(map_player)

	def press_keyboard_items(self, player,map_player, display):
		for item in self.items_in_game:
			if player.player_rect.colliderect(item.item_rect) : # the player can retrieve an item only if the player is close to the item
					if item.on_map: # check if the item is on the map or not
						player.retrieve_item(item) # the player retrieve the item
						item.go_to_inventory() #on_map = False
						map_player.delete_item(item) # item disappears of the map_list
						display.refresh(map) #update of the display

	def victory(self,player,map_player):
		if player.position_player_index == map_player.find_jailer():
			if len(player.inventory) == 3:
				print("you win !")
			else:
				print("you died !")






	def loop(self):
		launched = True
		while launched:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					launched = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.press_keyboard_items(mac_gyver,map_player, display)

					elif event.key == pygame.K_a:
						self.victory(mac_gyver,map_player)
						launched = False

					else:
						self.press_keyboard_movement(mac_gyver,map_player,event.key,display)


