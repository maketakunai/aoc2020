#!/usr/bin/env python3

with open('./11_input.txt') as input_file:
    seat_layout = input_file.read().splitlines()

def check_adj(coords, layout, row):
    y = coords[0]
    x = coords[1]
    occ = 0
    neighbors = [(y-1, x), (y-1, x+1), (y, x+1), (y+1, x+1), (y+1, x), (y+1, x-1), (y, x-1), (y-1, x-1)]
    for (b,a) in neighbors:
        if 0 <= b < len(layout) and 0 <= a < len(layout[b]):
            if layout[b][a] == '#':
                occ += 1
    if layout[y][x] == 'L' and occ == 0:
        row.append('#')
    elif layout[y][x] == '#' and occ >= 4:
        row.append('L')
    elif layout[y][x] == '.':
        row.append('.')
    else:
        row.append(layout[y][x])

def create_next(cur_layout):
    next_layout = []

    for y in range(0,len(cur_layout)):
        row = []
        for x in range(0,len(cur_layout[y])):
            check_adj([y,x], cur_layout, row)
        next_layout.append(''.join(row))
    return next_layout

prv = seat_layout.copy()
nxt = create_next(seat_layout)

while prv != nxt:
    prv = nxt.copy()
    nxt = create_next(prv)

occupied = 0
for i in range(0,len(prv)):
    for j in range(0,len(prv[i])):
        if prv[i][j] == '#':
            occupied +=1

print(occupied)