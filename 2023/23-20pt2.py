from collections import defaultdict
import math

# Fun one, Look at RX conjuction contributors, &dl, &fr, &rv, &bt, work out how often they give a pulse.
# wait for the planets to align, ie. work out lowest common multiple, (LCM)

f = open('23-20.txt').read().split('\n')

m = {}

wfs = {} #workflows
for line in f:  
  c = line.split('->')
  st = c[0].strip()
  op = [y.strip() for y in c[1].split(',')]  
  wfs[st] = op
  m[st[1:]] = st[0]

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (ans*x)//math.gcd(x,ans)
  return ans

back = defaultdict(list)
lct,hct = 0,0

pls = []
states = set()
st = {}

for stt,dst in wfs.items():   
  nys = []
  for e in dst:    
    ny = e
    if e in m:
      ny = m[e]+e
    nys.append(ny)    
  wfs[stt] = nys
  for sts in wfs[stt]:
    if sts[0]=='&':
      if sts not in st:
        st[sts] = {}
      st[sts][stt] = 'low'
    back[sts].append(stt)

dn = False


b = back['rx']
camps = []
for i in b:
  camps = back[i]

print('camps',camps)

prevt = []
cycles = []
for i in range(len(camps)):
  prevt.append(0)
  cycles.append(0)
print(cycles)

t = 0
ct = 0
while not dn:  
  pls.append(('broadcaster', 'button', 'lp'))

  while len(pls) != 0:    
    b, stt, md = pls.pop(0)
    #print(b)
    for i in range(len(camps)):
      if camps[i] in b:
       if md == 'lp':
        if prevt[i] == 0:
          prevt[i] = t
        else: 
          cycles[i] = t - prevt[i]
    z = True
    for i in cycles:
      if i == 0:
        z = False        
    if z: dn = True  

    if b=='broadcaster':
      for y in wfs[b]:
        pls.append((y, b, md))
    
    if md=='lp': lct += 1
    else: hct += 1
    
    if b not in wfs: continue

    elif b[0]=='%':
      if md=='hp':
        continue
      else:
        if b in states:
          states.discard(b)
          nt = 'lp'          
        else:
          states.add(b)
          nt = 'hp'
        for y in wfs[b]:
          pls.append((y, b, nt))

    elif b[0]=='&':
      st[b][stt] = md
      nt = 'lp'
      for y in st[b].values():
        if y != 'hp':
          nt = 'hp'
      for y in wfs[b]:
        pls.append((y, b, nt))
  ss = '&rv'
  if 'ss' in states:
    print('ss',t)
    dn = True
  #print(states)
  if t%1000==0: print(t)
  t += 1
print('part 1',lct*hct)
print('part 2',lcm(cycles))
