import itertools

ins = open('16-21.txt').read().split('\n')

def getp(fs,lt):
    for j in range(len(fs)):
      if fs[j] == lt:
         return j

st = 'abcdefgh'
tg = 'fbgdceah'
ds = ''
fi = [x for x in st]
def sc(f):
  for isp in ins:    
    ds = ''
    i = isp.split()    
    if 'swap' in i:
      if 'position' in i:
          i5 = int(i[5])
          i2 = int(i[2])
      if 'letter' in i:
          i5 = getp(f,i[5])
          i2 = getp(f,i[2])      
      [f[i5],f[i2]] = [f[i2],f[i5]]
    if 'rotate' in i:      
      if 'left' in i:                       
        f = f[int(i[2]):] + f[:int(i[2])]
      if 'right' in i:
        f = f[len(f)-int(i[2]):] + f[:len(f)-int(i[2])]
      if 'based' in i:
        lp = getp(f,i[6])+1
        if lp > 4:
            lp += 1        
        lp = len(f)-lp
        f = f[lp:] + f[:lp]
    if 'reverse' in i:
        i2 = int(i[2])
        i4 = int(i[4])        
        f = f[:i2] + f[i2:i4+1][::-1] + f[i4+1:]
    if 'move' in i:
        i2 = int(i[2])
        i5 = int(i[5])
        i2l = f[i2]
        f = f[:i2] + f[i2+1:]
        f = f[:i5] + [i2l] + f[i5:]
  
  return ds.join(f)

print('part 1 -',sc(fi))
for it in itertools.permutations(fi):
   ts = []
   for g in range(len(it)):
     ts.append(it[g])   
   st = sc(ts[:])   
   if tg == st:
      print('part 2 -', ds.join(ts))
      break
