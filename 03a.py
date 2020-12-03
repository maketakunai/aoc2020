#!/usr/bin/env python3
import math

with open('./03_input.txt') as input_file:
    grid = input_file.read().splitlines()

def tree_counter(movement, grid):
    steps = len(grid) - 1
    width = steps * movement[0]
    dupes_needed = math.ceil(width / len(grid[0]))

    extended_grid = []
    for row in grid:
        row = row * dupes_needed
        extended_grid.append(row)

    start = 0
    trees = 0
    for row in extended_grid:
        if row[start] == '#':
            trees += 1
        start += movement[0]

    return trees

ans = tree_counter([3,1], grid)
print(ans)