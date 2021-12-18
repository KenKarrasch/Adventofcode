f = open('21-17.txt').read()
# Fun missile launcher puzzle
d = f.split('=')
x1 = int(d[1].split('..')[0])
x2 = int(d[1].split('..')[1].split(',')[0])
x = [x1,x2]
y = [int(i) for i in d[2].split('..')]

def shoot(v,pr):
        hit = False        
        p = [0,0]
        hmax = 0
        while p[1] >= y[0] and p[0] <= x[1] and not hit:
            p[0] += v[0]
            p[1] += v[1]
            v[0] -= 1
            v[1] -= 1
            if v[0] < 0: v[0] = 0
            if x[0] <= p[0] <= x[1] and y[0] <= p[1] <= y[1]:            
                hit = True            
            if pr: print(p)
            if p[1] > hmax:
                hmax = p[1]
        return hit,hmax

i,dys = 1,[] # get y vels that would land in area
while 0.5*i*(i+1) < x[1]:    
    if 0.5*i*(i+1) > x[0]: dys.append(i)
    i += 1
nohits,h,chmx,dym = 0,3,0,0
while nohits < 100:  
# Search an extra 100 high to see if any
# higher velocities are possible.
  hit,hmx = False,0  
  for i in dys:     
    hi, hmx = shoot([i,h],False)
    if hi:
        hit = True  
  if not hit: nohits += 1
  else: nohits = 0
  if hit: 
      chmx = hmx
      dym = h
  h += 1
print('part 1 -',chmx)
hs = 0
for dx in range(min(dys),x[1]+1):
  for dy in range(y[0]-1,dym+1):                    
        hi, hmx = shoot([dx,dy],False)
        if hi: hs += 1
print('part 2 -',hs)   
