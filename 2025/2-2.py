f = open('day2in.txt').read().split('\n')

nf = ''
for i in f:
    nf = nf + i
f = nf.split(',')
sq = []
for i in f:
    st = int(i.split('-')[0])
    ed = int(i.split('-')[1])
    sq.append((st,ed+1))
tly = 0

def rtptn(num):
    s = str(num)
    l = len(s)
    for i in range(1, l // 2 + 1):
        if l % i == 0: 
            sb = s[:i]
            if sb * (l // i) == s:
                return True
    return False

for i in sq:
    for s in range(i[0],i[1]):
        if rtptn(s):
            tly += s
print(tly)
