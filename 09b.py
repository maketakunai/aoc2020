#!/usr/bin/env python3

with open('./09_input.txt') as input_file:
    data = input_file.read().splitlines()
    data = list(map(int, data))
window_size = 25
window_low = 0
window_high = 25
invalid_num = 0
for i in range(25,len(data)):
    subsection = data[window_low:window_high]
    flag = 0
    for j in range(window_size):
        subsection = data[window_low:window_high]
        target = data[i] - subsection[j]
        if target in subsection and (data[i]/2 != target):
            flag = 1

    if flag == 0:
        invalid_num = data[i]
    window_low += 1
    window_high += 1


for i in range(len(data)):
    cur_sum = data[i]
    j = i + 1
    while j < len(data):
        if cur_sum == invalid_num:
            subsection = data[i:j-1]
            if not len(subsection):
                break
            else:
                print(min(subsection)+max(subsection))
        if cur_sum > invalid_num or j == len(data):
            break
        cur_sum = cur_sum + data[j]
        j += 1

