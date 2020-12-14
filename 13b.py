#!/usr/bin/env python3
import math

with open('./13_input.txt') as input_file:
    notes = input_file.read().splitlines()

times = notes[1].split(',')
times = [0 if x=='x' else int(x) for x in times]

sched = []
for i in range(len(times)):
    if times[i]:
        sched.append((i, times[i]))
print(sched)

time_stamp = 0
increment = 1

for i,bus in sched:
    while (time_stamp + i) % bus != 0:
        time_stamp += increment
    increment *= bus

print(time_stamp)