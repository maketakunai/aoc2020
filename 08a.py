#!/usr/bin/env python3

with open('./08_input.txt') as input_file:
    instructions = input_file.read().splitlines()

def nop(instructions, pointer, accumulator, visited):
    visited.add(pointer)
    pointer += 1
    return pointer, accumulator, visited
def acc(instructions, pointer, accumulator, visited):
    visited.add(pointer)
    value = instructions[pointer].split()
    accumulator += int(value[1])
    pointer +=1
    return pointer, accumulator, visited
def jmp(instructions, pointer, accumulator, visited):
    visited.add(pointer)
    value = instructions[pointer].split()
    pointer += int(value[1])
    return pointer, accumulator, visited

pointer = 0
accumulator = 0
visited = set()
while pointer not in visited:
    ins = instructions[pointer][0:3]
    if ins == 'nop':
        pointer, accumulator, visited = nop(instructions, pointer, accumulator, visited)
    if ins == 'acc':
        pointer, accumulator, visited = acc(instructions, pointer, accumulator, visited)
    if ins == 'jmp':
        pointer, accumulator, visited = jmp(instructions, pointer, accumulator, visited)
    
print(accumulator)