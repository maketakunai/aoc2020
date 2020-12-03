#!/usr/bin/env python3

with open('./01_input.txt') as input_file:
    nums = set([int(i) for i in input_file.read().splitlines()])

for i in nums:
    target_1 = 2020 - i
    for j in nums:
        if j == i:
            continue
        else:
            target_2 = abs(target_1 - j)
            if (target_2 in nums) and (target_2+i+j == 2020):
                print(target_2, i, j)
                print(target_2*i*j)
                break
            else:
                continue