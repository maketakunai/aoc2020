#!/usr/bin/env python3

with open('./14_input.txt') as input_file:
    instructions = input_file.read().splitlines()

stored_values = {}
def assign_value(mask,k, v, values):
    binary = format(int(v), 'b').zfill(len(mask))
    new_num = []
    for i_b,j_m in zip(binary, mask):
        if j_m in ['0','1']:
            new_num.append(j_m)
        else:
            new_num.append(i_b)
    values[k] = int(''.join(new_num),2)
    return

mask = ''
for line in instructions:
    line = line.split(' = ')
    if line[0] == 'mask':
        mask = line[1]
    else:
        k = ''.join(c for c in line[0] if c.isdigit())
        assign_value(mask,k,line[1], stored_values)

print(sum(stored_values.values()))