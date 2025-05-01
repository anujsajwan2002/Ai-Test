import random

# function to optimize for x**2
def fitness(x):
    return x ** 2

# Create an individual
def create_individual():
    return random.uniform(-10, 10)  # Real-valued individual between -10 and 10

# Mutation function
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        individual += random.uniform(-1, 1)
    return individual

# Crossover between two individuals
def crossover(parent1, parent2):
    return (parent1 + parent2) / 2

# Genetic algorithm
def genetic_algorithm(pop_size=20, generations=50):
    population = [create_individual() for _ in range(pop_size)]

    for gen in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        print(f"Generation {gen}: Best = {population[0]}, Fitness = {fitness(population[0])}")

        # Select the top 50% as parents
        parents = population[:pop_size // 2]

        # Create the next generation
        next_gen = parents.copy()
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(parents, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            next_gen.append(child)

        population = next_gen

    return population[0]

best = genetic_algorithm()
print(f"\nBest solution found: x = {best}, f(x) = {best**2}")
