f = [int(d) for d in open('19-8.txt').read()]

i,bk = 0,[]
for g in range(100):
  tl = [0,0,0]
  for r in range(150):
    tl[f[i]] += 1
    i += 1
  bk.append(tl)
ly = min([g[0] for g in bk])
for h in range(len(bk)):
  if bk[h][0] == ly: b = h
print 'part 1 -',bk[b][1]*bk[b][2]
fim = f[:]
for g in range(150):
  lst = 0
  for lh in range(100):
    if f[g+(99-lh)*150] != 2:
      lst = f[g+(99-lh)*150]
  fim[g] = lst
print ('part 2 -')
for k in range(6):
   print(fim[k*25:(k+1)*25])
