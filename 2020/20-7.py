s = open('20-7.txt').read().split('\n')

# recursive algorthm, algorithm coild be optimised if required

bn,cs,am = [],[],[]

for b in s: #parse
    bn.append(b.split('contain')[0].split('bags')[0][0:-1])
    c = b.split('contain')[1].split()
    cg, ag = [],[]
    for u in range(len(c)/4):
        cg.append(c[u*4+1] + ' ' + c[u*4+2])
        ag.append(int(c[u*4]))
    cs.append(cg)
    am.append(ag)

bgb = [0 for i in bn]

def eb(bgn): #explore bags
  for b in range(len(cs)):
    for cont in cs[b]:
      if cont == bgn:
        bgb[b] = 1
        eb(bn[b])

eb('shiny gold')
print 'part 1 -',sum(bgb)

def obs(i,m): #open bags
   rc = 1
   for sb in range(len(cs[i])):
      for j in range(len(bn)):
         if bn[j] == cs[i][sb]:
             rc += obs(j,am[i][sb])
   return rc*m

for i in range(len(bn)):
    if bn[i] == 'shiny gold':
        print 'part 2 -',obs(i,1)-1
