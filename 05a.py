#!/usr/bin/env python3

highest_id = 0

with open('./05_input.txt') as input_file:
    boarding_passes = input_file.read().splitlines()
    for b_pass in boarding_passes:
        row_range = list(range(128))
        col_range = list(range(8))
        for char in b_pass:
            if char == 'F':
                row_range = row_range[:len(row_range)//2]
            if char == 'B':
                row_range = row_range[len(row_range)//2:]
            if char == 'L':
                col_range = col_range[:len(col_range)//2]
            if char == 'R':
                col_range = col_range[len(col_range)//2:]
        id_calc = (row_range[0] * 8) + col_range[0]
        if id_calc > highest_id:
            highest_id = id_calc

print(highest_id)




