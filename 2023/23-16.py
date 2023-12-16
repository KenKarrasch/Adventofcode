f = open('23-16.txt').read().split('\n')
drs = [[-1,0],[0,1],[1,0],[0,-1]]

bms = []
bmds = []

for i in range(len(f)):
  bms.append([i,-1])
  bmds.append(1)
  bms.append([i,len(f)])
  bmds.append(3)
  bms.append([-1,i])
  bmds.append(2)
  bms.append([len(f),i])
  bmds.append(0)
  
lg = []

for bd in range(len(bms)):
   bm = []
   bm.append(bms[bd][:])
   bmd = []
   bmd.append(bmds[bd])
   dn = []
   dnd = []
   while len(bm) > 0:
    nb = bm.pop(0)    
    nd = bmd.pop(0)
    if nb not in dn:
      dn.append(nb)
    if [nb[0],nb[1],nd] not in dnd:
     dnd.append([nb[0],nb[1],nd])         
     nb = nb[:] 
     nb[0] += drs[nd][0]
     nb[1] += drs[nd][1]     
     if 0 <= nb[0] < len(f[0]):
      if 0 <= nb[1] < len(f):           
        if f[nb[0]][nb[1]] == '.':          
          bm.append(nb)
          bmd.append(nd)
        if (nd == 0) or (nd == 2):
         if f[nb[0]][nb[1]] == '|':
          bm.append(nb)
          bmd.append(nd)
        if (nd == 1) or (nd == 3):
         if f[nb[0]][nb[1]] == '-':
          bm.append(nb)
          bmd.append(nd)
        if (nd == 1) or (nd == 3):
         if f[nb[0]][nb[1]] == '|':          
          bm.append(nb)
          bmd.append(0)
          bm.append(nb)
          bmd.append(2)
        if (nd == 0) or (nd == 2):
         if f[nb[0]][nb[1]] == '-':
          bm.append(nb)
          bmd.append(1)
          bm.append(nb)
          bmd.append(3)
        if nd == 1:
         if f[nb[0]][nb[1]] == '/':          
          bm.append(nb)
          bmd.append(0)
        if nd == 3:
         if f[nb[0]][nb[1]] == '/':
          bm.append(nb)
          bmd.append(2)
        if nd == 1:
         if f[nb[0]][nb[1]] == '\\':
          bm.append(nb)
          bmd.append(2)
        if nd == 3:
         if f[nb[0]][nb[1]] == '\\':
          bm.append(nb)
          bmd.append(0)
        if nd == 0:
         if f[nb[0]][nb[1]] == '/':
          bm.append(nb)
          bmd.append(1)
        if nd == 2:
         if f[nb[0]][nb[1]] == '/':
          bm.append(nb)
          bmd.append(3)
        if nd == 0:
         if f[nb[0]][nb[1]] == '\\':
          bm.append(nb)
          bmd.append(3)
        if nd == 2:
         if f[nb[0]][nb[1]] == '\\':
          bm.append(nb)
          bmd.append(1)
   print('checking line',bd,'of',len(bms))  
   print(len(dn)-1)
   lg.append(len(dn)-1)
print(max(lg))
