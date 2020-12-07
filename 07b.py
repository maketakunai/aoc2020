#!/usr/bin/env python3

bag_dict = {}
target = 'shiny gold'
with open('./07_input.txt') as input_file:
    for line in input_file:
        line = line.rstrip()
        line = line.split('bags contain ')
        contains = {}
        if line[1] == 'no other bags.':
            contains = {}
        else:
            for ch in ['bags.', 'bag.', 'bags', 'bag']:
                if ch in line[1]:
                    line[1] = line[1].replace(ch, '')
            line[1] = line[1].split(',')
            for bag in line[1]:
                bag = bag.lstrip().rstrip()
                contains[bag[2:]] = bag[0]

        bag_dict[line[0].rstrip()] = contains 

def dfs(graph, node):
    if not graph[node]:
        return 1
    return 1 + sum( (dfs(graph, key) * int(val) ) for key,val in graph[node].items())

print(dfs(bag_dict, target)-1) 