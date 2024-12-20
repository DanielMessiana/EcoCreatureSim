import numpy as np
import random as rand
import time, os, pygame, config

# <Genome> 
# ----------------------------------
# A Genome object is comprised of an arbitrary # of letters, 5 for now.
# The letters will influence the behavior/actions of the
# animal and what physical traits it displays. 
# ----------------------------------
class Genome():
	def __init__(self, letters):
		self.instructions = letters

	def getInstructions(self):
		print(self.instructions)
		#return self.instructions

# <Gene>
# ----------------------------------
# One Gene object is made up of multiple Genome objects. Each animal
# will have one type of DNA that they can pass on to offspring.
# ----------------------------------
class Gene():
	# genomes -> np array of genome objects
	def __init__(self, genomes):
		self.genomes = genomes

	def getGene(self):
		for gene in self.genomes:
			gene.getInstructions()

# <Loc>
# ----------------------------------
# One Loc object is made up of three variables, an x and y coordinate to 
# designate a creatures location on the map, and a direction to indicate 
# the direction it is facing.
# ----------------------------------
class Loc():
	def __init__(self, coordinates, direction):
		self.coordinates = coordinates
		self.direction = direction

# <Creature>
# ----------------------------------
# One Creature object has a Gene object and a Loc object. These will be the
# subject of the simulation.
# ----------------------------------
class Creature():
	def setGene(self, gene):
		self.gene = gene

	def setLoc(self, loc):
		self.loc = loc

# <CreatureBuilder>
# ----------------------------------
# The CreatureBuilder creates a creature object step by step, allowing for 
# specification of attributes
# ----------------------------------
class CreatureBuilder():
	def __init__(self):
		self.creature = Creature()

	def buildGene(self, gene):
		self.creature.setGene(gene)

	def buildLoc(self, loc):
		self.creature.setLoc(loc)

	def getCreature(self):
		return self.creature

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

			if self.titleScreenOn == True:
				self.titleScreen.display()

g1 = Genome(np.array(["A", "B", "C", "D", "E"]))
g2 = Genome(np.array(["B", "C", "D", "E", "A"]))
g3 = Genome(np.array(["C", "D", "E", "A", "B"]))
g4 = Genome(np.array(["D", "E", "A", "B", "C"]))
g5 = Genome(np.array(["E", "A", "B", "C", "D"]))

Gene1 = Gene(np.array([g1, g2, g3]))

cBuilder = CreatureBuilder()
cBuilder.buildGene(Gene1)
c1 = cBuilder.getCreature()
c1.gene.getGene()

game = Game()
game.run()