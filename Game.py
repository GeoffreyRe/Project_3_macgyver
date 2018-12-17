from Display import * 
from Map import *
from Player import *
from Item import *
class Game(object):
	def __init__(self):
		self.display = Display()
		self.map_player = Map()
		self.needle = Item("needle", 4, self.map_player)
		self.map_player.put_item_on_map(self.needle)
		self.ether = Item("ether", 5, self.map_player)
		self.map_player.put_item_on_map(self.ether)
		self.tube = Item("tube",6,self.map_player)
		self.map_player.put_item_on_map(self.tube)
		self.mac_gyver = Player(self.map_player)
		self.methods_display = [self.display.load_wall, self.display.load_ground,self.display.load_player_display,self.display.load_jailer,self.display.load_items]
		self.display.load_wall()
		self.display.load_ground()
		self.display.load_player_display()
		self.display.load_jailer()
		self.display.load_items()
		self.display.refresh(self.map_player)
		self.items_in_game = [self.needle,self.ether,self.tube]
		self.keyboard_list_movements = [pygame.K_UP, pygame.K_DOWN,pygame.K_LEFT, pygame.K_RIGHT]
		self.keyboard_functions = [self.mac_gyver.move_up, self.mac_gyver.move_down, self.mac_gyver.move_left, self.mac_gyver.move_right]

	def press_keyboard_movement(self,keyboard_value):
		for index, k in enumerate(self.keyboard_list_movements):
			if k == keyboard_value:
				self.keyboard_functions[index](self.map_player)
				self.display.refresh(self.map_player)

	def press_keyboard_items(self):
		for item in self.items_in_game:
			if self.mac_gyver.player_rect.colliderect(item.item_rect) : # the player can retrieve an item only if the player is close to the item
					if item.on_map: # check if the item is on the map or not
						self.mac_gyver.retrieve_item(item) # the player retrieve the item
						item.go_to_inventory() #on_map = False
						self.map_player.delete_item(item) # item disappears of the map_list
						self.display.refresh(self.map_player) #update of the display

	def victory(self):
		if self.mac_gyver.position_player_index == self.map_player.find_jailer():
			if len(self.mac_gyver.inventory) == 3:
				print("you win !")
				return False
			else:
				print("you died !")
				return False
		else:
			return True


	def loop(self):
		launched = True
		while launched:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					launched = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.press_keyboard_items()

					elif event.key == pygame.K_a:
						launched = self.victory()
						
					elif event.key in self.keyboard_list_movements:
						self.press_keyboard_movement(event.key)


