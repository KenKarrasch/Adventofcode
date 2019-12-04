f = [int(n) for n in open('19-4.txt').read().split('-')]

def cons(n):
    pr = 0
    for h in str(n):
        if pr > int(h):
            return False
        pr = int(h)
    return True

def adj(n):
    pr = ''
    for k in str(n):
      if k == pr:
          return True
      pr = k
    return False
    
def ladj(j):
      n = str(j)
      if n[0] == n[1]:
        if n[0] != n[2]:
          return True
      if n[4] == n[5]:
        if n[3] != n[4]:
          return True
      for k in [1,2,3]:
        if n[k] == n[k+1]:
          if n[k] != n[k-1]:
            if n[k] != n[k+2]:
              return True
      return False

ct1, ct2 = 0,0
for i in range(f[1]-f[0]):
    n = f[0]+i
    if cons(n):
     if adj(n):
       ct1 += 1
       if ladj(n):
        ct2+=1
print 'part 1 -',ct1
print 'part 2 -',ct2
