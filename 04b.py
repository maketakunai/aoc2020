#!/usr/bin/env python3

passport = {}
total_valid = 0
def check(pp):
    flags = [0] * 6
    valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    a = set(valid_keys)
    b = set(pp.keys())
    if a.issubset(b):
        flags[0] = 1
    else:
        return 0

    if (1920 <= int(pp['byr']) <= 2002) and (2010 <= int(pp['iyr']) <= 2020) and (2020 <= int(pp['eyr']) <= 2030):
        flags[1] = 1

    if (pp['hgt'][-2:] in {'in','cm'}):
        temp_s = ''.join(i for i in pp['hgt'] if i.isdigit())
        if (pp['hgt'][-2:] == 'cm' and (150 <= int(temp_s) <= 193)) or (pp['hgt'][-2:] == 'in' and (59 <= int(temp_s) <= 76)):
            flags[2] = 1

    if pp['hcl'][0] == '#' and len(pp['hcl']) == 7:
        if pp['hcl'][1:].isalnum():
            flags[3] = 1

    if pp['ecl'] in valid_ecl:
        flags[4] = 1
    
    if pp['pid'].isdigit() and len(str(pp['pid'])) == 9:
        flags[5] = 1
    
    if sum(flags) == 6:
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




