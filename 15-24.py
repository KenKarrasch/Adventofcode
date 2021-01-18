f = [int(x) for x in open('15-24.txt').read().split('\n')]
# There are many possible shortcuts, this solution
# takes time to prove the results 
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
            
gf(f[::-1],0,1,[],t,depth[0])
qel.sort()
print ('part 1 -',qel[0])
qel = []
depth[0] = len(f)
gf(f[::-1],0,1,[],q)
qel.sort()
print ('part 2 -',qel[0])
