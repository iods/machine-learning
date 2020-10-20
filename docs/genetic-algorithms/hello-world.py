# ===================================================================
#
# A simple genetic algorithm that evolves the string Hello, World
#
# ===================================================================

from random import ( randint, choice )

TARGET = "Hello, World"

class Chromosome:
    def __init__(self, gene):
        self.gene = gene

    def fitness(self): return self.cost(TARGET)

    def mate(self, chromosome):
        """ A way to combine together two chromosomes """
        pivot = randint(0, len(self.gene) - 1)
        x = self.gene[:pivot] + chromosome.gene[pivot:]
        y = chromosome.gene[:pivot] + self.gene[pivot:]
        return Chromosome(x), Chromosome(y)

    def random_from_genepool(self):
        return chr(randint(32, 121))

    def cost(self, target):
        """ Returns the cost fnction of this chromosome compared to some other target """
        value = 0
        for (x,y) in zip(self.gene, target):
            difference = ord(x) - ord(y)
            value += difference ** 2
        return value

    def mutate(self):
        """ Returns a mutated copy of an existing Chromosome"""
        gene = list(self.gene)
        idx = randint(0, len(gene) - 1)
        gene[idx] = self.random_from_genepool()
        return Chromosome(''.join(gene))

def random_chromosome(size):
    result = []
    for i in range(0, size):
        random_char = chr(randint(32, 121))
        result.append(random_char)
    return Chromosome(''.join(result))

class Population:
    def __init__(self, size, elitism = 5):
        self.size = size
        self.elitism = elitism
        self.members = Population.spawn(size, len(TARGET))

    def sorted_by_fitness(self):
        """ Return all members of the population sorted by fitness (cost function) """
        return list(sorted(self.members, key=lambda x: x.fitness()))

    def select_fittest(self):
        """ Select only the n fittest members of the population """
        self.members = self.sorted_by_fitness()[:self.elitism]

    def add_member(self, member):
        self.members = self.members + [member]

    def evolve(self):
        spawn = []
        (first_parent, second_parent) = self.sorted_by_fitness()[0:2]
        (first_child, second_child) = first_parent.mate(second_parent)
        self.select_fittest()
        self.add_member(first_child)
        self.add_member(second_child)
        self.add_member(first_child.mutate())
        self.add_member(second_child.mutate())
        self.add_member(first_parent.mutate())
        self.add_member(second_parent.mutate())
        return self.members

    @staticmethod
    def spawn(n, gene_size):
        """ Spawn a new population """
        population = []
        for i in range(n):
            population.append(random_chromosome(gene_size))
        return population

# =============================================================================

def run():
    population = Population(100)
    fittest = population.sorted_by_fitness()[0]
    generations = 0
    while fittest.gene != TARGET:
        population.evolve()
        fittest = population.sorted_by_fitness()[0]
        generations += 1
        print(fittest.gene)
    print("Evolution succeeded after %i generations" % generations)
