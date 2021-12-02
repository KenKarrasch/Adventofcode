tr = open('18-13.txt','r').read().split('\n')
L,U,R,D = 0,1,2,3
cts = []
m = [[D,L,U,R],[L,U,R,D],[U,R,D,L]]
curve = [[D,R,U,L],[U,L,D,R]]
advance = [[0,-1,0,1],[-1,0,1,0]]
for x in range(len(tr)):
  for y in range(len(tr[x])):
    if tr[x][y] in '<^>v':
      cts.append([x,y,'<^>v'.index(tr[x][y]),L,True])
allcrashed, pt1 = False, False
tcs = len(cts)
while not allcrashed:
   deadcts, pt2 = 0, 0   
   cts.sort(key=lambda i: tuple(i[:2]))  
   ctsprev = []
   for ct in range(tcs):
      ctsprev.append(cts[ct][:])   
   for ct in range(tcs):
       if tr[cts[ct][0]][cts[ct][1]] == '+':
          cts[ct][2] = m[cts[ct][3]][cts[ct][2]]
          cts[ct][3] = (cts[ct][3] + 1) % 3
       if tr[cts[ct][0]][cts[ct][1]] == '/':
           cts[ct][2] = curve[0][cts[ct][2]]
       if tr[cts[ct][0]][cts[ct][1]] == '\\':
           cts[ct][2] = curve[1][cts[ct][2]]       
       cts[ct][0] += advance[0][cts[ct][2]]
       cts[ct][1] += advance[1][cts[ct][2]]           
   for ct2 in range(tcs):
      for ct1 in range(tcs):
        if ct1 != ct2 and cts[ct1][4] and cts[ct2][4]:            
         if cts[ct1][:2] == cts[ct2][:2] or cts[ct1][:2] == ctsprev[ct2][:2] and ctsprev[ct1][:2] == cts[ct2][:2]:
                cts[ct1][4], cts[ct2][4]  = False, False
                if not pt1:
                   print 'part 1 -', cts[ct1][1],',', cts[ct1][0]
                   pt1 = True
   for h in range(tcs):        
     if cts[h][4]:
       deadcts += 1
       pt2 = h      
   if deadcts == 1:    
       allcrashed = True
       print 'part 2 -', cts[pt2][1],',', cts[pt2][0]         
