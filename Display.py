import pygame

# class which contains attributes and methods linked with display
class Display(object):
	def __init__(self):
		pygame.init()
		self.resolution = (840,675) #size of the window
		self.window_screen = pygame.display.set_mode(self.resolution) # instantiation of a surface object 

	def load_wall(self):
		wall_sheet = pygame.image.load("ressource/structures.png") # we load the image and transform it into a surface object
		self.wall = wall_sheet.subsurface(40,140,40,20) # we only want a part of the image
		self.wall = pygame.transform.scale(self.wall,(56,45)) # resizing the surface
	# idem for the ground
	def load_ground(self):
		ground_sheet = pygame.image.load("ressource/floor-tiles-20x20.png")
		self.ground = ground_sheet.subsurface(320,0,20,20)
		self.ground = pygame.transform.scale(self.ground, (56,45))
	#idem for the player
	def load_player_display(self):
		self.player_display = pygame.image.load("ressource/MacGyver.png")
		self.player_display = pygame.transform.scale(self.player_display, (56,45))
	#idem for the jailer
	def load_jailer(self):
		self.jailer = pygame.image.load("ressource/Gardien.png")
		self.jailer = pygame.transform.scale(self.jailer, (56,45))
	# idem for items 
	def load_items(self):
		self.item_1 = pygame.image.load("ressource/aiguille.png")
		self.item_1 = pygame.transform.scale(self.item_1, (56,45))

		self.item_2 = pygame.image.load("ressource/ether.png")
		self.item_2 = pygame.transform.scale(self.item_2, (56,45))
		self.item_2.set_colorkey((1,1,1))

		self.item_3 = pygame.image.load("ressource/tube_plastique1.png").convert_alpha()
		self.item_3 = pygame.transform.scale(self.item_3, (56,45)).convert_alpha()
	# method the class will use when something change on the map (the player moves, the player retrieves an item,... )

	# method that "blit" a surface on another surface
	def display_surfaces(self,first_surface,second_surface,position):
		self.window_screen.blit(first_surface,position)
		self.window_screen.blit(second_surface,position)

	def refresh(self, map_player):
		surfaces_list = [self.ground,self.wall,self.player_display,self.jailer,self.item_1,self.item_2,self.item_3] # list that contains all the surfaces the program needs
		value_display = [0,1,2,3,4,5,6] # values in the map_list
		self.window_screen.fill((0,0,0))
		for index_line, line in enumerate(map_player.map_list):
			for index_sprite, sprite in enumerate(line): # analysis of the map list
				position_px = (index_sprite * 56,index_line * 45) # position in pixels
				for index_value, value in enumerate(value_display): 
					if value == sprite:
						self.display_surfaces(self.ground,surfaces_list[index_value],position_px)

		pygame.display.flip() # method that updates display



