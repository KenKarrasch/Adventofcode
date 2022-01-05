import time
import copy

# Part 2 only - Made some optimisations on the part 1 code
#  
# - if an amphipod can get to a room, do that and dont consider any other options
# - if searching if a previously found path used less energy dont bother searching 
#    anymore.
#
#  Also noticed I had processed some things multiple times, so deleted those.
#
#  Still takes a very long time to process.
#  
#  These optimisations made it quicker by about 10 fold.
#
#  Converting from 2 deep rooms to 4 deep rooms was straightforward. Was quite 
#  surprised my code worked first time.
#  
#  Still hard coded, maybe I will write code to read in the test file later.
#  Debugging code and test examples left in
#
# f = open('21-23test.txt').read().split('\n')  # input has been hardcoded, see below

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
       '  #.#.#.#.#  ',
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
     
tob = [[[1,0],[4,0],[4,2],[3,1]],  # example input
      [[1,3],[3,3],[2,1],[3,2]],
      [[2,3],[3,0],[2,2],[4,1]],
      [[2,0],[4,3],[1,1],[1,2]]]

ob = [[[2,0],[3,0],[3,1],[4,2]],  # puzzle input
      [[2,1],[3,2],[3,3],[4,0]],
      [[2,2],[2,3],[4,1],[4,3]],
      [[1,0],[1,1],[1,2],[1,3]]]
#############
#...........#
###D#C#B#C###
  #D#C#B#A#
  #D#B#A#C#  
  #D#A#A#B#
  #########

ends = [[[1,0],[1,1],[1,2],[1,3]],
         [[2,0],[2,1],[2,2],[2,3]],
         [[3,0],[3,1],[3,2],[3,3]],
         [[4,0],[4,1],[4,2],[4,3]]]

# tobs are debugging datasets
tob = [[[1,0],[0,4],[1,4],[4,0]],
      [[1,3],[2,1],[4,4],[5,4]],
      [[2,2],[3,0],[3,1],[4,1]],
      [[1,1],[1,2],[2,0],[6,4]]]
############# # 40481
#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#
  #########
tob = [[[1,0],[0,4],[1,4],[5,4]],
      [[2,0],[2,1],[2,2],[2,3]],
      [[3,0],[3,1],[3,2],[3,3]],
      [[4,0],[1,1],[1,2],[6,4]]]
############# # 25016
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########
tob = [[[1,0],[1,1],[1,2],[5,4]],
      [[2,0],[2,1],[2,2],[2,3]],
      [[3,0],[3,1],[3,2],[3,3]],
      [[4,0],[4,1],[2,4],[6,4]]]
############# #10008
#...D.....AD#
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########
tob = [[[1,0],[1,1],[1,2],[5,4]],
      [[2,0],[2,1],[2,2],[2,3]],
      [[3,0],[3,1],[3,2],[3,3]],
      [[4,0],[4,1],[4,2],[6,4]]]
############# #3008
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
tob = [[[1,0],[1,1],[1,2],[1,3]],
      [[2,0],[2,1],[2,2],[2,3]],
      [[3,0],[3,1],[3,2],[3,3]],
      [[4,0],[4,1],[4,2],[6,4]]]
############# #3000
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

dp = []  # Dynamic Programming
dpc = [] # store the costs of moving
hits = [0]
bs = [1000000000]

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
        if j[1] == 4:
          pg[1][mp[j[0]]] = chr(ord('A') + i)
        else:
          pg[5-j[1]][mpb[j[0]-1]] = chr(ord('A') + i)
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
      if j[1] == 4:
        gr[j[0]] = 1

  pos = ob[ltr][ww]
  # coming back to base
  if d[1] < 4: # going back to home base     
   bl = b[ltr][pos[0]]  
   for w in bl:
    # see if anything sitting 
    # on blocker
    if gr[w-1] != 0:
      if w-1 != pos[0]:
        return False
   return True

  # leaving base
  p = d[0]    
  for lv in range(pos[1]+1,4):
    # can't move yet because there
    # is one on top of it
    for i in ob:
      if [pos[0],lv] in i:
       return False  

  bl = b[pos[0]-1][p]
  # get a list of blockers
  for w in bl:
    # see if anything sitting 
    # on blocker
    if gr[w-1] != 0:
      return False
  return True


def home(ob):  # Check if finished
    ct = 0
    for i in [0,1,2,3]:
      for ww in [0,1,2,3]:
        for cb in [0,1,2,3]:
          if ob[i][ww] == ends[i][cb]:
            ct += 1    
    if ct != 16:
        return False        
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
     
    
   # check if already home, i.e. make sure itself and anything below is already in the correct column 
   if p[1] < 4:    
    if p[0] == ltr+1: # Make sure it is the correct letter
     tl = 0
     for lt in range(p[1]+1):         
      lp = False
      for ln in range(4):             
        if ob[ltr][ln] == [ltr+1,lt]:
          lp = True
      if lp: 
          tl += 1
     if tl == p[1]+1:
      return [],[]  
        
   if ob[ltr][ww][1] == 4: # letter is out of base area, therefore going to base area   
    ks = True  # make sure that only the correct letters exist in base area
    for lv in range(4): 
      for lt in range(4): 
        if lt != ltr:
          if [ltr+1,lv] in ob[lt]:
            ks = False        
    if ks:  # See how deep to go
     am = d[ltr][p[0]]
     deep = 0
     for ld in range(4)[::-1]:
       if not inob([ltr+1,ld],ob):
         deep = ld
     if gd(ltr,ww,[ltr+1,deep],ob):
           am += (4-1)-deep
           dests.append([ltr+1,deep])
           costs.append(am)
     return dests,costs   

   if ob[ltr][ww][1] < 4: 
     for p in range(7): # If made it this far then the letter is
       # still in the base area, try each of the holding spots       
       free = True       
       for i in ob:         
         if [p,4] in i: 
           free = False
       if free:
         if gd(ltr,ww,[p,4],ob):
           am = d[ob[ltr][ww][0]-1][p]
           am += (4-1) - ob[ltr][ww][1]       
           #if ob[ltr][ww][1] == 0:
           #    am += 1 #extra step because in lower pos           
           dests.append([p,4])       
           costs.append(am)   
   return dests,costs
  
def sch(ob,c,dpth,dc):     # search the possible moves - recursive 
  #pt(ob)      
  sob = []  
  for i in ob:
    i.sort(key=lambda row: (row[0], row[1]), reverse=False)
    for j in i:
      sob.append(j[:])      
  if sob in dp: # Dynamic Programming DP (aka memo-isation), if this position is 
      #familiar just use previous results stored in DP list
    for i in range(len(dp)):
      if sob == dp[i]:                  
        return c+dpc[i]
  if home(ob): 
      if dc < bs[0]:
          print ('best solution',bs[0])
          bs[0] = dc
      return c
  cs = [1000000] # Worst case if no number is found    
  destdb = []
  hofd = False  
  for ltr in range(4): #letter
    for ww in range(4): #1stor2nd              
      if not hofd:
        dsts,costs = gdests(ltr,ww,ob)               
        if len(dsts) > 0:                 
          for ds in dsts:            
            if ds[1] in [0,1]:          
             destdb = []
             hofd = True
          destdb.append([dsts,costs,ltr,ww]) 
  #print(destdb)        
  for i in destdb:          
    ltr,ww = i[2],i[3]
    dsts,costs = i[0],i[1]
    if dpth == 0:
      print('ltr,ww',ltr,ww)   
    if dpth == 1:
      print(ltr,ww)  
    for ds in range(len(dsts)):    
          if dpth == 0:
            print('dst',dsts[ds])               
          obn = copy.deepcopy(ob)
          obn[ltr][ww] = dsts[ds][:]                    
          cost = 10000000000
          if dc+costs[ds]*(10**ltr) < bs[0]:
            cost = sch(obn, costs[ds]*(10**ltr),dpth+1,dc+costs[ds]*(10**ltr))   
          else:  hits[0] += 1               
          cs.append(cost)        
  
  dp.append(sob)  # add to the DP list
  dpc.append(min(cs))  
  return c+min(cs)

print('start at:')
pt(ob)
print('end at:')
pt(ends)
tst = time.time() * 1000
p1 = sch(ob,0,0,0)
tfn = time.time() * 1000
print('part 2 -',p1,len(dp),tfn-tst,'msecs',hits[0])
