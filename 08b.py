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

original_path = []
pointer = 0
accumulator = 0
visited = set()
last = 0
while pointer not in visited and pointer < len(instructions):
    ins = instructions[pointer][0:3]
    last = pointer
    original_path.append(last)
    if ins == 'nop':
        pointer, accumulator, visited = nop(instructions, pointer, accumulator, visited)
    if ins == 'acc':
        pointer, accumulator, visited = acc(instructions, pointer, accumulator, visited)
    if ins == 'jmp':
        pointer, accumulator, visited = jmp(instructions, pointer, accumulator, visited)
    
for i in reversed(original_path):
    new_ins = instructions.copy()
    if instructions[i][0:3] == 'jmp':
        new_ins[i]=new_ins[i].replace('jmp', 'nop')
    elif instructions[i][0:3] == 'nop':
        new_ins[i]=new_ins[i].replace('nop', 'jmp')

    pointer = 0
    accumulator = 0
    visited = set()
    last = 0
    while pointer not in visited and pointer < len(new_ins):
        ins = new_ins[pointer][0:3]
        last = pointer
        if ins == 'nop':
            pointer, accumulator, visited = nop(new_ins, pointer, accumulator, visited)
        if ins == 'acc':
            pointer, accumulator, visited = acc(new_ins, pointer, accumulator, visited)
        if ins == 'jmp':
            pointer, accumulator, visited = jmp(new_ins, pointer, accumulator, visited)
    
    if pointer >= len(new_ins):
        print(pointer, last, accumulator)

