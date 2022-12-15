import re
f = open('22-15.txt').read().split('\n')

# Started late due to Christmas shopping
#
# I did the slow solution and was taking a few minutes for part A, so I went for a better solution
# The best way I could think of was to find the intersection points of each diamond.
# then sorted them, then see where they overlap and rationalise, then added them up.
# Turned out a beacon was on my 2000000 line, so I had an 'off by one' error
# 
# Doing the part 2 - (4 million lines) takes a few minutes.

# PART 1-------------------------

l = 2000000

def md(n1,n2):
    return abs(n1[0]-n2[0]) + abs(n1[1]-n2[1])

g = []
d = []
lm = []
rm = []
cd = []
for i in f:
    sb = [int(x) for x in re.findall('-?[0-9]+', i)]
    cd.append(sb)
    ds = abs(sb[0]-sb[2]) + abs(sb[1]-sb[3])
    d.append(ds)
    lm.append(sb[0]-ds)
    rm.append(sb[0]+ds)

bs = []
for i in cd:
    if i[1] == l:
        nb = [i[1],i[1]]
        if nb not in bs:
            bs.append(nb)
         
    if i[3] == l:
        ns = [i[2],i[3]]
        if ns not in bs:
            bs.append(ns)

st = ''
ct = 0
ov = []
for dr in range(len(cd)):
 if abs(cd[dr][1] - l) < d[dr]:
    vs = d[dr] - (abs(cd[dr][1] - l))
    ov.append([cd[dr][0]-vs,cd[dr][0]+vs])

ed = []

def added(ned):
    if ned not in ed:
        ed.append(ned)

for i in ov:
    added(i[0])
    added(i[1]+1)

ed.sort()

cv = [False]*len(ed)

for i in ov:
  for e in range(len(ed)):
    if ed[e] >= i[0]:
      if ed[e] < i[1]:
        cv[e] = True

ct = 0
for i in range(len(cv)-1):
    if cv[i]:    
        ct += ed[i+1] - ed[i]

print('part 1 -',ct- len(bs))

# bad guesses
# 6220655 too high
# 5176945 too high
# 5176945 too high

# PART 2-------------------------

st = ''
ct = 0
ov = []
l = 10
wd = []
#for l in [2933732]:#range(4000000):
for l in range(4000000):
 if l%10000==0:
    print('scanned ',l,'lines of 4,000,000')
 ov = []   
 for dr in range(len(cd)):
  if abs(cd[dr][1] - l) < d[dr]:
    vs = d[dr] - (abs(cd[dr][1] - l))

    ov.append([cd[dr][0]-vs,cd[dr][0]+vs])

 ed = []

 def added(ned):
    if ned not in ed:
        ed.append(ned)

 for i in ov:
    added(i[0])
    added(i[1]+1)

 ed.append(0)
 ed.append(21)
 ed.append(4000001)
 ed.sort()

 cv = [False]*len(ed)

 for i in ov:
  for e in range(len(ed)):
    if ed[e] >= i[0]:
      if ed[e] < i[1]:
        cv[e] = True

 ct = 0
 for i in range(len(cv)-1):
  if ed[i] >= 0:
   if ed[i] < 4000001:
    if cv[i]:    
        ct += ed[i+1] - ed[i]
    else:
        #print('distress point found - ',l,ed[i]) # x,y
        ansx = ed[i]
        ansy = l
        print('part 2 -',(ansx*4000000) + l)
 
 wd.append([ct,l])

# answer for my input - 13350458933732 , y=2933732 x=3337614
