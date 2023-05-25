import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

# Define the equation system
def equation_system(x, y, v, t):
    f = 0.36
    h = 0.0
    m = 0.02

    dx_dt = f * x - x * v
    dy_dt = x * v - y
    dv_dt = y - m * x * v - h * v

    return dx_dt, dy_dt, dv_dt

# Define the fitness function
def fitness_function(solution):
    dimension = len(solution) // 3
    t = np.linspace(0, 20, num=dimension)
    x, y, v = solution[:dimension], solution[dimension:2*dimension], solution[2*dimension:]

    dx_dt, dy_dt, dv_dt = equation_system(x, y, v, t)
    fitness = np.sum(dx_dt**2+ dy_dt**2 + dv_dt**2)

    return fitness

# Genetic Algorithm implementation
def genetic_algorithm(population_size, num_generations, dimension):
    num_variables = 3 * dimension
    bounds = np.array([0, 1])  # Adjust the bounds based on the problem's constraints

    rng = default_rng()
    population = rng.uniform(bounds[0], bounds[1], size=(population_size, num_variables))

    best_fitness = np.inf
    best_solution = None

    for generation in range(num_generations):
        fitness_values = np.zeros(population_size)
        for i in range(population_size):
            fitness_values[i] = fitness_function(population[i])

        min_fitness_index = np.argmin(fitness_values)
        if fitness_values[min_fitness_index] < best_fitness:
            best_fitness = fitness_values[min_fitness_index]
            best_solution = population[min_fitness_index]

        parents = population[np.argsort(fitness_values)[:2]]

        # Crossover
        offspring = np.zeros_like(parents)
        for j in range(num_variables):
            alpha = rng.uniform(0, 1)
            offspring[0, j] = alpha * parents[0, j] + (1 - alpha) * parents[1, j]
            offspring[1, j] = (1 - alpha) * parents[0, j] + alpha * parents[1, j]

        # Mutation
        mutation_rate = 0.05  # Adjust the mutation rate as needed
        for j in range(2):
            for k in range(num_variables):
                if rng.uniform(0, 1) < mutation_rate:
                    offspring[j, k] = rng.uniform(bounds[0], bounds[1])

        population = np.vstack((population, offspring))

    return best_solution

# Solve the nonlinear equation system using Genetic Algorithm
population_size = 1000
num_generations = 250
dimension = 20

solution = genetic_algorithm(population_size, num_generations, dimension)

# Plot the solutions
t = np.linspace(0, 20, num=dimension)
x, y, v = solution[:dimension], solution[dimension:2*dimension], solution[2*dimension:]

plt.plot(t, x, label='x')
plt.plot(t, y, label='y')
plt.plot(t, v, label='v')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Solution of the Nonlinear Equation System')
plt.show()
