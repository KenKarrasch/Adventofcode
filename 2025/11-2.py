from functools import cache
f = open('25-11.txt').read().split('\n')
# 11    6393   3901  ***

#  Turned out to be bazillion paths, used basically same solution as day 7 using caching

rl = {}
for r in f:
    st = r.split(':')[0]
    es = r.split(':')[1].split()
    rl[st] = es

@cache
def score(pl,seendac,seenfft):
    if pl == 'out' and seendac and seenfft:
        return 1
    if pl == 'out':
        return 0
    tly = 0
    for np in rl[pl]:
        sd = seendac        
        sf = seenfft        
        if np == 'dac':
            sd = True
        if np == 'fft':
            sf = True            
        tly += score(np,sd,sf)
    return tly
    
print(score('svr',False,False))
