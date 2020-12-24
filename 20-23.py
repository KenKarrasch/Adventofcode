# Started out using an array to swap around memory bits, but found it was too slow,
# It would have taken about a year to calculate.

# Made use of 'dict' class data structure to implement a linked list, very quick
# to access its elements.  Quick to reference the destination (which was killing
# the array implementation).  No idea how they got the dict array to work so fast, probably
# some sort of hashing function I guess.  Made use tuple for swapping links around.
# pypy calculates an answer pt1&2 in about 1.5 secs.
# I had an 'out by one' error, which costed some time.

file = '20-23.txt'
f = open(file).read()

def pl():
    ref = c[0]
    st = ''
    sta = []
    for i in range(ln):
        st = st + str(nxtd[ref])
        ref = nxtd[ref]
        sta.append(ref)
    return sta
    
def calc(cycles):
  i,cnr = 0,c[0]  
  while i < cycles:
    i += 1
    pu,epu = [],cnr    
    for j in [1,2,3]:
        pu.append(nxtd[epu])
        epu = nxtd[epu]
    nxtd[cnr] = nxtd[pu[2]]        
    d = cnr-1    
    for n in [0,1,2]:
      for m in [0,1,2]:
          if d == pu[m]:
            d -= 1
          if d == 0:
            d = ln
    nxtd[d],nxtd[pu[2]] = (pu[0],nxtd[d])
    cnr = nxtd[cnr]    
    if i%100000==0:
        print(i,'of 10,000,000')

c = [int(x) for x in f]
ln = len(c)
nxtd = {}
for j in range(len(c)-1):
    nxtd[c[j]] = c[j+1]
nxtd[c[len(c)-1]] = c[0]
nxt = [x for x in range(1,ln)]
nxt.append(0) # completed circle, link back to first element
calc(100)
co = pl()
for y in range(ln):
    if co[y] == 1:
        b = co[y:] + co[0:y]
stri = ''
for x in b[1:]:
    stri = stri + str(x)
c = c + [x for x in range(10,1000001)]
ln = len(c)
nxtd = {}
for j in range(len(c)-1):
    nxtd[c[j]] = c[j+1]
nxtd[c[len(c)-1]] = c[0]
nxt = [x for x in range(1,ln)]
nxt.append(0)
calc(10000000)
one = nxtd[1]
two = nxtd[nxtd[1]]

print('part 1 -',stri)
print('part 2 -',one*two)
