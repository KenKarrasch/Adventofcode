p = ['children','cats','samoyeds','pomeranians','akitas',
     'vizslas','goldfish','trees','cars','perfumes']
m = [3,7,2,3,0,0,5,3,2,1]
s = open('15-16.txt').read().split('\n')
sues = []
for i in s:
    sue = [-1 for x in range(len(p))]
    for th in range(len(sue)):
        if p[th] in i:
            sue[th] = int(i.split(p[th]+':')[1].split(',')[0])
    sues.append(sue)

for i in range(len(sues)):
    wsue = True
    for j in range(len(p)):
        if (m[j] != sues[i][j]) and (sues[i][j] != -1):
            wsue = False
    if wsue:
        print('part 1 -',i+1)
        
for i in range(len(sues)):
    wsue = True
    for j in range(len(p)):
        if j in [1,7]:
            if (m[j] > sues[i][j]) and (sues[i][j] != -1):
                wsue = False
        if j in [3,6]:
            if (m[j] <= sues[i][j]) and (sues[i][j] != -1):
                wsue = False
        if j not in [1,7,3,6]:
           if (m[j] != sues[i][j]) and (sues[i][j] != -1):
            wsue = False
    if wsue:
        print('part 2 -',i+1)
