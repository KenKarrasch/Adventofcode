import copy

f = open('23-22.txt').read().split('\n')

# verry slow, need to optimise

#print(f)
cb = []

for i in f:
    cdi = [[int(z) for z in y.split(',')] for y in i.split('~')]
    if(cdi[0][2] > cdi[1][2]):
       cb.append([cdi[1],cdi[0]])
    else:
       cb.append([cdi[0],cdi[1]])
    #cb.append([[int(z) for z in y.split(',')] for y in i.split('~')])

nl = []
for i in range(len(cb)):   
   nl.append([cb[i][0][2],cb[i][1][2],cb[i][0][1],cb[i][1][1],cb[i][0][0],cb[i][1][0]])
#print('nl unsorted',nl)
nl.sort()
#print('nl sorted',nl)
ncb = []
for i in range(len(nl)):
   ad = []
   pt1 = []      
   pt1.append(nl[i][4])
   pt1.append(nl[i][2])
   pt1.append(nl[i][0])
   ad.append(pt1) 
   pt2 = []
   pt2.append(nl[i][5])
   pt2.append(nl[i][3])
   pt2.append(nl[i][1])
   ad.append(pt2)    
   ncb.append(ad)
#print(len(cb))
#print(len(ncb))
#print(ncb)
#print(cb)
cb = copy.deepcopy(ncb)

st = []
mxz = 0
for i in range(len(cb)):
   if cb[i][0][2] - cb[i][1][2] > mxz:      
      mxz = cb[i][0][2] - cb[i][1][2]
   if cb[i][1][2] - cb[i][0][2] > mxz:      
      mxz = cb[i][1][2] - cb[i][0][2]
   st.append((cb[i][0][2],cb[i][1][2]))
#print('mxz',mxz)


#print(st)
st.sort()
print 
#print(st)

def getms():
   mx = [-100000,-100000,-100000]
   mn = [100000,100000,100000]
   for i in cb: 
    for e in [0,1]: 
     for d in [0,1,2]:    
      if i[e][d] < mn[d]:
         #print(d,i,mn)
         mn[d] = i[e][d]
      if i[e][d] > mx[d]:
         mx[d] = i[e][d] + 1
   return(mx,mn)     

mx,mn = getms()

print (mx,mn)


def ovlp(r1,r2):
    (x1, y1), (x2, y2) = r1
    (x3, y3), (x4, y4) = r2    
    if x2 < x3 or x1 > x4: return False
    if y2 < y3 or y1 > y4: return False
    return True   

laser = [] 

for x in range(1+mx[0]):
   xs = []
   for y in range(1+mx[1]):
     tps = []
     btms = []
     for i in range(len(cb)):
        c1 = cb[i]  
        r1 = ((c1[0][0],c1[0][1]),(c1[1][0],c1[1][1]))
        r2 = ((x,y),(x,y))
        if ovlp(r1,r2):
          if cb[i][0][2] > cb[i][0][2]:
           tps.append(cb[i][0][2])
           btms.append(cb[i][1][2])
          else:
           tps.append(cb[i][1][2])
           btms.append(cb[i][0][2])
     xs.append([tps,btms])
   laser.append(xs) 

#for i in laser:
   #print(i)

    


def incubeyz(i,y,z,ncb):    
    c1 = ncb[i]    
    r1 = ((c1[0][1],c1[0][2]),(c1[1][1],c1[1][2]))
    r2 = ((y,z),(y,z))
    if ovlp(r1,r2):
        return True
    return False

def prtyz(o,ncb):
   print(mx[2],mx[1])
   print('-----------------')   
   for z in range(1+(mx[2]))[::-1]:
      ln = ''
      for y in range(mn[1]-1,1+mx[1]):
         l = ''
         #print(y,z)
         for i in range(len(ncb))[::o]:
            if incubeyz(i,y,z,ncb):
               l = chr(ord('A') + i)
         if l == '':
            ln += '.'
         else: ln += l
      print(ln)     
   



def incubexz(i,x,z,ncb):    
    c1 = ncb[i]    
    r1 = ((c1[0][0],c1[0][2]),(c1[1][0],c1[1][2]))
    r2 = ((x,z),(x,z))
    if ovlp(r1,r2):
        return True
    return False

def prtxz(ncb):
   print(mx[2],mx[0])
   print('-----------------')   
   print(ncb)
   for z in range(1+(mx[2]))[::-1]:
      ln = ''
      for x in range(mn[0]-1,1+mx[0]):
         l = ''
         for i in range(len(ncb)):
            if incubexz(i,x,z,ncb):
               l = chr(ord('A') + i)
         if l == '':
            ln += '.'
         else: ln += l
      print(ln)         

def mvdn(c,ncb,brg,trg):
    fd = []  # fall down options
    #print('looking at',c,cb)
    for i in range(max(0,c+brg),min(c + trg,len(ncb))):      
      btm = min(ncb[c][0][2],ncb[c][1][2]) # bottom of this cube
      tp = max(ncb[i][0][2],ncb[i][1][2]) # top of other cube
      #print('tp,btm',tp,btm)
      if tp < btm:
       if c != i:          
        c1 = ncb[i]
        c2 = ncb[c]       
        r1 = ((c1[0][0],c1[0][1]),(c1[1][0],c1[1][1]))
        r2 = ((c2[0][0],c2[0][1]),(c2[1][0],c2[1][1]))
        #print('r1,r2',r1,r2)
        if ovlp(r1,r2):
              fd.append(-1 + btm - tp)    
    #print('fd',fd)
    if len(fd) > 0:    
      if(min(fd) > 0):
        ncb[c][0][2] -= min(fd)
        ncb[c][1][2] -= min(fd)
        #print('fd',fd)
        return True
      #print('not fd',fd)      
      return False  
    else:
        dnd = min(ncb[c][0][2],ncb[c][1][2])
        ncb[c][0][2] -= dnd
        ncb[c][1][2] -= dnd
        if dnd == 0:          
          #print('dndo',dnd)
          return False
        #print('dnd1',dnd)
        return True
    return False  

mx,mn = getms()
#print('mx,mx',mx,mn)
#prtxz()
#prtyz(1)
#print('---------------')

dn = False
sc = 0
while not dn:
   print('scan',sc)
   sc += 1
 #for h in [0]:
   dn = True
   #print('-run 1-------------')
   for c in range(len(cb)):
      #print('cube',c)      
      if mvdn(c,cb, -1500,1500):  
        #print('cube moved down',c)      
        dn = False
mx,mn = getms()
#print('mx,mx',mx,mn)
#prtxz()
#prtyz(1)
#prtyz(-1)
#print(cb,len(cb))
ct = 0

def dis(cbe,ocb,depth):
  global ct  
  popable = True    
  fally = []     
  #print('depth,cbe',depth,cbe)
  tmpl = copy.deepcopy(ocb)   
  dmy = tmpl.pop(cbe)
  
  if depth < 30: #for cbe in range(len(ocb)):
    #print('mx,mx',mx,mn)
    #print(ocb)
    #prtxz(tmpl)
    #prtyz(1,tmpl)
    #prtyz(-1,tmpl)    
    if True:# False:          
     for snum in range(len(tmpl)):      
      ncb = copy.deepcopy(tmpl)         
      #print(ncb)
      #print('searching',snum)      
      if popable == True:
       #if snum != cbe: 
        if mvdn(snum,ncb,-50,50):
         #print('not popable',cbe,snum,tmpl[snum])
         popable = False 
         fally.append([tmpl[snum][0][:],tmpl[snum][1][:]])    
       
  if not popable:
     css = []    
     #print('fally',fally)
     nncb = copy.deepcopy(ocb) 
     dmy = nncb.pop(cbe)  
     #print(nncb,fally)
     for fy in range(len(fally)):         
        fyr = -1        
        for i in range(len(nncb)):           
           #print('eq',nncb[i][0],fally[fy][0])
           if nncb[i][0] == fally[fy][0]:
             #print('here')
             if nncb[i][1] == fally[fy][1]:
              fyr = i
        css.append(dis(fyr,nncb,depth+1)+1)
     #print('css',css)
     return max(css)    
  else: 
     return 1
     

css = []

for cbe in range(len(cb)):
   print('testing',cbe)
   res = dis(cbe,cb,0)
   css.append(res-1)
    
print ('css',css)
print('part 2',sum(css))


    
    # 538 too high
# 522 correct answer
