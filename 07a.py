#!/usr/bin/env python3

bag_dict = {}
target = 'shiny gold'
count = 0
with open('./07_input.txt') as input_file:
    for line in input_file:
        line = line.rstrip()
        line = line.split('bags contain ')
        contains = []
        if line[1] == 'no other bags.':
            contains = []
        else:
            for ch in ['bags.', 'bag.', 'bags', 'bag']:
                if ch in line[1]:
                    line[1] = line[1].replace(ch, '')
            line[1] = line[1].split(',')
            for bag in line[1]:
                bag = bag.lstrip().rstrip()
                #bag = [bag[0], bag[2:]]
                bag = bag[2:]
                contains.append(bag)

        bag_dict[line[0].rstrip()] = contains 


def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for n in graph[node]:
            dfs(visited, graph, n)
    

for bag in bag_dict:
    visited = set()
    dfs(visited, bag_dict, bag)
    if target in visited:
        count += 1

print('bags: ', count-1)
