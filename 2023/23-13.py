f = open('23-13.txt').read().split('\n\n')

# Took a while to work out the reflections for part 2, and what counts as a change due to smudge

cs = 0
rs = 0
ty = 0
def hr(r,g):
    gd = False
    for rd in range(min(len(g)-r-1,r+1)):
      gd = True
      for c in range(len(g[0])):
        if g[r-rd][c] != g[1+r+rd][c]:
            return False
    return gd
               
def vr(c,g):
    gd = False
    for cd in range(min(len(g[0])-c-1,c+1)):
      gd = True
      for r in range(len(g)):
        if g[r][c-cd] != g[r][1+c+cd]:
          return False
    return gd
    
def getrc(g):
    cs = [0]
    rs = [0]
    for r in range(len(g)-1):
      if hr(r,g):
        rs.append(r+1)
    for c in range(len(g[0])-1):
      if vr(c,g):
        cs.append(c+1)      
    return [rs[:],cs[:]]
    
d = []

for mr in f:  
    g = mr.split('\n')
    ot = getrc(g)
    rs,cs = ot[0][-1],ot[1][-1]
    ty += 100*(rs) + (cs)

print('part 1',ty)
ty = 0

for mr in f:  
    g = mr.split('\n')
    ot = getrc(g)
    rs,cs = ot[0][-1],ot[1][-1]    
    td = []
    if True:
     fd = False
     for sx in range(len(g[0])):
      for sy in range(len(g)):
        tg = []
        ot = []        
        for i in range(len(g[0])):
          ln = []
          for j in range(len(g)):
            if [i,j] == [sx,sy]:
              if g[j][i] == '.':
                ln.append('#')                
              else:
                ln.append('.')                
            else:               
               ln.append(g[j][i])
          tg.append(ln)
        ot = getrc(tg)
        for i in range(len(tg[0])):
          line = ''
          for j in range(len(tg)):#i:
            line += tg[j][i]
        for el in ot[0]:
         if not fd:
          if el != cs:
            if el != 0:              
              d.append([el,0])
              fd = True         
        for el in ot[1]:
         if not fd:
          if el != rs:
            if el != 0:              
              d.append([0,el])
              fd = True                  


for i in d:
    ty += i[0]*1
    ty += i[1]*100
print('part 2',ty)

# 5089 too low
# 8950 too low
