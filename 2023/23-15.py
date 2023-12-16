f = open('23-15.txt').read().split(',')

def hsh(i):
    n = 0
    for c in i:
        n += ord(c)
        n *= 17
        n = n%256
    return n

s = []
for i in f:
    n = hsh(i)
    s.append(n)

ln = [[] for i in range(256)]

for r in range(len(f)):
  i = f[r]
  if '-' in i:
    si = i.split('-')[0]
    n = hsh(si)
    ls = ln[n]
    oj = -1
    for j in range(len(ls)):
      if si == ls[j].split('=')[0]:
        oj = j
    if oj != -1:
         ls.pop(oj)
    ln[n] = ls
      
  if '=' in i:
    fd = False
    si = i.split('=')[0]
    n = hsh(si)
    ls = ln[n][:]
    nj = -1
    for j in range(len(ls)):
      if si == ls[j].split('=')[0]:
         nj = j
    if nj != -1: ls[nj] = i
    if nj == -1:
        ls.append(i)
    ln[n] = ls

ct = 0
for i in range(len(ln)):
   for j in range(len(ln[i])):
      nm = int(ln[i][j].split('=')[1])
      ct += (i+1)*(j+1)*nm

print ct

# 305030 too high
# 306503 too high


