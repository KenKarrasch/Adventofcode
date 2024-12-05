
# Online Python - IDE, Editor, Compiler, Interpreter

# finding all permutation was taking too long, then I realised I only needed to 
# find a number that had an equal number to the left as the right.

import functools
g = open('24-5.txt').read()

pu = []

pn = []

import itertools

for i in g.split('\n\n')[0].split('\n'):
        print(i)
        pu.append(i)

for i in g.split('\n\n')[1].split('\n'):
    for b in i.split('\n'):
        pn.append([j for j in i.split(',')])


strs = []

for y in pu:
    i = y.split('|')
    for j in [0,1]:
        if i[j] not in strs:
            strs.append(i[j])

print(strs)
def check_order(string_book, rules):
    for rule in rules:
        string1, string2 = rule.split('|')
        if string1 in string_book and string2 in string_book:
            if string_book.index(string1) > string_book.index(string2):
                return False
    return True

ct = 0
ct2 = 0
for i in pn:
    result = check_order(i, pu)
    if(result):
        ct += int(i[len(i)//2])
    else:        
        for a in i:
            lft = 0
            rgt = 0
            for b in i:
                if a!= b:
                    if a + '|' + b in pu:
                        lft += 1
                    if b + '|' + a in pu:
                        rgt += 1
            if lft == rgt:
                ct2 += int(a)
print('part 1 -',ct)
print('part 2 -',ct2)
