#!/usr/bin/env python3

with open('./06_input.txt') as input_file:
    answers = input_file.read().splitlines()
    answers.append('')

counter = set()
total = 0
for reply in answers:
    if reply != '':
        counter.update(list(reply))
    else:
        total += len(counter)
        counter.clear()

print(total)
