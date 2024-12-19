import numpy as np
import random as rand
import time, os

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
# One Creature object has a Gene object and a Loc object
# ----------------------------------
class Creature():
	def setGene(self, gene):
		self.gene = gene

	def setLoc(self, loc):
		self.loc = loc

# <CreatureBuilder>
# ----------------------------------
# The CreatureBuilder creates a creature object
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