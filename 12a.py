#!/usr/bin/env python3

instructions = []
with open('./12_input.txt') as input_file:
    for line in input_file:
        temp = line.strip()
        instructions.append((temp[0],int(temp[1:])))

ship = ['E',0,0]
cardinal = ['N','E','S','W']

for i in instructions:
    if i[0] == 'N':
        ship[2] += i[1]
    elif i[0] == 'S':
        ship[2] -= i[1]
    elif i[0] == 'E':
        ship[1] += i[1]
    elif i[0] == 'W':
        ship[1] -= i[1]
    elif i[0] == 'L':
        multiplier = i[1]//90
        r_cardinal = cardinal[::-1]
        idx = r_cardinal.index(ship[0])
        ship[0] = r_cardinal[(idx+multiplier)%4]
    elif i[0] == 'R':
        multiplier = i[1]//90
        idx = cardinal.index(ship[0])
        ship[0] = cardinal[(idx+multiplier)%4]
    elif i[0] == 'F':
        if ship[0] == 'N':
            ship[2] += i[1]
        elif ship[0] == 'S':
            ship[2] -= i[1]
        elif ship[0] == 'E':
            ship[1] += i[1]
        elif ship[0] == 'W':
            ship[1] -= i[1]

print(abs(ship[1]) + abs(ship[2]))