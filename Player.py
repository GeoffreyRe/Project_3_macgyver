from copy import deepcopy
import pygame
class Player(object):
	def __init__(self,map_player):
		self.position_player_index,self.position_player_px = map_player.find_player()
		self.player_rect = pygame.Rect(self.position_player_px[0], self.position_player_px[1],56,45)

	def move_up(self,map_player):
		previous_position = deepcopy(self.position_player_index)
		if map_player.map_list[self.position_player_index[1] - 1][self.position_player_index[0]] == 0:
			self.position_player_index[1] -= 1
			self.position_player_px[1] -= 45
			self.player_rect.y -= 45
			new_position = self.position_player_index
			map_player.change_map(previous_position, new_position)
		else:
			print("You can not go to this position")

	def move_down(self,map_player):
		previous_position = deepcopy(self.position_player_index)
		if map_player.map_list[self.position_player_index[1] +1][self.position_player_index[0]] == 0:
			self.position_player_index[1] += 1
			self.position_player_px[1] += 45
			self.player_rect.y += 45
			new_position = self.position_player_index
			map_player.change_map(previous_position, new_position)
		else:
			print("You can not go to this position")

	def move_left(self,map_player):
		previous_position = deepcopy(self.position_player_index)
		if map_player.map_list[self.position_player_index[1]][self.position_player_index[0] - 1] == 0:
			self.position_player_index[0] -= 1
			self.position_player_px[0] -= 56
			self.player_rect.x -= 56
			new_position = self.position_player_index
			map_player.change_map(previous_position, new_position)
		else:
			print("You can not go to this position")

	def move_right(self,map_player):
		previous_position = deepcopy(self.position_player_index) # on crée une véritable copie car sinon previous position changera après la ligne 115
		if map_player.map_list[self.position_player_index[1]][self.position_player_index[0] + 1] == 0:
			self.position_player_index[0] += 1
			self.position_player_px[0] += 56
			self.player_rect.x += 56
			new_position = self.position_player_index
			map_player.change_map(previous_position, new_position)

		else:
			print("You can not go to this position")