#!/usr/bin/env python3
import math

with open('./13_input.txt') as input_file:
    notes = input_file.read().splitlines()

target = int(notes[0])

times = notes[1].split(',')
times = [int(n) for n in times if n.isdigit()]

def closest_time(target, time):
    if time > target:
        return time
    steps = math.ceil(target/time)
    return steps * time

closest = [closest_time(target, i) for i in times]
c_index = closest.index(min(closest))
print( times[c_index] * (closest[c_index]-target) )