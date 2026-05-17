import random
import math
import time
import tracemalloc


# Count attacking queen pairs
def conflicts(board):

    n = len(board)

    count = 0

    for i in range(n):

        for j in range(i + 1, n):

            # Same column
            if board[i] == board[j]:
                count += 1

            # Same diagonal
            elif abs(board[i] - board[j]) == abs(i - j):
                count += 1

    return count


# Print chess board
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


# Simulated Annealing Algorithm
def simulated_annealing(n):

    # Random initial board
    board = [random.randint(0, n - 1) for _ in range(n)]

    current_conflicts = conflicts(board)

    # Initial temperature
    temperature = 100

    # Cooling rate
    cooling_rate = 0.99

    step = 0

    while temperature > 0.1 and current_conflicts > 0:

        step += 1

        # Create neighbor board
        new_board = board[:]

        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)

        new_board[row] = col

        new_conflicts = conflicts(new_board)

        delta = new_conflicts - current_conflicts

        # Better solution
        if delta < 0:

            board = new_board
            current_conflicts = new_conflicts

        else:

            # Accept worse solution with probability
            probability = math.exp(-delta / temperature)

            if random.random() < probability:

                board = new_board
                current_conflicts = new_conflicts

        # Cool down
        temperature *= cooling_rate

        # Progress output every 1000 steps
        if step % 1000 == 0:

            print(
                f"Step: {step} | "
                f"Temperature: {temperature:.4f} | "
                f"Conflicts: {current_conflicts}"
            )

    return board, current_conflicts, step


# =========================
# MAIN PROGRAM
# =========================

n = 200

tracemalloc.start()

start = time.perf_counter()

solution, final_conflicts, steps = simulated_annealing(n)

end = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()


# Output
if final_conflicts == 0:

    print("\nSolution Found!\n")

    print_board(solution)

else:

    print("\nBest Solution Reached (not perfect)\n")

    print_board(solution)

print(f"\nFinal Conflicts: {final_conflicts}")

print(f"Total Steps: {steps}")

print(f"\nTime Taken: {end - start:.6f} seconds")

print(f"Peak Memory Usage: {peak / 1024:.2f} KB")