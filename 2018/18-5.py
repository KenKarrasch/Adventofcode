def plen(n,b,st):
  str = ''
  ind = st
  while ind < len(b):
    str = str + b[ind]
    ind = n[ind]
  return len(str)

f = open('18-5.txt','r')
letter = ''
fb = f.read()
min = len(fb)
for lt in '&abcdefghijklmnopqrstuvwxyz':
  b = ''
  for p in fb:
    if ord(p) != ord(lt) and ord(p) + 32 != ord(lt):
        b = b + p
  n = range(1,len(b))
  n.append(len(b))
  p = [-1] + range(len(b))
  start = 0
  g = 0
  while n[g] < len(b):
    d = ord(b[g]) - ord(b[n[g]])
    if d == 32 or d == -32:
        prev = p[g]
        next = n[n[g]]
        if prev > -1:
          n[prev] = next
        p[next] = prev
        if prev >= start:
          g = prev
        else:
          g = next
          start = next
    else:
      g = n[g]
  plength = plen(n,b,start)
  if plength < min:
      min = plength
      letter = lt
  if lt == '&':
      print 'part 1 -',plength
print 'part 2 -',min
