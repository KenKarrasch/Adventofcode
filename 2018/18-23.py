f = open('18-23.txt').read().split('\n')
# After several failed attempts I landed on this solution.
# Initially I thought the problem was impossible due to the size.  This I tried
# investigating the 8 tips of each bot, then seeing how many others are within
# the points. This gave a solution too small.
# I then did some research and found Bron Kerbosch and Microsoft's Z3 algorithm
# could solve the problem, but could not get my hands on the software.  I plan
# to try implementing a hand coded version of Bron Kerbosch to find a maximum
# clique, Bron Kerbosch psuedocode is on Wikipedia. 

# In the end I went back to my gut instincts and went for a Dichotomous solution.
# I did something similar for my final year thesis at university, in 1996
# This solution splits the solution space into a cube made of eight parts, (call
# them Quadrants, but in 3d). For each quadrant it works out the highest number
# of bots contained within the quadrant, or within range of any part of the
# quadrant. It then stores the quadrant in memory, quadrant, size, botsfound, and
# distance from centre.

# On the next iteration it chooses the next most interesting quadrant, based on
# number of bots, size of quadrant, and distance from the 0,0,0 point, in that order.
# It then splits the interesting quadrant into 8 more quadrants of smaller size,
# and puts them in memory.  The cycle repeats until a quadrant size of 1 is found.

# I believe this is a general solution, however, I am sure how one would prove this.

bots = []
for l in f:
    a = map(int, l.split()[0].split('<')[1].split('>')[0].split(','))
    r = int(l.split('=')[2])
    bots.append([a[0],a[1],a[2],r])

def dist(pt1,pt2):
    return abs(pt1[0]-pt2[0]) + \
           abs(pt1[1]-pt2[1]) + \
           abs(pt1[2]-pt2[2])

def botsinqaudrant(qi,sz):    
    binb = 0
    for b in bots:
      dist = 0
      for d in [0,1,2]:
       dist += abs(qi[d]-b[d])+abs(qi[d]+sz-b[d])-sz     
      if dist/2 <= b[3]:
       binb += 1
    return binb

def cp(qi,sz):
    return [qi[i]+sz/2 for i in [0,1,2]]

def findbestcandidate(c):
    global bimax
    bestbots = 0    
    for opt in c:
      if bestbots < opt[4]:
         bestbots = opt[4]
    smsz = 0
    for opt in c:
     if opt[4] == bestbots:
       if smsz < opt[3]:
         smsz = opt[3]
    cls = 3*bimax+1
    for opt in range(len(c)):
     if c[opt][3] == smsz:
      if c[opt][4] == bestbots:   
       if cls > c[opt][5]:
         cls = c[opt][5]
         return opt
    
def explore(qin,size,totalbots):
  global bimax
  c = [[qin[0],qin[1],qin[2],size,totalbots,3*bimax]]
  while True:
    nxt = findbestcandidate(c)
    qi = [c[nxt][0],c[nxt][1],c[nxt][2]]
    size = c[nxt][3]
    distance = c[nxt][5]
    c = c[0:nxt] + c[nxt+1:]
    if size == 1:
        print 'part 2 -', distance
        return True
    sz = size/2    
    qds = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],
           [1,0,0],[1,0,1],[1,1,0],[1,1,1]]
    for q in range(len(qds)):
        qinq = [qi[0]+qds[q][0]*sz, \
                qi[1]+qds[q][1]*sz, \
                qi[2]+qds[q][2]*sz]
        botct = botsinqaudrant(qinq,sz-1)
        c.append([qinq[0],qinq[1],qinq[2],sz,botct,dist(cp(qinq,sz),[0,0,0])])

count,maxr,bn = 0,0,0
for r in range(len(bots)):
    if maxr < bots[r][3]:
        maxr = bots[r][3]
        bn = r
for n in range(len(bots)):
    if bots[bn][3] >= abs(bots[bn][0] - bots[n][0]) + \
                      abs(bots[bn][1] - bots[n][1]) + \
                      abs(bots[bn][2] - bots[n][2]):
            count += 1
        
print 'part 1 -',count
maxb = 0
for i in bots:
 for dim in [0,1,2]:
  if maxb < i[dim] + i[3]:
      maxb = i[dim] + i[3]
bimax = 1
while bimax < maxb:
  bimax *= 2
quadinside = [-bimax,-bimax,-bimax]
explore(quadinside, 2*bimax, len(bots))
