ls = open('18-12.txt','r').read().split('\n')
# This puzzle is similar to Conways game of life. Keep generating until we get a steady growth rate, then extraploate 50 billion times.  The steady state is similar to a 'walker' in game of life.  The walker drifts to the right adinfinitum.
# At first I was excited when I spotted what appeared to be a factory generating walkers, then despair when the factory appeared to be growing. Then after 109 generations the whole factory turned into a bunch walkers, even better.
pad = '.' * 1000
init = pad + ls[0].split(':')[1][1:]+ pad
rules = []
for r in ls[2:]:
  if r[-1] == '#':
    rules.append(r[:5])
b = init[:]
oldtl, wlker, wlkrun, c = 0,0,0,0
found = False
while not found:
  stg = '..'
  for i in range(2,len(b)-2):
    ry = False
    for r in rules:
       pt = True
       for ch in range(5):
        if b[i-2:i+3][ch] != r[ch]:
            pt = False
       if pt:
           ry = True
    if ry:
           stg = stg + '#'
    else:
           stg = stg + '.'
  b = stg + '..'
  tl = 0
  for i in range(len(b)):
    if b[i] == '#':
        tl += i - 1000
  if wlker == tl - oldtl:
      wlkrun += 1
  else:
      wlkrun =0
  wlker = tl - oldtl
  if c == 19:
      print 'part 1 -', tl
  if wlkrun > 5:
      found = True
      print 'part 2 -', tl + (49999999999 - c) * wlker
  oldtl = tl
  c += 1
