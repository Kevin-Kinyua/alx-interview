#!/usr/bin/python3
"""N Queens"""

import sys

def is_safe(board, row, col, n):
    # Check if no queen can attack this position
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        return

    def print_solution(board):
        for row in board:
            print("".join(["Q" if cell else "." for cell in row]))

    def solve(board, col):
        if col == n:
            print_solution(board)
            print()
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
