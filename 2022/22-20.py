f = open('22-20.txt').read().split('\n')

# part 1 

# went with a double linked list
# I figured it would be quicker
# than slicing a list. Made a few mistakes
# with moving elements around.
# Also didn't take into account
# that there are multiple elements
# with the same number, ended up
# storing elements as tuples instead

# part 2

# speeded up by rotating my the modulus only, not the full distance
# i.e. 811589153 % (len(list)-1)


def cycl(pt):
 eky = 1
 cyc = 1
 if pt == 2:
     eky = 811589153
     cyc = 10
     
 c = []
 for x in range(len(f)):
    c.append((int(f[x])*eky,x))
    if int(f[x]) == 0:
        zero = (0,x)

 nxtd = {}
 pxtd = {}

 for j in range(len(c)-1):
    nxtd[c[j]] = c[(j+1)%len(c)]
 for j in range(len(c)):
    pxtd[c[j]] = c[(j-1)%len(c)]
 nxtd[c[len(c)-1]] = c[0]
 pxtd[c[0]] = c[len(c)-1]

 p,p1 = c[0]

 for z in range(cyc):
  print z,'of',cyc
  for i in range(len(c)):        
    p,p1 = c[i]     
    n,n1 = p,p1  
    if n != 0:  
        oln,oln1 = nxtd[(n,n1)]
        olp,olp1 = pxtd[(n,n1)]    
        pxtd[(oln,oln1)] = olp,olp1 
        nxtd[(olp,olp1)] = oln,oln1
    if n > 0:           
        for j in range((n+1)%(len(c)-1)):
          p,p1 = nxtd[(p,p1)]     
        pp,pp1 = pxtd[(p,p1)]     
    elif n < 0:                
        for j in range((-n)%(len(c)-1)):
          p,p1 = pxtd[(p,p1)]
        pp,pp1 = pxtd[(p,p1)] 
    if n != 0:
      nxtd[(n,n1)] = (p,p1)
      pxtd[(n,n1)] = (pp,pp1)
      nxtd[(pp,pp1)] = (n,n1)
      pxtd[(p,p1)] = (n,n1)
    
 t = []

 p,p1 = zero
 for cyc in [1,2,3]:
  for x in range(1000):
    p,p1 = nxtd[(p,p1)]
  t.append(p)

 print 'part',pt,'-',sum(t)

#--------------------------
cycl(1)
cycl(2)
