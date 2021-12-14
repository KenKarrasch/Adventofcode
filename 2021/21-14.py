f = open('21-14.txt').read().split('\n')
# Strategy was to set a dictionary of letter pairs e.g. AC -> B
# becomes d['AC'] = {'AB', 'BC'}
# Then set up a dictionary of how often the letter pairs appear in the
# sequence.  e.g. sequence ABC would be repesented as
#  t = {'AA' : 0, 'AB' : 1, 'AC': 0,
#       'BA' : 0, 'BB' : 0, 'BC': 1,
#       'CA' : 0, 'CB' : 0, 'CC': 0}
# Then on the next iteration substitute in new pairs to get a running 
# tally of letter pairs.
# 
# At the end of the iterations the tally of letter pairs
# can be used to see how often a letter appears.

s = f[0]
rl,cl = [],{}
for i in f[2:]:
    r = i.split(' -> ')
    rl.append([r[0],r[1]])
    cl[i[0][0]] = 0

def getpr(sq):
  for i in rl:
    if i[0] == sq:
      return [sq[0]+i[1],i[1]+sq[1]]

pr = {} #dictionary of pairs that spawn from a pair 
fc = {} # final tally of pairs
for i in cl.keys(): # Set up pairs table
  for j in cl.keys():    
    pr[i+j] = getpr(i+j)
    fc[i+j] = 0
pz = fc.copy()
for pt in [10,40]:
 for e in range(len(s)-1): # go through each pair of letter in input string
  lc = pz.copy() #  set up local tally 
  lc[s[e] + s[e+1]] = 1
  for ct in range(pt): # iterate pt (10 and 40) times
   n = pz.copy()
   for e in pr.keys(): # get the two new pairs from the dictionary
    if lc[e] > 0:  # add them to the local tally
     for i in pr[e]:
      n[i] += lc[e]  
   lc = n.copy()
  for y in pr.keys():
   fc[y] += lc[y]  # add the local tally to the final count
 sts = list(fc.keys())
 sts.append(s[-1]) # add last letter
 sta = list(fc.values())
 sta.append(1)
 res = {}
 for i in range(len(sts)): res[sts[i][0]] = 0 # count the letters, grab first letter in each pair
 for i in range(len(sts)): res[sts[i][0]] += sta[i]
 rs = list(res.values()) 
 print('part',pt,'-',max(rs)-min(rs))
