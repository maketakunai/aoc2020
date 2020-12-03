#!/usr/bin/env python3

with open('./02_input.txt') as input_file:
    passwords = input_file.read().splitlines()

total = 0

for pw in passwords:
    pw = pw.split(' ')
    count = pw[2].count(pw[1][0])
    bounds = pw[0].split('-')
    if (count >= int(bounds[0])) and (count <= int(bounds[1])):
        total += 1

print(total)
