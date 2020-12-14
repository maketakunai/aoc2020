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


# satisfied = 0
# target = len(sched)
# base_list = [sched[0][1]+sched[x][0] for x in range(len(sched))]
# print(base_list)
# increment = sched[0][1]
# increment = 17
# tracker = [0 for i in base_list]
# print(tracker)
# curr = sum(tracker)
# while not satisfied:
#     counter = 0
#     for j in range(len(base_list)):
#         if base_list[j] % sched[j][1] == 0:
#             counter += 1
#             if not tracker[j]:
#                 tracker[j] = 1
#         else:
#             break
#     print(j,counter,base_list[j],tracker)
#     if counter == target:
#         satisfied = 1
#     if sum(tracker) > curr:
#         increment = lcm(sched[0][0], sched[1][0])
#         curr = sum(tracker)
#     else:
#         base_list = [x+increment for x in base_list]
# print(base_list)