f = [int(i) for i in open('21-7.txt').read().split(',')]

def tc(d):
    return int(0.5*(d*(d+1)))
    
for pt in [1,2]:
 d = []
 for g in range(max(f)):
    t = 0
    for i in f:
        ds = abs(i-g)
        if pt == 1: t += abs(i-g)
        else: t += tc(abs(i-g))
    d.append(t)
 print 'part',pt,'-',min(d)
