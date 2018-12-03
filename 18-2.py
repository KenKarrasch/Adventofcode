f = open('18-2.txt','r')
b = f.read().split('\n')
db = [0 for i in range(26)]
tl = [0,0,0,0]
lr = 0
for l in b:
    tl[0:2] = [0,0]
    for ch in l:
        lr = ord(ch) - ord('a')
        db[lr] = db[lr] + 1
    for sc in range(len(db)):
        if db[sc] == 3:
            tl[1] = 1
        if db[sc] == 2:
            tl[0] = 1
    for h in range(2):
      if tl[h] > 0:
        tl[h+2] = tl[h+2] + 1
    for i in range(26):
       db[i] = 0
print 'part 1 -', tl[2] * tl[3]
ref = 0
found = False
for l in b:
  for h in b:
   d = 0
   if l != h:
     for ch in range(26):
        if h[ch] != l[ch]:
            d = d + 1
            ref = ch
   if d == 1:
    if found == False:
      print 'part 2 -',l[:ref] + l[ref+1:]
      found = True
      
