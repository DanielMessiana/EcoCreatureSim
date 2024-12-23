import numpy as np
# <World>
# ----------------------------------
# A World object will depict and hold creatures in a world for them to act
# as agents in and explore and learn from.
# ----------------------------------
class World():
	def __init__(self, grid_size, screen):
		self.grid_size = grid_size
		self.grid = np.full((grid_size, grid_size), None)
		self.screen = screen
		#self.creatures = creatures

	def drawWorld(self):
		cell_size = min(config.SCREEN_WIDTH, config.SCREEN_HEIGHT) // self.grid_size
		for x in range(self.grid_size):
			for y in range(self.grid_size):
				rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
				color = config.LIGHT_GREY if self.grid[x, y] is None else config.BLUE
				pygame.draw.rect(self.screen, color, rect)
				pygame.draw.rect(self.screen, config.BLACK, rect, 1)

	def updateWorld(self):
		for creature in creatures:
			creature.update()
