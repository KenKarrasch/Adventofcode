s = [int(x) for x in open('15-17.txt').read().split('\n')]
mt = []

def fd(us,tg,depth):
  if tg == 0:
    us.sort()
    if us not in mt:
      mt.append(us)
    return
  if tg < 0:
    return
  for i in range(len(s)):
    if depth == 0:
      print (i,'of',len(s))
    if i not in us:
      fd(us[:]+[i],tg-s[i],depth+1)      

fd([],150,0)
print('part 1 -',len(mt))
l = [len(x) for x in mt]
ml = min(l)
print('part 2 -',len([x for x in mt if len(x) == ml]))
