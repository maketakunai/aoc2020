#!/usr/bin/env python3

with open('./10_input.txt') as input_file:
    data = input_file.read().splitlines()
    data = list(map(int, data))

data = sorted(data)
jolt1 = 1
jolt3 = 1
for i in range(0,len(data)-1):
    diff = data[i+1] - data[i]
    if diff == 1:
        jolt1 += 1
    else:
        jolt3 += 1

print(jolt1*jolt3) 