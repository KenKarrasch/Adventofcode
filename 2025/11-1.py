f = open('in.txt').read().split('\n')

rl = {}
for r in f:
    st = r.split(':')[0]
    es = r.split(':')[1].split()
    rl[st] = es

Q = ['you']
tly = 0

while Q:
    pl = Q.pop()
    if pl == 'out':
        tly += 1
        continue
    if pl in rl.keys():
        for i in rl[pl]:
            Q.append(i)
print(tly)
