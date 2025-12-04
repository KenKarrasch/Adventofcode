f = [x for x in open('25-4-1.txt').read().split('\n')]

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

tly = 0

for r in range(len(f)):
    for c in range(len(f[0])):
        if f[r][c] == '@': 
            ct = 0
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0 <= nr < len(f) and 0 <= nc < len(f[0]):
                    if f[nr][nc] == '@':
                        ct += 1            
            if ct < 4:
                tly += 1

print(tly)
