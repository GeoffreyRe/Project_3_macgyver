import pygame

class Display(object):
	def __init__(self):
		pygame.init()
		self.resolution = (840,675)
		self.window_screen = pygame.display.set_mode(self.resolution)

	def load_wall(self):
		wall_sheet = pygame.image.load("ressource/structures.png")
		self.wall = wall_sheet.subsurface(40,140,40,20)
		self.wall = pygame.transform.scale(self.wall,(56,45))

	def load_ground(self):
		ground_sheet = pygame.image.load("ressource/floor-tiles-20x20.png")
		self.ground = ground_sheet.subsurface(320,0,20,20)
		self.ground = pygame.transform.scale(self.ground, (56,45))

	def load_player_display(self):
		self.player_display = pygame.image.load("ressource/MacGyver.png")
		self.player_display = pygame.transform.scale(self.player_display, (56,45))

	def load_jailer(self):
		self.jailer = pygame.image.load("ressource/Gardien.png")
		self.jailer = pygame.transform.scale(self.jailer, (56,45))

	def load_items(self):
		self.item_1 = pygame.image.load("ressource/aiguille.png")
		self.item_1 = pygame.transform.scale(self.item_1, (56,45))

		self.item_2 = pygame.image.load("ressource/ether.png")
		self.item_2 = pygame.transform.scale(self.item_2, (56,45))
		self.item_2.set_colorkey((1,1,1))

		self.item_3 = pygame.image.load("ressource/tube_plastique1.png").convert_alpha()
		self.item_3 = pygame.transform.scale(self.item_3, (56,45)).convert_alpha()

	def refresh(self, map_player):
		self.window_screen.fill((0,0,0))
		for index_line, line in enumerate(map_player.map_list):
			for index_sprite, sprite in enumerate(line):
				position_px = (index_sprite * 56,index_line * 45)
				if sprite == 1:
					self.window_screen.blit(self.wall, position_px)

				elif sprite == 0:
					self.window_screen.blit(self.ground, position_px)

				elif sprite == 2:
					self.window_screen.blit(self.ground, position_px)
					self.window_screen.blit(self.player_display, position_px)

				elif sprite == 3:
					self.window_screen.blit(self.ground, position_px)
					self.window_screen.blit(self.jailer, position_px)

				elif sprite == 4:
					self.window_screen.blit(self.ground, position_px)
					self.window_screen.blit(self.item_1, position_px)
				elif sprite == 5:
					self.window_screen.blit(self.ground, position_px)
					self.window_screen.blit(self.item_2, position_px)
				elif sprite == 6:
					self.window_screen.blit(self.ground, position_px)
					self.window_screen.blit(self.item_3, position_px)

		pygame.display.flip()
