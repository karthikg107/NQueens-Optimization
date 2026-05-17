import time
import tracemalloc

def is_safe(board, row, col):
    for r in range(row):
        c = board[r]

        # Same column
        if c == col:
            return False

        # Same diagonal
        if abs(r - row) == abs(c - col):
            return False

    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col):

            board[row] = col

            if solve(board, row + 1, n):
                return True

            board[row] = -1

    return False


def print_board(board, n):

    for row in range(n):

        line = ""

        for col in range(n):

            if board[row] == col:
                line += "Q "
            else:
                line += ". "

        print(line)


n = 30

board = [-1] * n

tracemalloc.start()

start = time.perf_counter()

if solve(board, 0, n):
    print_board(board, n)
else:
    print("No solution found")

end = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
print(f"\nTime taken: {end - start:.6f} seconds")
print(f"Peak Memory Usage: {peak / 1024:.2f} KB")