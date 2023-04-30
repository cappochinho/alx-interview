#!/usr/bin/python3
"""Nqueens: Chess Problem"""


import sys


def is_viable(board, row, col):
    """
    Checks if a row or column isn't already occupied
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def soln_nqueens(board, row, n, solutions):
    """Placing all queens"""

    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_viable(board, row, col):
            board[row] = col
            soln_nqueens(board, row + 1, n, solutions)


def print_solution(solution):
    """Prints the solution"""

    n = len(solution)
    solution_list = []
    for row in range(n):
        solution_list.append([row, solution[row]])
    print(solution_list)


def nqueens(n):
    """Main function"""

    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []

    soln_nqueens(board, 0, n, solutions)

    for solution in solutions:
        print_solution(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
