import re
f = open('22-5.txt').read().split('\n')

ngd = []

for i in f:
    if '[' in i:
      st = []
      for j in range(9):    
        if(1 + j*4 < len(i)):
            st.append(i[1 + j*4])
        else: st.append(' ')
      ngd.append(st)

def countgd(g):
    lt = 0
    for i in g:
        for j in i:
            if j != ' ':
                lt += 1
    return lt

def getgd(gi):
    ng = []
    for u in range(len(gi)):
        ng.append(gi[-1+len(gi)-u][::])
    for i in range(countgd(ng)):
        ng.append([' ']*9)    
    return(ng)    

def gh(col):
    ct = 0
    for i in range(len(gd)):
        st = gd[-1+len(gd)-i]
        if st[col] != ' ':
            ct += 1
    return(ct)

for pt in [1,2]:
  gd = getgd(ngd)
  for i in f:
    if 'move' in i:
        sz,s,e = [int(k) for k in re.findall(r'\d+', i)]
        stk = []
        hts = gh(s-1)
        for j in range(sz):
            stk.append(gd[hts-sz+j][s-1])                 
        hte = gh(e-1)
        stk = stk[::-3+2*pt]
        for j in range(sz):                        
            gd[hte+j][e-1] = stk[j][::-1]
        for j in range(sz):                        
            gd[hts+j-sz][s-1] = ' '

  cd = ''
  for i in range(9):    
    cd += gd[gh(i)-1][i]
  print('part',pt,'-',cd)
