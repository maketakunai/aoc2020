#!/usr/bin/env python3
from itertools import groupby

with open('./16_input.txt') as input_file:
    info = input_file.read().splitlines()

def check(tix_nums, criteria):
    tix_nums = tix_nums.split(',')
    for num in tix_nums:
        flag = 0
        for rule in criteria:
            range1 = criteria[rule][0].split('-')
            range2 = criteria[rule][1].split('-')
            if int(num) in range(int(range1[0]),int(range1[1])+1) or int(num) in range(int(range2[0]),int(range2[1])+1):
                flag = 1
                break
            else:
                continue
        if flag == 0:
            return int(num)
        else:
            continue
    return 0

info = [list(sub) for ele, sub in groupby(info, key = bool) if ele]

criteria = {}

for i in info[0]:
    line = i.split(': ')
    ranges = line[1].split(' or ')
    criteria[line[0]] = ranges

total_invalid = 0
for j in info[2][1:]:
    inv_value = check(j, criteria)
    total_invalid += inv_value

print(total_invalid)