#!/usr/bin/python3
"""
    Printing Pascal's main_list
"""


def pascal_triangle(n):
    """ Return Pascal's main_list of n """

    if (n <= 0):
        return []

    main_list = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(main_list[i-1][j-1] + main_list[i-1][j])
        row.append(1)
        main_list.append(row)

    return main_list
