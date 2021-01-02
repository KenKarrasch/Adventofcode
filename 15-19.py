s = open('15-19.txt').read().split('\n')
mol,b,m = s[len(s)-1],[],[]
for i in s[0:-2]:  
  b.append(i.split(' => ')[0])
  m.append(i.split(' => ')[1])
nms = []
for i in range(len(b)):
  for x in range(len(mol)):
    sz = len(b[i])
    if x+sz <= len(mol):
      if mol[x:x+sz] == b[i]:
        nm = mol[:x] + m[i] + mol[x+sz:]      
        if nm not in nms:
          nms.append(nm)
print('part 1 -',len(nms))
rc,el = 1,0
for i in range(len(mol)):
  if mol[i].isupper(): el += 1
  if mol[i:i+2] == 'Rn': rc += 1
  if mol[i:i+2] == 'Ar': rc += 1
  if mol[i:i+1] == 'Y': rc += 2
print('part 2 -',el-rc)
