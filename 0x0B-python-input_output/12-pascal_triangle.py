#!/usr/bin/python3
def pascal_triangle(n):
    """ Returns the Pascal's triangle as a matrix

    Args:
        n: The number of lines in the Pascal's triangle.

    Returns:
        matrix: A matrix representing the Pascal's triangle.

    """

    matrix = []
    prev = []

    for i in range(n):
        res_list = []
        p1 = -1
        p2 = 0
        for j in range(len(prev) + 1):
            if p1 == -1 or p2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[p1] + prev[p2]]
            p1 += 1
            p2 += 1
        matrix.append(res_list)
        prev = res_list[:]

    return matrix

