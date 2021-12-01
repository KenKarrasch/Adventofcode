f = [int(x) for x in open('15-24.txt').read().split('\n')]
# There are many possible shortcuts, this solution
# takes time to prove the results, take about 30 seconds to run
t = sum(f)/3
q = sum(f)/4
tly = [0]
qel = []
depth = [len(f)]

def okay(nf,sm,gr,t):    
    if sm > t:
      return False
    if t-sm in nf:
      return True   
    if sm == t:        
      return True   
    ng = nf[:]
    for i in range(len(ng)):       
       if okay(ng[:i]+ng[i+1:],sm+ng[i],gr,t):
         if gr > 3:
           if okay(ng[:i]+ng[i+1:],sm+ng[i],gr-1,t):
             return True
           return False
         return True
    return False

def gf(nf,sm,qe,st,spl):
    if len(st) == depth[0]:
        tly[0] += 1
        if tly[0]%1000000==0:
          print (tly[0])
    if sm == spl:
        st.sort()
        if [qe,st] not in qel:
           qel.append([qe,st])
           print (st)
           if depth[0] > len(st):
              depth[0] = len(st)
        return False
    if sm > spl:
        return False
    if len(st) < depth[0]:
      for b in range(len(nf)):         
         gf(nf[:b]+nf[b+1:],sm+nf[b],qe*nf[b],st+[nf[b]],spl)   

def subt(nnf,st):
    nf = nnf[:]
    for p in st:
      popped = False
      for n in range(len(nf)):       
       if not popped:   
        if p == nf[n]:
          nf.pop(n)
          popped = True
    return nf
            
gf(f[::-1],0,1,[],t)
p1 = ''
qel.sort()
p1,done = '',False
for qp in qel:
  if not done:    
    nf = subt(f[:],qp[1])
    if okay(nf,0,3,t):      
      p1 = 'part 1 - ' + str(qp[0])
      done = True
qel = []
depth[0] = len(f)
gf(f[::-1],0,1,[],q)
qel.sort()
p2,done = '',False
for qp in qel:
  if not done:    
    nf = subt(f[:],qp[1])
    if okay(nf,0,4,q):      
      p2 = 'part 2 - '+str(qp[0])
      done = True
print (p1)
print (p2)
