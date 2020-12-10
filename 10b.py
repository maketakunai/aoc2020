#!/usr/bin/env python3

with open('./10_input.txt') as input_file:
    data = input_file.read().splitlines()
    data = list(map(int, data))

data.append(0)
data.append(max(data)+3)
data = sorted(data)

tracker = {x:0 for x in data}
tracker[0] = 1

for i in range(1, len(data)):
    for j in range(i):
        if data[i] - data[j] <= 3:
            tracker[data[i]] += tracker[data[j]]
            #print(i,j,data[i],data[j],tracker[data[i]],tracker[data[j]])

print(max(tracker.values()))
