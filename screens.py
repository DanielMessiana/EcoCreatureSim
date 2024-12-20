import pygame

# <TitleScreen>
# ----------------------------------
# Displays the title screen, which will allow the user to start the 
# simulation.
# ----------------------------------
class TitleScreen():
	def __init__(self, screen, clock):
		# Main GUI variables from game
		self.screen = screen
		self.clock = clock

		# Title text
		self.titletext = config.FONT_LARGE.render("Eco Creature Simulator", True, config.LIGHT_GREY)
		self.titletextRect = self.titletext.get_rect(center=(config.SCREEN_WIDTH / 1.18, 100))

		# Start button


	def display(self):
		self.screen.blit(self.titletext, self.titletextRect)

		pygame.display.flip()
		self.clock.tick(30)

# <SimScreen>
# ----------------------------------
# Displays the simulation screen, which will allow the user to see the 
# simulation.
# ----------------------------------
class SimScreen():
	def __init__(self, screen, clock):
		# Main GUI variables from game
		self.screen = screen
		self.clock = clock

	def display(self):

		pygame.display.flip()
		self.clock.tick(30)