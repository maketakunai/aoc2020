#!/usr/bin/env python3
import itertools

with open('./14_input.txt') as input_file:
    instructions = input_file.read().splitlines()

stored_values = {}
def assign_value(mask, k, v, values):
    binary = format(int(k), 'b').zfill(len(mask))
    new_num = []
    x_count = 0
    for c in mask:
        if c == 'X':
            x_count += 1
    #create number of bit permutations determined by num of X's in mask
    perms = [list(seq) for seq in itertools.product("01", repeat=x_count)]

    #generate the masked address 
    for i_b,j_m in zip(binary, mask):
        if j_m == '0':
            new_num.append(i_b)
        elif j_m == '1':
            new_num.append(j_m)
        elif j_m == 'X':
            new_num.append(j_m)

    #generate permutations of masked address
    for b_perm in perms:
        temp_res = []
        for c in new_num:
            if c == 'X':
                temp_res.append(b_perm.pop())
            else:
                temp_res.append(c)
        values[int(''.join(temp_res),2)] = int(v)


mask = ''
for line in instructions:
    line = line.split(' = ')
    if line[0] == 'mask':
        mask = line[1]
    else:
        k = ''.join(c for c in line[0] if c.isdigit())
        assign_value(mask,k,line[1], stored_values)

print(sum(stored_values.values()))