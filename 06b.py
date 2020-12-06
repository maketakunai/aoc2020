#!/usr/bin/env python3

with open('./06_input.txt') as input_file:
    answers = input_file.read().splitlines()
    answers.append('')

total_answers = ''
people = 0
total_yes = 0
for reply in answers:
    if reply != '':
        total_answers += reply
        people += 1
    else:
        c = lambda total_answers, char: total_answers.count(char)
        answer_dict = dict([(char, c(total_answers, char)) for char in total_answers])
        for k,v in answer_dict.items():
            if int(people) == int(v):
                total_yes += 1
        total_answers = ''
        people = 0

print(total_yes)