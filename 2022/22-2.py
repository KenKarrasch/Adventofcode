f = open('22-2.txt').read().split('\n')
# nice puzzle after christmas party
wn = ['A Y','B Z','C X']
l = ['A Z','B X','C Y']
t= {'X': 1,'Y': 2,'Z': 3}
sc = 0
for i in f:
    sc += t[i[2]] + 3
    if i in wn: sc += 3
    if i in l: sc -= 3
print 'part 1',sc

r = ['A Y','B X','C Z']
p = ['A Z','B Y','C X']
s = ['A X','B Z','C Y']
t= {'X': 1,'Y': 2,'Z': 3}
sc = 0
for i in f:
    if i in r: ob = 'X'
    if i in p: ob = 'Y'
    if i in s: ob = 'Z'
    sc += t[ob] + 3
    ni = i[0] + ' ' + ob
    if ni in wn: sc += 3
    if ni in l: sc -= 3
print 'part 2',sc
