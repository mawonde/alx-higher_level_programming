#!/usr/bin/python3

"""
This module contains an algorithm that solves the N-Queen puzzle using backtracking.
"""


def isSafe(m_queen, nqueen):
    """
    Determines if the queens can or can't attack each other.

    Args:
        m_queen (list): Array that contains the positions of the queens.
        nqueen (int): The index of the queen being placed.

    Returns:
        bool: True if the queens can't attack each other, False otherwise.
    """

    for i in range(nqueen):
        if m_queen[i] == m_queen[nqueen]:
            return False

        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

    return True


def print_result(m_queen, nqueen):
    """
    Prints the list with the positions of the queens.

    Args:
        m_queen (list): Array that contains the positions of the queens.
        nqueen (int): The total number of queens.
    """

    res = []

    for i in range(nqueen):
        res.append([i, m_queen[i]])

    print(res)


def Queen(m_queen, nqueen):
    """
    Recursive function that executes the backtracking algorithm to solve the N-Queen puzzle.

    Args:
        m_queen (list): Array that contains the positions of the queens.
        nqueen (int): The index of the queen being placed.
    """

    if nqueen == len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    while m_queen[nqueen] < len(m_queen) - 1:

        m_queen[nqueen] += 1

        if isSafe(m_queen, nqueen):

            if nqueen != len(m_queen):
                Queen(m_queen, nqueen + 1)


def solveNQueen(size):
    """
    Invokes the backtracking algorithm to solve the N-Queen puzzle.

    Args:
        size (int): The size of the chessboard and the number of queens.
    """

    m_queen = [-1 for _ in range(size)]

    Queen(m_queen, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueen(size)

