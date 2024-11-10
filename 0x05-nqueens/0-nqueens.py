#!/usr/bin/python3
"""
The N-Queens Solver program finds all possible ways to place N queens on an N×N chessboard such that no two queens threaten each other. Using backtracking, it places queens row by row, ensuring they don’t share the same column
"""

import sys


def print_solutions(n, board):
    
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                solution.append([i, j])
    print(solution)

def is_safe(board, row, col):
   
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row, board):
   
    if row == n:
        print_solutions(n, board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board)

def main():
   
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

    board = [-1] * n  
    solve_nqueens(n, 0, board)

if __name__ == "__main__":
    main()

