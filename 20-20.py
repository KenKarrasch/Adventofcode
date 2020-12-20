import math
import copy

# lots of flipping and rotating

# 1) work out which tiles edges match
# other edges
# 2) tiles with only two matching 
# edges are corner pieces -> pt 1
# 3) get a list of tiles that needed
# to be flipped
# 4) flip the tiles then recalculate
# 5) choose the first corner piece plug 
# it into the top left
# 6) work through each other tile
# positioning them in the right lie
# 7) make the final painting
# 8) search for loch ness monster
# 9) try flipping, a rotating 4 ways
# 10) count occurrences of loch
# 11) multiply by 15
# 12) part 2 - subtract from number of #'s

# debug info has been left in


file = '20-20.txt'
f = open(file).read().split('\n\n')

n = []
t = []

flips = [2749, 2129, 2617, 3449, 1553, 3643, 2441, 2969, 1511, 2243, 1613, 2767, 3323, 3797, 1669, 1861, 1129, 2677, 3191, 3727, 2417, 1019, 3001, 1063, 3547, 1621, 2069, 2851, 1907, 1733, 2371, 2089, 3331, 3719, 1447, 1997, 1289, 1277, 3911, 1951, 2297, 1889, 3019, 2699, 3739, 1657, 2791, 3011, 3659, 1831, 3251, 2663, 3527, 2647, 3709, 1489, 1823, 3571, 1523, 2591, 1559, 1303, 2341, 1051, 3691, 1619, 3067]

if file == '20-20test.txt':
    flips = [3079]
flips = []

for tl in f:
    tn = tl.split('\n')
    n.append(tn[0][5:len(tn[0])-1])
    #print tn
    tl = []
    for ln in tn[1:]:
        lnh = []
        for c in ln:
            #print c
            lnh.append(c)
        if tn[0][5:len(tn[0])-1] in flips:            
            tl.append(lnh)
        else:
            tl.append(lnh[::-1])
    t.append(tl)
sz = len(t[0][0])

def hb(c):
    if c == '.':
        return '_'
    return c


def printt(ind,rot):    
    if rot == 0:
     for l in t[ind]:
        stri = ''
        for h in l:
            stri = stri + hb(h)
        print(stri)
    if rot == 1:
     for x in range(sz):  
        stri = ''   
        for y in range(sz):
            stri = stri + hb(t[ind][sz-1-y][x])
        print(stri)
    if rot == 2:
     for x in range(sz): 
        stri = ''    
        for y in range(sz):
            stri = stri + hb(t[ind][sz-1-x][sz-1-y])
        print(stri)
    if rot == 3:
     for x in range(sz) :
        stri = ''    
        for y in range(sz):
            stri = stri + hb(t[ind][y][sz-1-x])
        print(stri)

            
def gete(cl,e,tl):
    sd = []
    for i in range(sz):
        if e == 0:#top
            sd.append(t[tl][0][i])
        if e == 1:#left
            sd.append(t[tl][i][sz-1])            
        if e == 2:#bottom
            sd.append(t[tl][sz-1][sz-1-i])
        if e == 3:#right
            sd.append(t[tl][sz-1-i][0])
    if cl:
        return sd
    else:
        return sd[::-1]

def getoptions():
 tb = [] # Book of possible matching tiles
 for t1 in range(len(t)):
  tm = []
  for s1 in [0,1,2,3]:    
    for t2 in range(len(t)):
      if t1 != t2:
        for s2 in [0,1,2,3]:#side
          for f in [True,False]:#flip
            if gete(True,s1,t1) == gete(f,s2,t2):                
                mt = True
                tm.append([n[t2],s2,f,s1,n[t1],t1,t2]) # matching tile, side number, flipped
  tb.append(tm)
 return(tb)


tb = getoptions()
m = 1
g = [[[0,0,False] for i in range(sz)]  for j in range(sz)] 
# tilenumber, rotation



side = []
# Find the first tile with two matching edges only
m = 1
for i in range(len(tb)):
    if len(tb[i]) == 2:
        m *= int(n[i])
        st = i
        print(tb[i])
        for sds in tb[i]:
            side.append(sds[3])
        break


print('st,side',n[st],side) 

# Find the Top Left tile
rot = -1
fl = False # Flip on vertical axis
for i in [0,1,2,3]:    
    if ((side[0]+i)%4 == 1) and ((side[1]+i)%4 == 2):
        rot = i
        fl = False        
    if ((side[0]+i)%4 == 3) and ((side[1]+i)%4 == 2):
        rot = i
        fl = True

g[0][0] = [n[st],rot,fl]

print('start tile',g[0][0])

flst = {}
flst[n[st]] = fl

def fliptiles(tl,fl,depth): # Recursively search the grid looking for flipped tiles
    flip = False
    #print(tl,fl,depth)
    #print('flst',flst)
    if(depth < 1000):
      for i in range(len(tb)):
        if i == tl:            
            for j in tb[i]:
                #print(' '*depth,j)
                if j[0] not in flst.keys():
                    #print('new tile',j[0])
                    if (fl and j[2]) or ((not fl) and (not j[2])):
                        flip = False
                        flst[j[0]] = False
                    else:
                        flip = True
                        flst[j[0]] = True                    
                    fliptiles(j[6],flip,depth+1)

print('getting flips ------')
fliptiles(st,fl,0)
print(flst)
stri = ''
for i in flst:    
    if flst[i]:
        stri = stri + ', ' + i
        print(i)
print(stri)

t = []
for tl in f:  # Read the whole thing in again, this time flipping the offending
            # They were doing my head in
    tn = tl.split('\n')
    name = tn[0][5:len(tn[0])-1]
    n.append(name)
    flip = False
    if flst[name]:
        print('name',name,'flipped')
        flip = True    
    tl = []
    for ln in tn[1:]:
        lnh = []
        for c in ln:
            lnh.append(c)
        if flip:
            tl.append(lnh[::-1])
        else:
            tl.append(lnh)
    t.append(tl)


def getoptions2():
 tb = [] # Book of possible matching tiles
 for t1 in range(len(t)):
  tm = []
  for s1 in [0,1,2,3]:    
    for t2 in range(len(t)):
      if t1 != t2:
        for s2 in [0,1,2,3]:#side
            if gete(True,s1,t1) == gete(False,s2,t2):                
                mt = True
                tm.append([n[t2],s2,False,s1,n[t1],t1,t2]) # matching tile, side number, flipped
  tb.append(tm) 
 return(tb)


gsz = int(math.sqrt(len(tb)))
print('gsz',gsz)

tb = []
tb = getoptions2()
m = 1
g = [[[0,0,False,''] for i in range(gsz)]  for j in range(gsz)] 
# tilenumber, rotation

side = []
# Find the first tile with two matching edges only
for i in range(len(tb)):
    if len(tb[i]) == 2:
        st = i
        #print(tb[i])
        for sds in tb[i]:
            side.append(sds[3])
        break

print('st,side',n[st],side) 

# Find the Top Left tile
rot = -1
fl = False # Flip on vertical axis
print('side',side)
for i in [0,1,2,3]:    
    if ((side[0]+i)%4 == 1) and ((side[1]+i)%4 == 2):
        rot = i
        fl = False        
    if ((side[0]+i)%4 == 2) and ((side[1]+i)%4 == 1):
        rot = i
        fl = True

print('rot',rot)
g[0][0] = [st,rot,True,n[st]]

def getright(x,y):    
    
    rot = g[x][y][1]
    tn = g[x][y][0]
    print('get right')
    for i in tb[tn]:
        print('i',i)
        if (i[3]+rot)%4 == 1:
            return i[6],(3-i[1])%4

def getdown(x,y):
    rot = g[x][y][1]
    tn = g[x][y][0]
    print('get down')
    for i in tb[tn]:
        print('i',i)
        if (i[3]+rot)%4 == 2:
            return i[6],(4-i[1])%4
    
    
#[n[t2],s2,False,s1,n[t1],t1,t2]

for el in range(1,gsz*gsz):
    x = el%gsz
    y = int(math.floor(el/gsz))
    print('x,y',x,y)
    if x != 0:
        tn,rt = getright(x-1,y)        
        print(n[tn],rt)
        print(x,y)
        g[x][y] = [tn,rt,True,n[tn]]
    else:
        tn,rt = getdown(x,y-1)
        g[x][y] = [tn,rt,True,n[tn]]

print('g',g)
print('look at first row to confirm they are lining up')
for i in range(gsz):
    print(' ')
    printt(g[0][i][0],g[0][i][1])

ec = 0
cnrs = 0
print('matches between edges')
if True:
  for i in range(len(tb)):    
    print(n[i])
    for j in tb[i]:
        print(j)
    if len(tb[i]) == 2:
        m *= int(n[i])
        cnrs *= 1
    if len(tb[i]) == 3:
        ec += 1
    print(len(tb[i]))
print(ec,'edges')
print(cnrs,'corners')
print(m)

def printgp(gp):
 for ln in gp:
    stri = ''
    for c in ln:
        stri = stri + hb(c)
    print(stri)

def rotate(grid,rt):
    sz = len(grid[0])
    gridn = [['.' for x in range(sz)] for y in range(sz)]
    if rt == 0:
     for x in range(sz):  
        for y in range(sz):
            gridn[x][y] = grid[x][y]
    if rt == 1:
     for x in range(sz):  
        for y in range(sz):
            gridn[x][y] = grid[sz-1-y][x]
    if rt == 2:
     for x in range(sz): 
        for y in range(sz):
            gridn[x][y] = grid[sz-1-x][sz-1-y]
    if rt == 3:
     for x in range(sz) :
        for y in range(sz):
            gridn[x][y] = grid[y][sz-1-x]
    return gridn
    
    
def flip(grid,fp):
    sz = len(grid[0])
    gridn = [['.' for x in range(sz)] for y in range(sz)]
    if fp:
     for x in range(sz):  
        for y in range(sz):
            gridn[x][y] = grid[x][sz-1-y]
    else:
        gridn = copy.deepcopy(grid)
    return(gridn)
            

gp = [['_' for i in range(gsz*(sz-2))]  for j in range(gsz*(sz-2))] 

for x in range(gsz):
    for y in range(gsz):
        tl = g[x][y][0]
        ngr = rotate(t[tl],g[x][y][1])
        for x1 in range(sz-2):
            for y1 in range(sz-2):
                gp[y*8+x1][x*8+y1] = ngr[x1+1][y1+1]

print('the final painting')
printgp(gp)


#loch = open('loch.txt').read().split('\n')[1:]

#print(loch)

loch = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']

for i in loch:
  s = ''
  for c in i:
      if c == ' ':
          s = s+'_'
      else: s = s+c
  print s

ly = range(len(loch[0]))
lx = range(len(loch))
print(loch,lx,ly)
lochs = 0
lcs = []
gpc = 0
ps = len(gp)

rct = 0
for x in range(ps):
   for y in range(ps):
       if gp[x][y] == '#':
           rct += 1
print('number of #s',rct)

for fp in [True,False]:
 for rs in [0,1,2,3]:
  ngp = flip(rotate(copy.deepcopy(gp),rs),fp)
  for x in range(ps):
   for y in range(ps):
    lm = True
    ds = False
    for x1 in lx:
      for y1 in ly:
        if x+x1 < ps:
          if y+y1 < ps:
           if loch[x1][y1] == '#':
            if ngp[x+x1][y+y1] == '.':
             lm = False
          else: ds = True
        else: ds = True
    if lm and not ds:
        lcs.append([fp,rs,x,y])
        lochs += 1
print('lochs found',lochs)
print('where loch found [flipped,rotated by, x & y coords] -',lcs)
print('part 1 -',m)
print('part 2 -',rct - (lochs*15))
