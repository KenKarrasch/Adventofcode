f = open('23-20.txt').read().split('\n')
m = {}
wfs = {} #workflows
for line in f:  
  c = line.split('->')
  st = c[0].strip()
  op = [y.strip() for y in c[1].split(',')]  
  wfs[st] = op
  m[st[1:]] = st[0]

lct,hct = 0,0  # high/low counts

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

for t in range(1000):
  pls.append(('broadcaster', 'button', 'lp'))

  while len(pls) != 0:    
    b, stt, md = pls.pop(0)
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
print('part 1',lct*hct)
