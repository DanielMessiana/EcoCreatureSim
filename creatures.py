

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