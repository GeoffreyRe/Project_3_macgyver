import pygame
# class that contains method and attributes linked with items


class Item():

	def __init__(self, name, value, map_player):
		self.name = name  # name of the item
		self.value = value  # value of the item on the map_list
		self.index_value = map_player.random_position()  # search a place on the map list wich is free ( = 0 = ground)
		self.item_rect = pygame.Rect((self.index_value[0] * 56) - 1, (self.index_value[1] * 45) - 1, 58, 47)  # associate a rect to the item
		self.on_map = True

	def go_to_inventory(self):
		self.on_map = False  # if the item is taken by the player, it is not on the map anymore
