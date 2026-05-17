import random
import time
import tracemalloc


# Count conflicts
def conflicts(board):

    n = len(board)

    count = 0

    for i in range(n):

        for j in range(i + 1, n):

            if board[i] == board[j]:

                count += 1

            elif abs(board[i] - board[j]) == abs(i - j):

                count += 1

    return count


# Fitness function
def fitness(board):

    return 1 / (1 + conflicts(board))


# Create random board
def random_board(n):

    return [random.randint(0, n - 1) for _ in range(n)]


# Selection
def selection(population):

    tournament = random.sample(population, 5)

    tournament.sort(key=fitness, reverse=True)

    return tournament[0]


# Crossover
def crossover(parent1, parent2):

    n = len(parent1)

    point = random.randint(1, n - 2)

    child = parent1[:point] + parent2[point:]

    return child


# Mutation
def mutation(board, mutation_rate=0.05):

    n = len(board)

    for i in range(n):

        if random.random() < mutation_rate:

            board[i] = random.randint(0, n - 1)

    return board


# Print board
def print_board(board):

    n = len(board)

    for row in range(n):

        line = ""

        for col in range(n):

            if board[row] == col:
                line += "Q "
            else:
                line += ". "

        print(line)


# Genetic Algorithm
def genetic_algorithm(
    n,
    population_size=30,
    generations=200
):

    # Initial population
    population = [
        random_board(n)
        for _ in range(population_size)
    ]

    for generation in range(generations):

        # Sort by fitness
        population.sort(
            key=fitness,
            reverse=True
        )

        best = population[0]

        best_conflicts = conflicts(best)

        # Progress
        if generation % 50 == 0:

            print(
                f"Generation: {generation} | "
                f"Conflicts: {best_conflicts}"
            )

        # Solution found
        if best_conflicts == 0:

            print(
                f"\nSolution found in generation {generation}"
            )

            return best, generation

        new_population = []

        # Elitism
        new_population.extend(population[:10])

        while len(new_population) < population_size:

            parent1 = selection(population)

            parent2 = selection(population)

            child = crossover(parent1, parent2)

            child = mutation(child)

            new_population.append(child)

        population = new_population

    return population[0], generations


# =========================
# MAIN PROGRAM
# =========================

n = 500

tracemalloc.start()

start = time.perf_counter()

solution, generations_used = genetic_algorithm(n)

end = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()

final_conflicts = conflicts(solution)


# Output
if final_conflicts == 0:

    print("\nPerfect Solution Found!\n")

else:

    print("\nNear Optimal Solution Found\n")

print(f"Final Conflicts: {final_conflicts}")

print(f"Generations Used: {generations_used}")

print(f"\nTime Taken: {end - start:.6f} seconds")

print(f"Peak Memory Usage: {peak / 1024:.2f} KB")