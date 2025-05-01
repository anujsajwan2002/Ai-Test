import numpy as np
import random
import matplotlib.pyplot as plt

# Define the fitness function
def fitness_function(x):
    return x * np.sin(10 * np.pi * x) + 1

# GA parameters
population_size = 20
generations = 100
mutation_rate = 0.1

# Create initial population
def create_population():
    return [random.uniform(0, 1) for _ in range(population_size)]

# Selection (tournament)
def select_parents(population):
    parents = []
    for _ in range(population_size):
        a, b = random.sample(population, 2)
        winner = a if fitness_function(a) > fitness_function(b) else b
        parents.append(winner)
    return parents

# Crossover (uniform)
def crossover(p1, p2):
    if random.random() < 0.5:
        return p1
    else:
        return p2

# Mutation
def mutate(x):
    if random.random() < mutation_rate:
        return x + random.uniform(-0.1, 0.1)
    return x

# GA main loop
population = create_population()
best_per_gen = []

for gen in range(generations):
    # Selection
    parents = select_parents(population)

    # Crossover and mutation
    new_population = []
    for i in range(0, population_size, 2):
        p1, p2 = parents[i], parents[i+1]
        child1 = mutate(crossover(p1, p2))
        child2 = mutate(crossover(p2, p1))
        new_population.extend([child1, child2])

    population = new_population[:population_size]
    best = max(population, key=fitness_function)
    best_per_gen.append(fitness_function(best))

# Final result
best_solution = max(population, key=fitness_function)
print(f"Best solution x = {best_solution:.5f}")
print(f"Maximum value f(x) = {fitness_function(best_solution):.5f}")

# Plotting performance
plt.plot(best_per_gen)
plt.title("Best Fitness Over Generations")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.grid(True)
plt.show()
