import pygame
import json
import random
# class that contains methods and attributes linked with the map list
class Map(object):
	def __init__(self):
		with open("map.json") as f:
			self.map_list = json.load(f) #transform an json file into a python object
	# method that find the index of the player
	def find_player(self):
		for index_line, line in enumerate(self.map_list):
			for index_sprite, sprite in enumerate(line):
				if sprite == 2:
					position_player_index = [index_sprite, index_line]
					position_player_px = [index_sprite * 56, index_line * 45]

		return position_player_index, position_player_px
	# idem for the jailer 
	def find_jailer(self):
		for index_line, line in enumerate(self.map_list):
			for index_sprite, sprite in enumerate(line):
				if sprite == 3:
					position_jailer_index = [index_sprite - 1, index_line]
		return position_jailer_index
	# when the player moves, it changes the map list
	def change_map(self,previous_position, new_position):
		previous_position_y = previous_position[1]
		previous_position_x = previous_position[0]
		new_position_y = new_position[1]
		new_position_x = new_position[0]
		self.map_list[previous_position_y][previous_position_x] = 0
		self.map_list[new_position_y][new_position_x] = 2
	# "delete" the item on the map list when it is taken by the player
	def delete_item(self, item):
		self.map_list[item.index_value[1]][item.index_value[0]] =0
	# method that finds index positions which are not occupied (= 0)
	def random_position(self):
		accepted = False
		while not accepted: 
			position_index_x = random.randint(1,13) # method that gives a int between 1 and 13
			position_index_y = random.randint(1,13)
			if self.map_list[position_index_y][position_index_x] == 0:
				accepted = True
		return (position_index_x, position_index_y)

	def put_item_on_map(self, item):
		self.map_list[item.index_value[1]][item.index_value[0]] = item.value







