class Item():
	def __init__(self, value,name, map_player):
		self.position_index_x, self.position_index__y = map_player.random_position()
		self.value = value
		self.name = name
		self.item_rect = pygame.Rect(self.position_index_x*56,position_index__y*45,56,45)