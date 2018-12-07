def inltrs(ch, ltrs):
    for ltr in ltrs:
      if ltr == ch:
          return True
    return False

def gnxtltr(steps,post,pre,ltrs,lt,num):
   for ch in range(len(steps)):
      ok = True
      if inltrs(steps[ch],ltrs):
        ok = False
      for i in range(5):
        if i != num - 1:
          if steps[ch] == lt[i]:
            ok = False
      for po in range(len(post)):
        if steps[ch] == post[po]:
          if not inltrs(pre[po],ltrs):
              ok = False
      if ok:
        return(steps[ch])
   return ''
    
f = open('18-7text.py','r')
#f = open('18-7test.txt','r')
b = f.read().split('\n')

pre = []
post = []
for n in range(len(b)):
    pre.append(b[n].split(' ')[1])
    post.append(b[n].split(' ')[7])

#steps = 'ABCDEF'
steps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

haspost = [0 for i in steps]

for g in range(len(pre)):
   for ch in range(len(steps)):
    if post[g] == steps[ch]:
      haspost[ch] = 1

ltrs = []
start = ''
for g in range(len(haspost)):
    if haspost[g] == 0:
      if start == '':
        start = steps[g]
ltrs.append(start)

while len(ltrs) < len(steps):
  ind = 0
  fd = False
  for ch in range(len(steps)):
    if not fd:
      ok = True
      if inltrs(steps[ch],ltrs):
        ok = False
      for po in range(len(post)):
        if steps[ch] == post[po]:
          if not inltrs(pre[po],ltrs):
              ok = False
      if ok:
        ltrs.append(steps[ch])
        fd = True

str = ''
for ch in ltrs:
    str = str + ch
print 'part 1 -', str

timer = -1
FREE = 0
BUSY = 1
worker1 = False
worker2 = False
worker3 = False
worker4 = False
worker5 = False
wtimer1 = 0
wtimer2 = 0
wtimer3 = 0
wtimer4 = 0
wtimer5 = 0
wl = ['' for i in range(5)]
ltrs = []
while len(ltrs) < len(steps):
   
   timer = timer + 1
   
   if not worker1:
       wl[1-1] = gnxtltr(steps, post, pre, ltrs, wl, 1)
       if wl[1-1] != '':
         wtimer1 = 61 + ord(wl[1-1]) - ord('A')
         worker1 = True
   
   if not worker2:
       wl[2-1] = gnxtltr(steps, post, pre, ltrs, wl, 2)
       if wl[2-1] != '':
         wtimer2 = 61 + ord(wl[2-1]) - ord('A')
         worker2 = True
         
   if not worker3:
       wl[3-1] = gnxtltr(steps, post, pre, ltrs, wl, 3)
       if wl[3-1] != '':
         wtimer3 = 61 + ord(wl[3-1]) - ord('A')
         worker3 = True
         
   if not worker4:
       wl[4-1] = gnxtltr(steps, post, pre, ltrs, wl, 4)
       if wl[4-1] != '':
         wtimer4 = 61 + ord(wl[4-1]) - ord('A')
         worker4 = True
         
   if not worker5:
       wl[5-1] = gnxtltr(steps, post, pre, ltrs, wl, 5)
       if wl[5-1] != '':
         wtimer5 = 61 + ord(wl[5-1]) - ord('A')
         worker5 = True
         

   wtimer1 = wtimer1 - 1
   wtimer2 = wtimer2 - 1
   wtimer3 = wtimer3 - 1
   wtimer4 = wtimer4 - 1
   wtimer5 = wtimer5 - 1
   
   if wtimer1 == 0:
       worker1 = False
       if wl[1-1] != '':
         ltrs.append(wl[1-1])
         wl[1-1] = ''
   
   if wtimer2 == 0:
       worker2 = False
       if wl[2-1] != '':
         ltrs.append(wl[2-1])
         wl[2-1] = ''
   
   if wtimer3 == 0:
       worker3 = False
       if wl[3-1] != '':
         ltrs.append(wl[3-1])
         wl[3-1] = ''
         
   if wtimer4 == 0:
       worker4 = False
       if wl[4-1] != '':
         ltrs.append(wl[4-1])
         wl[4-1] = ''
        
   if wtimer5 == 0:
       worker5 = False
       if wl[5-1] != '':
         ltrs.append(wl[5-1])
         wl[5-1] = ''
         
   if wtimer1 < 0:
       wtimer1 = 0
   if wtimer2 < 0:
       wtimer2 = 0
   if wtimer3 < 0:
       wtimer3 = 0
   if wtimer4 < 0:
       wtimer4 = 0
   if wtimer5 < 0:
       wtimer5 = 0
       
print 'part 2 -',timer + 1
