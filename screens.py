import config, pygame

# <Text>
# ----------------------------------
# A text class to be displayed on screen, it also allows easy creation of new
# text boxes.
# ----------------------------------
class Text():
	def __init__(self, text, position, size, font, screen):
		self.text = text
		self.position = position
		self.size = size
		self.font = font
		self.screen = screen

		self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
		self.text_surface = font.render(text, True, config.BLACK)

	def draw(self):
		# Draw text box
		text_rect = self.text_surface.get_rect(center=self.rect.center)
		self.screen.blit(self.text_surface, text_rect)

	def setText(self, text):
		self.text = text
		self.text_surface = font.render(text, True, config.BLACK)

# <InputBox
# ----------------------------------
# An input box class to be displayed on screen
# ----------------------------------
class InputBox():
	def __init__(self, position, size, font, input_text, screen):
		self.position = position
		self.size = size
		self.font = font
		self.input_text = input_text
		self.active = False
		self.screen = screen

		self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
		self.input_surface = self.font.render(self.input_text, True, config.BLACK)

	def draw(self):
		self.input_surface = self.font.render(self.input_text, True, config.BLACK)
		# Draw input box
		pygame.draw.rect(self.screen, config.BLACK, self.rect, 2)
		input_rect = self.input_surface.get_rect(center=self.rect.center)
		self.screen.blit(self.input_surface, input_rect)

# <Button>
# ----------------------------------
# A button class to be displayed on screen, it also allows easy creation of new
# buttons.
# ----------------------------------
class Button():
	def __init__(self, text, position, size, font, color, hover_color, screen):
		self.text = text
		self.position = position
		self.size = size
		self.font = font
		self.color = color
		self.hover_color = hover_color
		self.screen = screen

		self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
		self.text_surface = font.render(text, True, config.BLACK)

	def draw(self):
		# Detect hover
		mouse_pos = pygame.mouse.get_pos()
		is_hovered = self.rect.collidepoint(mouse_pos)
		current_color = self.hover_color if is_hovered else self.color

		# Draw button and text
		pygame.draw.rect(self.screen, current_color, self.rect)
		text_rect = self.text_surface.get_rect(center=self.rect.center)
		self.screen.blit(self.text_surface, text_rect)

	def is_clicked(self):
		mouse_pos = pygame.mouse.get_pos()
		mouse_click = pygame.mouse.get_pressed()
		return self.rect.collidepoint(mouse_pos) and mouse_click[0]

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
		self.titletext = Text(
			text="Eco Creature Simulator",
			position=(config.SCREEN_WIDTH // 2 - 100, 100),
			size=(200, 50),
			font=config.FONT_LARGE,
			screen=self.screen
		)

		# Start button
		self.start_button = Button(
			text="Start",
			position=(config.SCREEN_WIDTH // 2 - 100, config.SCREEN_HEIGHT // 2),
			size=(200, 50),
			font=config.FONT_MEDIUM,
			color=config.GREEN,
			hover_color=config.GREEN_HOVER,
			screen=self.screen
		)

	def display(self):
		self.titletext.draw()
		self.start_button.draw()
		pygame.display.flip()
		self.clock.tick(30)

	def handle_input(self):
		return self.start_button.is_clicked()

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
		self.simOn = False

		# Population set text field
		self.pop_input = InputBox(
			position=(config.SCREEN_WIDTH // 2 - 200, config.SCREEN_HEIGHT // 2 - 300),
			size=(100, 50),
			font=config.FONT_MEDIUM,
			input_text="50",
			screen=self.screen
		)

		# Run Simulation button
		self.run_button = Button(
			text="Run simulation",
			position=(config.SCREEN_WIDTH // 2 - 100, config.SCREEN_HEIGHT // 2),
			size=(200, 50),
			font=config.FONT_MEDIUM,
			color=config.GREEN,
			hover_color=config.GREEN_HOVER,
			screen=self.screen
		)



	def initialize_creatures(self, population):
		from creatures import CreatureBuilder, Gene, Genome



	def display(self):
		if not self.simOn:
			self.run_button.draw()
			self.pop_input.draw()
		elif self.simOn:


		pygame.display.flip()
		self.clock.tick(30)