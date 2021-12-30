from population import Population

target_str = "This is the target."
popCount = 500
mutationChance = 0.01


def main():
    population = Population(target=target_str, mutation_chance=mutationChance, num=popCount)

    while not population.finished:
        population.natural_selection()
        population.generate()
        population.calc_fitness()
        print(population.get_best())

    print(f"This took {population.generations} generations to accomplish.")


if __name__ == '__main__':
    main()
