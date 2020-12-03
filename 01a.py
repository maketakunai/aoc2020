#!/usr/bin/env python3

with open('./01_input.txt') as input_file:
    nums = set([int(i) for i in input_file.read().splitlines()])

for i in nums:
    target = 2020 - int(i)
    if target in nums:
        print(target*int(i))
        break
    else:
        continue