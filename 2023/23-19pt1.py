f = open('23-19t.txt').read().split('\n\n')

ltr = {0:'x',1:'m',2:'a',3:'s'}

fwf = ''
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


ty = 0

for pt in xm:
   dn = False
   wf = 'in'    
   while not dn:               
    if wf == 'A':
      st = sum(pt)
      ty += st
      dn = True
    elif wf == 'R':
      dn = True
    else:      
      rls = wk[wf]
      ss = False
      wfc = ''
      rdn = False
      for rl in rls:       
       if not rdn:         
         if rl != rls[-1]: # last one default
          rdn = False
          for lt in range(4):           
           if ltr[lt] == rl[0]:            
            if rl[1] == '>':
             if pt[lt] > rl[2]:
              wf = rl[3]              
              rdn = True              
            if rl[1] == '<':
             if pt[lt] < rl[2]:
              wf = rl[3]              
              rdn = True
         else:            
          wf = rl                    
          rdn = True

print(4000*4000*4000*4000)    
print(167409079868000)    

print(ty)

cds = []

for wf in list(wk.keys()):
  rls = wk[wf]
  for rl in rls[0:-1]:    
    if rl[3] == 'A':
      cds.append(wf)
  if rls[-1] == 'A':
      cds.append(wf)

print(cds)

      
