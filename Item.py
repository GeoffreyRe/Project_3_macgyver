import pygame

class Item():

	def __init__(self, name,value,map_player ):
		self.name = name
		self.value = value
		self.index_value = map_player.random_position()
		self.item_rect = pygame.Rect((self.index_value[0] * 56) - 1, (self.index_value[1] * 45) - 1, 58, 47)
		self.on_map = True

	def go_to_inventory(self):
		self.on_map = False