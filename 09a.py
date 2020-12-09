#!/usr/bin/env python3

with open('./09_input.txt') as input_file:
    data = input_file.read().splitlines()
    data = list(map(int, data))
window_size = 25
window_low = 0
window_high = 25
for i in range(25,len(data)):
    subsection = data[window_low:window_high]
    flag = 0
    for j in range(window_size):
        subsection = data[window_low:window_high]
        target = data[i] - subsection[j]
        if target in subsection and (data[i]/2 != target):
            flag = 1

    if flag == 0:
        print(data[i])
    window_low += 1
    window_high += 1