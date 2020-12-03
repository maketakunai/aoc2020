#!/usr/bin/env python3

with open('./02_input.txt') as input_file:
    passwords = input_file.read().splitlines()

total = 0

for pw in passwords:
    pw = pw.split(' ')
    bounds = pw[0].split('-')
    target = pw[1][0]
    if ((pw[2][int(bounds[0])-1] == target) and not (pw[2][int(bounds[1])-1] == target)) or ((pw[2][int(bounds[1])-1] == target) and not (pw[2][int(bounds[0])-1] == target) ):
        total += 1

print(total)
