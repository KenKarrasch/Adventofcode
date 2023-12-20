import copy

f = open('23-19t2.txt').read().split('\n\n')

# split valid combinations into ranges
# input could have been made harder
ltr = {0:'x',1:'m',2:'a',3:'s'}

fwf = 'in'
wk = {}
for i in f[0].split('\n'):
   wkf = i.split('{')
   wkfn = wkf[0]
   if fwf == '':
     fwf = wkfn
   rs = wkf[1][0:-1].split(',')
   df = rs[-1]
   rl = []
   for act in rs[0:-1]:   
       dr = act.split(':')
       pr = dr[1]   
       for gt in ['>','<']:
         if gt in dr[0]:
          cmp = gt
          xmas = dr[0].split(gt)[0]
          v = int(dr[0].split(gt)[1])
       rl.append([xmas,cmp,v,pr])
   rl.append(df)
   wk[wkfn] = rl


xm = []
   
for i in f[1].split('\n'):
   xmas = []
   bl = i.split(',')
   for j in bl[0:3]:
     xmas.append(int(j.split('=')[1]))
   xmas.append(int(bl[3].split('=')[1].split('}')[0]))
   xm.append(xmas)


def rat(cst,lt,s,e):
    ncst = copy.deepcopy(cst)
    ncst[lt] = []
    nss = [0 for x in range(4000)]
    ct = 0
    for i in cst[lt]:
      for j in range(i[0],i[1]):
          nss[j] = 1
          ct += 1
    ct = 0
    for i in range(4000):
      if i < s or i >= e:
        nss[i] = 0
        ct += 1
    nncst = []
    sect = False
    ss = 0
    for i in range(4000):
      if nss[i] == 1:
        if not sect:
          ss = i
          sect = True
      if nss[i] == 0:
        if sect:
          nncst.append([ss,i])
          sect = False
    if sect:
        nncst.append([ss,4000])
    ncst[lt] = copy.deepcopy(nncst)
    return ncst
            

bin = []

def drill(wf,rln,cst):
   rl = rln
   if wf == 'A':
      bin.append(cst)
   elif wf == 'R':
      return
   else:      
      rls = wk[wf]
      ss = False
      rl = rls[rln]       
      if rl != rls[-1]:
        rdn = False
        for lt in range(4):           
           if ltr[lt] == rl[0]:            
            if rl[1] == '>':
              nwf = rl[3] 
              ncst = copy.deepcopy(cst)
              
              ncst = rat(cst,lt,rl[2]+1,4000)             
              drill(nwf,0,ncst)
              nwf = wf
              
              ncst = rat(cst,lt,0,rl[2])                
              drill(nwf,rln+1,ncst)
              
              rdn = True              
            if rl[1] == '<':
              nwf = rl[3] 
              ncst = rat(cst,lt,0,rl[2]-1)     
              drill(nwf,0,ncst)
              nwf = wf
              ncst = copy.deepcopy(cst)
              ncst = rat(cst,lt,rl[2],4000)                   
              drill(nwf,rln+1,ncst)            
              rdn = True
      else:            
          nwf = rl
          ncst = copy.deepcopy(cst)                    
          drill(nwf,0,ncst) 
          rdn = True
          
st = [[[1,4000]],[[1,4000]],[[1,4000]],[[1,4000]]]


drill('in',0,st)

ty = 0

for i in bin:
    mf = []
    for j in i:
       bt = 0
       for k in j:
           tp = k[1]
           d = 1+tp-k[0]
           bt += d
       mf.append(bt)
    ty += mf[0]*mf[1]*mf[2]*mf[3]
    
print 'part 2',ty
