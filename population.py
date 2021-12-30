from dna import DNA
import random


def translate(value, left_min, left_max, right_min, right_max):
    """
    this function is a simple mapping helper function.
    it maps a range of values to another range of values
    """
    # Figure out how 'wide' each range is
    left_span = left_max - left_min
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (float)
    value_scaled = float(value - left_min) / float(left_span)

    # Convert the 0-1 range into a value in the right range.
    return right_min + (value_scaled * right_span)


class Population:
    def __init__(self, target, mutation_chance, num):
        self.population = []
        self.target = target
        self.mutationChance = mutation_chance

        for i in range(num):
            self.population.append(DNA(len(target)))

        self.calc_fitness()
        self.mating_pool = []
        self.finished = False
        self.generations = 0
        self.perfect_score = int(len(target) ** 2)

    def calc_fitness(self):
        # calculate the fitness of all creatures of this generation
        for i in range(len(self.population)):
            self.population[i].calc_fitness(self.target)

    def natural_selection(self):
        # compare fitness values of creatures
        # create a new generation based of the best creatures genes combined into new ones
        self.mating_pool = []

        max_fitness = 0

        for i in range(len(self.population)):
            if self.population[i].fitness > max_fitness:
                max_fitness = self.population[i].fitness

        for i in range(len(self.population)):
            fitness = translate(self.population[i].fitness, 0, max_fitness, 0, 1)
            n = int(fitness * 100)
            for j in range(n):
                self.mating_pool.append(self.population[i])

    def generate(self):
        # create a new generation of creatures based on the outcomes of natural selection
        for i in range(len(self.population)):
            partner_a = random.choice(self.mating_pool)
            partner_b = random.choice(self.mating_pool)
            child = partner_a.crossover(partner_b)
            child.mutate(self.mutationChance)
            self.population[i] = child
        self.generations += 1

    def get_best(self):
        # find the creature with the highest fitness of this generation
        best_fitness = 0
        index = 0
        for i in range(len(self.population)):
            if self.population[i].fitness > best_fitness:
                index = i
                best_fitness = self.population[i].fitness
        if best_fitness == self.perfect_score:
            self.finished = True
        return self.population[index].get_phrase()

    def get_average_fitness(self):
        # get the average fitness of creatures in this generation
        total = 0
        for i in range(len(self.population)):
            total += self.population[i].fitness
        return total / len(self.population)

    def all_phrases(self):
        # get the generated string off all creatures combined in this generation
        phrases = ""
        display_limit = len(self.population) if len(self.population) < 50 else 50

        for i in range(display_limit):
            phrases += f"{self.population[i].get_phrase()}\n"

        return phrases
