f = open('15-5.txt').read().split('\n')
bd = ['ab','cd','pq','xy']
gs = 0
for st in f:
 v = 0
 p = ''
 r = False
 bl = False
 for c in st:
  if c in 'aeiou':
    v += 1
  if p == c:
    r = True
  p = c
 for b in bd:
   if b in st:
    bl = True
 if v > 2 and not bl and r:
    gs += 1
print 'part 1 - ',gs
v = 0
for st in f:
 r = False
 d = False
 for c in range(len(st)-2):
   if st[c:c+2] in st[0:c] or \
      st[c:c+2] in st[c+2:]:
    d = True
   if st[c] == st[c+2]:
    r = True
 if r and d:
  v += 1
print 'part 2 -',v
