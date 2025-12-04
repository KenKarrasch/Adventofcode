f = [x for x in open('25-4-1.txt').read().split('\n')]

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

dn = False

ttly = 0

while not dn:
    tly = 0
    fn = [[x[:] for x in y] for y in f]
    for r in range(len(f)):
        for c in range(len(f[0])):
            if f[r][c] == '@': 
                ct = 0
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < len(f) and 0 <= nc < len(f[0]):
                        if f[nr][nc] == '@':
                            ct += 1
                #print(r,c)
                if ct < 4:
                    fn[r][c] = '.'
                    tly += 1
                    ttly += 1
    if tly == 0:
        dn = True
    f = [[x[:] for x in y] for y in fn]
print(ttly)
