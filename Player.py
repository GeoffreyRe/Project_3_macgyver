from copy import deepcopy
import pygame


# class that contains methods and attributes linked with the player

class Player(object):

    def __init__(self, map_player):
        self.position_player_index, self.position_player_px = map_player.find_player()  # it allows to know where is the player
        self.player_rect = pygame.Rect(self.position_player_px[0], self.position_player_px[1], 56, 45)
        # a list wich will contains each item that the player can retrieve
        self.inventory = []

    def move_up(self, map_player):
        # deepcopy method allows to create a real copy of a list
        previous_position = deepcopy(self.position_player_index)
        # check if the position where the player wants to go is not a wall, an item or the jailer
        if map_player.map_list[self.position_player_index[1] - 1][self.position_player_index[0]] == 0:
            self.position_player_index[1] -= 1
            self.position_player_px[1] -= 45
            self.player_rect.y -= 45
            # keeps the new position in a variable
            new_position = self.position_player_index
            # the map_list has to be refresh
            map_player.change_map(previous_position, new_position)
        else:
            print("You can not go to this position")
    # idem if the player wants to go down

    def move_down(self, map_player):
        previous_position = deepcopy(self.position_player_index)
        if map_player.map_list[self.position_player_index[1] + 1][self.position_player_index[0]] == 0:
            self.position_player_index[1] += 1
            self.position_player_px[1] += 45
            self.player_rect.y += 45
            new_position = self.position_player_index
            map_player.change_map(previous_position, new_position)
        else:
            print("You can not go to this position")
    # idem if the player wants to go left

    def move_left(self, map_player):
        previous_position = deepcopy(self.position_player_index)
        if map_player.map_list[self.position_player_index[1]][self.position_player_index[0] - 1] == 0:
            self.position_player_index[0] -= 1
            self.position_player_px[0] -= 56
            self.player_rect.x -= 56
            new_position = self.position_player_index
            map_player.change_map(previous_position, new_position)
        else:
            print("You can not go to this position")
    # if the player wants to go right

    def move_right(self, map_player):
        previous_position = deepcopy(self.position_player_index)
        if map_player.map_list[self.position_player_index[1]][self.position_player_index[0] + 1] == 0:
            self.position_player_index[0] += 1
            self.position_player_px[0] += 56
            self.player_rect.x += 56
            new_position = self.position_player_index
            map_player.change_map(previous_position, new_position)
        else:
            print("you can not go to this position")
    # item add to the inventory of the player if the player retrieves it

    def retrieve_item(self, item):
        self.inventory.append(item)
