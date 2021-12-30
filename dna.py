import string
import random


def get_random_char():
    chars = [char for char in string.printable]
    return random.choice(chars)


class DNA:
    def __init__(self, num):
        self.fitness = 0
        self.genes = [get_random_char() for _ in range(num)]

    def get_phrase(self):
        # get the string the genes would form (output of creature)
        return ''.join(self.genes.copy())

    def calc_fitness(self, target):
        # calculate how well this dna is doing
        score = 0
        for index, gene in enumerate(self.genes):
            if gene == target[index]:
                score += 1
        self.fitness = score**2

    def crossover(self, partner_dna):
        # use partner dna to return a child consisting of both this and the other genes
        child = DNA(len(self.genes))
        midpoint = random.randint(0, len(self.genes))

        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner_dna.genes[i]
        return child

    def mutate(self, mutation_rate):
        # mutate each gene based on chance (randomize it)
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = get_random_char()
