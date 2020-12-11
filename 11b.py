#!/usr/bin/env python3

with open('./11_input.txt') as input_file:
    seat_layout = input_file.read().splitlines()

def check_adj(coords, layout, row):
    y = coords[0]
    x = coords[1]
    occ = 0
    neighbors = [(-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1), (-1, -1)]
    for (b,a) in neighbors:
        dead_end = 0
        b_new = y+b
        a_new = x+a
        if b_new < 0 or b_new >= len(layout) or a_new < 0 or a_new >= len(layout[b_new]):
                dead_end = 1
        while dead_end != 1 and layout[b_new][a_new] == '.':
            b_new += b
            a_new += a
            if b_new < 0 or b_new >= len(layout) or a_new < 0 or a_new >= len(layout[b_new]):
                dead_end = 1
        if dead_end:
            b_new -= b
            a_new -= a
        if layout[b_new][a_new] == '#' and not dead_end:
            occ += 1

    if layout[y][x] == 'L' and occ == 0:
        row.append('#')
    elif layout[y][x] == '#' and occ >= 5:
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

def check_same(mtx_a, mtx_b):
    for i in range(0,len(mtx_a)):
        for j in range(0,len(mtx_a[i])):
            if mtx_a[i][j] != mtx_b[i][j]:
                return 0
    return 1

prv = seat_layout.copy()
nxt = create_next(seat_layout)

while not check_same(prv,nxt):
    prv = nxt.copy()
    nxt = create_next(prv)

occupied = 0
for i in range(0,len(prv)):
    for j in range(0,len(prv[i])):
        if prv[i][j] == '#':
            occupied +=1

print(occupied)
