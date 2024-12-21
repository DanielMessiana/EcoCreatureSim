# <Genome> 
# ----------------------------------
# A Genome object is comprised of an arbitrary # of letters, 5 for now.
# The letters will influence the behavior/actions of the
# animal and what physical traits it displays. 
# ----------------------------------
class Genome():
	def setInstructions(self, instructions):
		self.instructions = instructions

	def getInstructions(self):
		return self.instructions

# <GenomeBuilder> 
# ----------------------------------
# The GenomeBuilder object creates a Genome object step by step, allowing  
# for specification of Genomes
# ----------------------------------
class GenomeBuilder():
	def __init__(self):
		self.genome = Genome()

	def buildInstructions(self, instructions):

# <Gene>
# ----------------------------------
# One Gene object is made up of multiple Genome objects. Each animal
# will have one type of DNA that they can pass on to offspring.
# ----------------------------------
class Gene():
	def setGenomes(self, genomes):
		self.genomes = genomes

	def getGenomes(self):
		return self.genomes

# <GeneBuilder>
# ----------------------------------
# The GeneBuilder object creates a Gene object step by step, allowing  
# for specification of Genomes
# ----------------------------------
class GeneBuilder():
	def __init__(self):
		self.gene = Gene()
		self.genomeBuilder = GenomeBuilder()

	def buildGeneomes(self, genomes):
		self.gene.setGenomes(genomes)

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
# The CreatureBuilder object creates a Creature object step by step, allowing  
# for specification of attributes
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