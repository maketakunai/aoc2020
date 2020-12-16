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

valid_list = info[2][1:][:]

total_invalid = 0
for j in info[2][1:]:
    inv_value = check(j, criteria)
    total_invalid += inv_value
    if inv_value:
        valid_list.remove(j)
print(total_invalid)

valid_list = [i.split(',') for i in valid_list]
transpose_valid = [list(i) for i in zip(*valid_list)]
possible = dict.fromkeys(criteria.keys())
for rule in possible:
    possible[rule] = set()

for col in range(len(transpose_valid)):
    for rule in criteria:
        range1 = criteria[rule][0].split('-')
        range2 = criteria[rule][1].split('-')
        if all( (int(e) >= int(range1[0]) and int(e) <= int(range1[1])) or (int(e) >= int(range2[0]) and int(e) <= int(range2[1])) for e in transpose_valid[col]):
            possible[rule].add(col)

for k,v in possible.items():
    print(k,v)

# eliminated possibilities by hand
# to-do: fix this later

my_tix = info[1][1].split(',')
my_tix = [int(i) for i in my_tix]

print(my_tix[3] * my_tix[5] * my_tix[16] * my_tix[11] * my_tix[4] * my_tix[17])