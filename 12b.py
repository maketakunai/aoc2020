#!/usr/bin/env python3

instructions = []
with open('./12_input.txt') as input_file:
    for line in input_file:
        temp = line.strip()
        instructions.append((temp[0],int(temp[1:])))

ship = [0,0]
cardinal = ['N','E','S','W']
waypoint = [10,1]

for i in instructions:
    if i[0] == 'N':
        waypoint[1] += i[1]
    elif i[0] == 'S':
        waypoint[1] -= i[1]
    elif i[0] == 'E':
        waypoint[0] += i[1]
    elif i[0] == 'W':
        waypoint[0] -= i[1]
    elif i[0] == 'L':
        if i[1] == 90:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        elif i[1] == 180:
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        elif i[1] == 270:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    elif i[0] == 'R':
        if i[1] == 90:
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif i[1] == 180:
            waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
        elif i[1] == 270:
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif i[0] == 'F':
        ship[0] += waypoint[0]*i[1]
        ship[1] += waypoint[1]*i[1]

print(abs(ship[0]) + abs(ship[1]))