import pygame
import json
import random

class Map(object):
	def __init__(self):
		with open("map.json") as f:
			self.map_list = json.load(f)
	def find_player(self):
		for index_line, line in enumerate(self.map_list):
			for index_sprite, sprite in enumerate(line):
				if sprite == 2:
					position_player_index = [index_sprite, index_line]
					position_player_px = [index_sprite * 56, index_line * 45]

		return position_player_index, position_player_px

	def change_map(self,previous_position, new_position):
		previous_position_y = previous_position[1]
		previous_position_x = previous_position[0]
		new_position_y = new_position[1]
		new_position_x = new_position[0]
		self.map_list[previous_position_y][previous_position_x] = 0
		self.map_list[new_position_y][new_position_x] = 2

	def random_position(self):
		accepted = False
		while not accepted: 
			position_index_x = random.randint(1,13)
			position_index_y = random.randint(1,13)
			if self.map_list[position_index_y][position_index_x] == 0:
				accepted = True
		return (position_index_x, position_index_y)

	def put_item_on_map(self):
		position_object_1 = self.random_position()
		self.map_list[position_object_1[1]][position_object_1[0]] = 4

		position_object_2 = self.random_position()
		self.map_list[position_object_2[1]][position_object_2[0]] = 5

		position_object_3 = self.random_position()
		self.map_list[position_object_3[1]][position_object_3[0]] = 6







