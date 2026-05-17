import random
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


# Hill Climbing with Random Restart
def hill_climbing(n, max_restarts=500):

    for restart in range(max_restarts):

        print(f"Restart Attempt: {restart + 1}")

        # Generate random board
        board = [random.randint(0, n - 1) for _ in range(n)]

        current_conflicts = conflicts(board)

        while current_conflicts > 0:

            best_board = board[:]
            best_conflicts = current_conflicts

            # Try moving every queen
            for row in range(n):

                original_col = board[row]

                for col in range(n):

                    if col == original_col:
                        continue

                    board[row] = col

                    new_conflicts = conflicts(board)

                    # Better board found
                    if new_conflicts < best_conflicts:

                        best_conflicts = new_conflicts
                        best_board = board[:]

                # Restore original position
                board[row] = original_col

            # Local optimum reached
            if best_conflicts == current_conflicts:

                print("Stuck in local optimum. Restarting...\n")
                break

            board = best_board
            current_conflicts = best_conflicts

        # Solution found
        if current_conflicts == 0:

            print(f"\nSolution found after {restart + 1} restart(s)")

            return board

    return None


# =========================
# MAIN PROGRAM
# =========================

n = 100

tracemalloc.start()

start = time.perf_counter()

solution = hill_climbing(n)

end = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()


# Print Result
if solution:

    print("\nFinal Solution Board:\n")

    print_board(solution)

    print("\nConflicts:", conflicts(solution))

else:

    print("\nNo solution found")


# Performance Output
print(f"\nTime Taken: {end - start:.6f} seconds")

print(f"Peak Memory Usage: {peak / 1024:.2f} KB")