f = [[int(y) for y in x] for x in open('day2in.txt').read().split('\n')]

def gn(pl,ut,sq,num):
    if pl == 12:
        return num
    bn = 0
    lb = 0
    for i in range(ut,len(sq)-(11-pl)):
        if sq[i] > bn:
            bn = sq[i]
            lb = i
    return gn(pl+1,lb+1,sq,num*10+bn)
  
tly = 0
for i in f: 
    tly += gn(0,0,i,0)
print(tly)
