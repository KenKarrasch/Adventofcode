f = open('16-6.txt').read().split('\n')

ms,ms2 = '',''
sz = 26
a,sz = ord('a'),26
for lt in range(len(f[0])):
  g = [[0,x] for x in range(sz)]
  for i in f:
    g[ord(i[lt])-a][0] += 1
  g.sort(reverse=True)
  ms += chr(g[0][1]+a)
  for i in g:
      if i[0] != 0:
          lc = chr(i[1]+a)
  ms2 += lc
print 'part 1 -',ms
print 'part 2 -',ms2
