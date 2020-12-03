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

    for i in range(0,len(extended_grid),movement[1]):
        if extended_grid[i][start] == '#':
            trees += 1
        start += movement[0]

    return trees


movements = [[1,1],[3,1],[5,1],[7,1],[1,2]]
answer = []

for moves in movements:
    answer.append(tree_counter(moves, grid))

final_answer = 1
for ans in answer:
    final_answer *= ans

print(final_answer)