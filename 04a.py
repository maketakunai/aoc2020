#!/usr/bin/env python3

passport = {}
total_valid = 0
def check(input):
    valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    a = set(valid_keys)
    b = set(input.keys())
    if a.issubset(b):
        return 1
    else:
        return 0

with open('./04_input.txt') as input_file:
    passports = input_file.read().splitlines()
    passports.append('')
    for line in passports:
        if line != '':
            inputs = line.split()
            for pair in inputs:
                key,value = pair.split(':')
                passport[key] = value
        else:
            total_valid += check(passport)
            passport = {}

print(total_valid)




