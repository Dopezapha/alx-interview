#!/usr/bin/python3
"""N Queens Problem Solver"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and print the solutions"""
    board = [-1] * n
    solutions = []

    def solve(col):
        if col == n:
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return

        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                solve(col + 1)
                board[col] = -1

    solve(0)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
