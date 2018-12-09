import pygame
import json

class Map(object):
	def initialization(self):
		with open("map.json") as f:
			self.map_list = json.load(f) 

	def display():
		


pygame.init()

map_py = Map()
map_py.initialization()
print(map_py.map_list)


