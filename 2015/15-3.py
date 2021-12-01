f = open('15-3.txt').read()
sz,w = 1000,[0,1]
pr = ['part 1 - ','part 2 - ']
g = [[[0 for i in range(sz)] for i in range(sz)] for y in w]
m,p = [[0,1],[0,-1],[1,0],[-1,0]],[sz/2,sz/2] 
p2 = [p,p]
for k in range(len(f)):
  h = f[k]
  v = [m['><^v'.index(h)][i] for i in w]
  p = [p[i] + v[i] for i in w]
  p2[k%2] = [p2[k%2][i] + v[i] for i in w]
  g[0][p[0]][p[1]] = 1
  for u in w:
    g[1][p2[u][0]][p2[u][1]] = 1
print [pr[e] + str(sum([sum(y) for y in g[e]])) for e in w]
