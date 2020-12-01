# 14mins, couldn't download the question for 10 mins, 
# perhaps the aoc website was ddos'ed

r = open('20-1.txt').read().split('\n')
v = [int(i) for i in r]
for a in v:
    for b in v:
        if a+b == 2020:
            print a*b
for a in v:
    for b in v:
        for c in v:
         if a+b+c == 2020:
            print a*b*c
