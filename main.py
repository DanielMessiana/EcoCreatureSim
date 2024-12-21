import numpy as np
import random as rand
import config, time, os, pygame

# <Game>
# ----------------------------------
# Runs the game loop in order to display the pygame application,
# ----------------------------------
class Game():
	# Constructor with main variables
	def __init__(self):
		# Main GUI variables
		pygame.init()
		self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
		self.clock = pygame.time.Clock()
		self.main = True

		# Screen variables
		from screens import TitleScreen, SimScreen
		self.titleScreen = TitleScreen(self.screen, self.clock)
		self.titleScreenOn = True
		self.simScreen = SimScreen(self.screen, self.clock)
		self.simScreenOn= False

	# Main game loop to run the world 
	def run(self):
		while self.main:
			self.screen.fill(config.WHITE)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.main = False
				elif event.type == pygame.MOUSEBUTTONDOWN and self.simScreenOn:
					if self.simScreen.pop_input.rect.collidepoint(event.pos):
						self.simScreen.pop_input.active = not self.simScreen.pop_input.active
					else:
						self.simScreen.pop_input.active = False
				elif event.type == pygame.KEYDOWN and self.simScreen.pop_input.active:
					if event.key == pygame.K_RETURN:
						self.population = int(self.simScreen.pop_input.input_text)
						self.simScreen.pop_input.input_text = ""
					elif event.key == pygame.K_BACKSPACE:
						self.simScreen.pop_input.input_text = self.simScreen.pop_input.input_text[:-1]
					else:
						self.simScreen.pop_input.input_text += event.unicode

			# Show title screen if it is on
			if self.titleScreenOn == True:
				self.titleScreen.display()
				if self.titleScreen.handle_input():
					self.titleScreenOn = False
					self.simScreenOn = True

			# Show simulation screen if it is on
			if self.simScreenOn == True:
				self.simScreen.display()

game = Game()
game.run()