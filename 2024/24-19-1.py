f = open('24-19.txt').read().split('\n\n')

sc = [i.strip() for i in f[0].split(',')]
#print(sc)

cd = f[1].split('\n')

DP = {}

def sch(design,dpth):
    #print(design,dpth)
    if design in DP:
        return DP[design]
    gd = 0
    for i in sc:
        if gd == 0:
            if i == design:
                return 1
            if design.startswith(i):
                #print('searching',design,i)
                if len(i) <= len(design):
                    gd = sch(design[len(i):],dpth+1)
    DP[design] = gd
    return gd

ct = 0
for c in cd:
    print(c)
    ct += sch(c,0)
print(ct)

