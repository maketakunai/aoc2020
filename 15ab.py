#!/usr/bin/env python3

nums = [0,13,1,16,6,17]
log = {0:[1], 13:[2], 1:[3], 16:[4], 6:[5], 17:[6]}
target = 30000000
start = len(nums)
last = nums[-1]
for i in range(start+1,target+1):
    if (last in log) and (len(log[last]) == 1):
        log[0].append(i)
        last = 0
    else:
        temp = log[last][-1] - log[last][-2]
        if temp in log:
            log[temp].append(i)
        else:
            log[temp] = []
            log[temp].append(i)
        last = temp

for k,v in log.items():
    if target in v:
        print(k)