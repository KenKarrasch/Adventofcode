r = open('23-5.txt').read().split('\n\n')
# comments and debugging left in

sds = [int(y) for y in r[0].split(':')[1].split()]
lx = 100000000000000000000000000 #max(sds)
dp = []
bk = []
for m in r:
  if len(m) > 0:
    st = []
    #st = [[int(y) for y in x.split()] for x in m.split('\n')[1:]]
    item = []
    #print 
    for xs in m.split('\n')[1:]:
        x = [int(y) for y in xs.split()]
        xs = [x[1],x[0],x[2]]
        item.append(xs)
    #print (item)
    item.sort()
    #print('sorted',item)
    
    sitem = []
    for ite in item:
       it = [ite[1],ite[0],ite[2]]
       sitem.append(it)
    st.append(sitem)
    #print(st)
    bk.append(sitem)
  else:
    bk.append()
#print ('bk',bk)

def gt(t,fr,n):
    #print('adding',n)
    fr.append(n)

def grt(tx,n):
 global lx
 if tx == len(bk):
   if n[0] < lx:
     if(n[0] != 0):
       print ('new low',n[0])
     lx = n[0]
   return n[0]
 t = tx+1
 #print("---------------",tx)
 #print( t,n)
 
 s,l = n[0],n[1]
 fr = []
 for m in bk[tx]:
    #print(m)
    if(s < m[1]):    
      if s+l >= m[1]+m[2]:
        #print('x|x|x')
        gt(t,fr,[s,m[1]-s])
        gt(t,fr,[m[0],m[2]])
        #gt(t,fr,[m[1]+m[2],s-(m[1]+m[2])])
      if s+l > m[1]:
        #print ('x|x|_')
        gt(t,fr,[s,m[1]-s])
        gt(t,fr,[m[0],s+l-m[1]])
      #if s+l < m[1]:
        #print ('x|_|_')
        #gt(t,fr,[s,l])
    if (s >= m[1]) and (s < m[1]+m[2]):
      if s+l > m[1]+m[2]:
        #print ('_|x|x')
        gt(t,fr,[m[0]+(s-m[1]),
          m[2]-(s-m[1])])
        #gt(t,fr,[m[1]+m[2],s+l-(m[1]+m[2])])
      else:
        #print ('_|x|_')        
        gt(t,fr,[m[0]+(s-m[1]),l])
    #if s >= m[1]+m[2]:
        #print('_|_|x')
        #gt(t,fr,[s,l])
    #ns = m[1] + m[2]
    #l = l - (ns-s)     
    #s = ns
    #print('fr',fr)
    if l < 0: 
       break
 if len(fr) == 0:
    #print('adding (0)',n)
    fr.append([n[0],n[1]])
 
 #print('t, len(f)',t,len(fr),fr)
 for f in fr:    
    grt(t,f)
     

dst = []

if True:
 #print(sds)
 for id in range(int(len(sds)/2)):
  #for p in range(2):#sds[id*2+1]):
   nn = [sds[id*2],sds[id*2+1]]
   #print('nn',nn)
   #nn = [36,3]
   #nn = [55,1]
   txl = 0
   if True:#for txl in range(len(bk)-1):
      #print('txl',txl)
      grt(txl+1,nn)
   dst.append(nn)
print('lowest', lx)
