import copy

#  Part 1 only - very slow, needs optimising, dynamic programming (DP) used to 
#  speed up processing, but is still very slow.
#  bypassed Djkstra algorithm by hard coding the graph.

# Debugging code and test examples left in


#f = open('21-23test.txt').read().split('\n')  # input has been hardcoded, see below

#l3 = f[2]
#l4 = f[3]

minc = [100000000]
msp = ['']

#01 2 3 4 56. vias
#############
#...........#
###D#C#B#C###
  #D#A#A#B#
  #########
#. 1 2 3 4   homes
grp = ['#############',
       '#...........#',
       '###.#.#.#.###',
       '  #.#.#.#.#  ',
       '  #########  ']

# distances p to via (unit cost)
d = [[3,2,2,4,6,8,9],  # home 1
     [5,4,2,2,4,6,7],  # home 2
     [7,6,4,2,2,4,5],  # home 3
     [9,8,6,4,2,2,3]]  # home 4
          
# blockers, these places need to be vacant for a valid move
b = [[[1,2],[2],[3],[3,4],[3,4,5],[3,4,5,6],[3,4,5,6,7]],
     [[1,2,3],[2,3],[3],[4],[4,5],[4,5,6],[4,5,6,7]],
     [[1,2,3,4],[2,3,4],[3,4],[4],[5],[5,6],[5,6,7]],
     [[1,2,3,4,5],[2,3,4,5],[3,4,5],[4,5],[5],[6],[6,7]]]
     
ob = [[[1,0],[4,0]],  # example input
      [[1,1],[3,1]],
      [[2,1],[3,0]],
      [[2,0],[4,1]]]

ob = [[[2,0],[3,0]],  # puzzle input
      [[3,1],[4,0]],
      [[2,1],[4,1]],
      [[1,0],[1,1]]]
#############
#...........#
###D#C#B#C###
  #D#A#A#B#
  #########

ends = [[[1,0],[1,1]],
         [[2,1],[2,0]],
         [[3,1],[3,0]],
         [[4,1],[4,0]]]

tob = [[[1,0],[1,2]],  # test case
         [[2,0],[4,2]],
         [[3,1],[3,0]],
         [[4,1],[4,0]]]
############# # 12081 / 420
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########

tob = [[[1,0],[4,0]],
         [[1,1],[2,2]],
         [[2,1],[3,0]],
         [[2,0],[4,1]]]
############# # 12481 / 40
#...B.......#
###B#C#.#D###
  #A#D#C#A#
  #########
tob = [[[1,0],[4,0]],
         [[1,1],[2,2]],
         [[3,1],[3,0]],
         [[2,0],[4,1]]]
############# # 12081 / 420
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########
iob = [[[1,0],[4,0]],  
         [[1,1],[2,0]],
         [[3,1],[3,0]],
         [[3,2],[4,1]]]
############# # 9051 / 3450?
#.....D.....#
###B#.#C#D###
  #A#B#C#A#
  #########
tob = [[[1,0],[4,0]],
         [[2,2],[2,0]],
         [[3,1],[3,0]],
         [[3,2],[4,1]]]
############# # 9031 / 3470?
#...B.D.....#
###.#.#C#D###
  #A#B#C#A#
  #########
tob = [[[1,0],[4,0]],  
         [[2,1],[2,0]],
         [[3,1],[3,0]],
         [[3,2],[4,1]]]
############# # 9011
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########
tob = [[[1,0],[4,0]], 
         [[2,1],[2,0]],
         [[3,1],[3,0]],
         [[3,2],[4,2]]]
############# # 7011
#.....D.D...#
###.#B#C#.###
  #A#B#C#A#
  #########
tob = [[[1,0],[5,2]], #
         [[2,1],[2,0]],
         [[3,1],[3,0]],
         [[3,2],[4,2]]]
############# # 7008
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########
tob = [[[1,0],[5,2]],
         [[2,1],[2,0]],
         [[3,1],[3,0]],
         [[3,2],[4,0]]]
############# # 4008
#.....D...A.#
###.#B#C#.###
  #A#B#C#D#
  #########
tob = [[[1,0],[5,2]],
         [[2,1],[2,0]],
         [[3,1],[3,0]],
         [[4,1],[4,0]]]
#############  # 8
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########

dp = []  # Dynamic Programming
dpc = [] # store the costs of moving
dpd = [] # Store the depth, (probably don't actually need this)
dpp = [] # Store the pathway for debugging

def pt(ob):  # Print the situation
    mp = [1,2,4,6,8,10,11]
    mpb = [3,5,7,9]
    pg = []
    for i in grp:
      r = []
      for ch in i:
        r.append(ch)
      pg.append(r)          
    for i in range(len(ob)):
      for j in ob[i]:
        if j[1] == 2:
          pg[1][mp[j[0]]] = chr(ord('A') + i)
        else:
          pg[3-j[1]][mpb[j[0]-1]] = chr(ord('A') + i)
    for l in pg:
      st = ''
      for ch in l:
        st += ch
      print(st)

def gd(ltr,ww,d,ob):  
# Check if proposed route is ok
# and nothing is blocking the route.

  gr = [0]*7

  for i in ob:
    for j in i:
      if j[1] == 2:
        gr[j[0]] = 1

  pos = ob[ltr][ww][:]
  # coming back to base
  if d[1] < 2: # going back to home base   
   pos = ob[ltr][ww][:] 
   bl = b[ltr][pos[0]][:]  
   for w in bl:
    # see if anything sitting 
    # on blocker
    if gr[w-1] != 0:
      if w-1 != pos[0]:
        return False
   return True

  # leaving base
  p = d[0]
  pos = ob[ltr][ww][:]
  if pos[1] == 0: 
    # can't move yet because there
    # is one on top of it
    for i in ob:
      if [pos[0],1] in i:
       return False  
  bl = b[pos[0]-1][p][:]
  # get a list of blockers
  for w in bl:
    # see if anything sitting 
    # on blocker
    if gr[w-1] != 0:
      return False
  return True

def home(ob):  # Check if finished
    ct = 0
    for i in [1,2,3,4]:
      for ww in [0,1]:
        for cb in [0,1]:
          if ob[i-1][ww] == ends[i-1][cb]:
            ct += 1    
    if ct != 8:
        return False    
    #pt(ob)
    return True
  
def inob(tg,ob): 
    ii = False
    for i in ob:
        if tg in i:  # lets see if we can move to base bottom
           ii = True
    return ii

def gdests(ltr,ww,ob):
   dests = []
   costs = []
   p = ob[ltr][ww]  # start pos
      
    # Y N Y - Can we move (top)?
    # A A B
    # B A A

   if p[1] == 1:       
     #if p[0] == ltr+1 and ob[ltr][1] == ltr+1:        
     if ob[ltr][0] == [ltr+1,0] or ob[ltr][1] == [ltr+1,0]:                                 
       if ob[ltr][0] == [ltr+1,1] or ob[ltr][1] == [ltr+1,1]:        
            return [],[]

    # N N N N Y- Can we move (bottom)?
    # A A B - -
    # B A A A B

   if p[1] == 0:  
     #if ob[ltr][0] == [ltr+1,0] or ob[ltr][1] == [ltr+1,0]: 
     if p[0] == ltr+1:
       return [],[]

   #if p[0]-1 == ltr and p[1] in [0,1]: # don't go anywhere we are already home
    #    return [],[]
   if p[1] == 0: # If there is a letter on top, then can't move     
     if inob([p[0],1],ob):
         return [],[]     
   if ob[ltr][ww][1] == 2: # letter is out of base area    
     am = d[ltr][p[0]]
     if not inob([ltr+1,1],ob): # taken
       if not inob([ltr+1,0],ob): # taken           
           am += 1
           dests.append([ltr+1,0])
           costs.append(am)
       else:
         if ob[ltr][0] == [ltr+1,0] or ob[ltr][1] == [ltr+1,0]:  # don't place a letter over a bad one
           dests.append([ltr+1,1])
           costs.append(am)
     return dests,costs     
   if ob[ltr][ww][1] < 2: 
     for p in range(7): # If made it this far then the letter is
       # still in the base area, try each of the holding spots       
       free = True       
       for i in ob:         
         if [p,2] in i: 
           free = False
       if free:
           am = d[ob[ltr][ww][0]-1][p]
           if ob[ltr][ww][1] == 0:
               am += 1 #extra step because in lower pos           
           dests.append([p,2])       
           costs.append(am)
   return dests,costs
  
def sch(ob,c,dpth,sp):     # search the possible moves - recursive
  same = True
  nob = copy.deepcopy(ob)
  for i in range(len(ob)):
    for j in range(len(ob[i])):
       if iob[i][j] != ob[i][j]:          
          same = False
  #if same:  
      #print('same')    
      #pt(ob)
      #print(c)
  sob = []  
  for i in ob:
    i.sort(key=lambda row: (row[0], row[1]), reverse=False)
    for j in i:
      sob.append(j)
  #sob.sort(key=lambda row: (row[0], row[1]), reverse=False)
  #if False:
  if sob in dp: # Dynamic Programming DP (aka memo-isation), if this position is 
      #familiar just use previous results stored in DP list
    for i in range(len(dp)):
      if sob == dp[i]:
        if dpth == dpd[i]:
          #ad = copy.deepcopy(dpp[i])
          return c+dpc[i], []#,ad
  if home(ob): 
    if c < minc[0]:
       minc[0] = c 
       msp[0] = []           
    return c,[]#,[[i[:] for i in ob]] #cost
  cs = [1000000] # Worst case if no number is found
  #csp = [[]]
  for ltr in range(4): #letter
    for ww in range(2): #1stor2nd   
      if dpth == 0:
          print('ltr,ww',ltr,ww)   
      if dpth == 1:
          print(ltr,ww)               
      if True: #nothome(ltr,ww,ob):      
       dsts,costs = gdests(ltr,ww,ob)
       #print(ob[ltr][ww],'potential dests ->',dsts)
       for ds in range(len(dsts)):
        #print('attempting move from',ob[ltr][ww],'to',dsts[ds])        
        if gd(ltr,ww,dsts[ds],ob):
          #print('valid move ->',ob[ltr][ww],'to',dsts[ds])                      
          obn = copy.deepcopy(ob)
          obn[ltr][ww] = dsts[ds][:]          
          cost,pth = sch(obn, \
            costs[ds]*(10**ltr),dpth+1,', '+ str(ob[ltr][ww]) + ' to '+ \
                str(dsts[ds])) 
          cs.append(cost)
          #ad = copy.deepcopy(pth)
          #csp.append(ad)
  sob = []  
  for i in nob:
    i.sort(key=lambda row: (row[0], row[1]), reverse=False)  
    for j in i:
      sob.append(j[:])
  dp.append(sob)  # add to the DP list
  dpd.append(dpth)
  
  mn = 10000000
  mi = -1
  for i in range(len(cs)):
    if mn > cs[i]:
      mn = cs[i]
      mi = i
  dpc.append(min(cs))  
  #ad = copy.deepcopy(csp[mi])  
  #ad.insert(0,[i[:] for i in ob])  
  #dpp.append(ad) 
  ad = [] 
  
  return c+min(cs), ad
print('start at:')
pt(ob)
print('end at:')
pt(ends)
p1, p2 = sch(ob,0,0,'')
#print('part 1 -',sch(ob,0,0,''))
print('part 1 -',p1,p2)
for i in range(len(p2)):
  print('move',i+1)
  pt(p2[i]) 
