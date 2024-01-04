#!/usr/bin/python3
"""N-queens problem solver."""


import sys


def print_solution(solution):
    """Print chessboard representation of a solution."""
    print("[", end="")
    for i in range(len(solution)):
        print("[{}, {}]".format(i, solution[i]), end="")
        if i < len(solution) - 1:
            print(", ", end="")
    print("]")


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if (
                board[i] == row or
                board[i] - i == row - col or
                board[i] + i == row + col
                ):
            return False
    return True


def solve_nqueens(board, col, n):
    """Solve N-queens using backtracking."""
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(board, col + 1, n)


def nqueens(n):
    """Initiate N-queens solving."""
    if not isinstance(n, int):
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
