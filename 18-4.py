def addev(ev,sts,ends, day,month,guard):
   newmin = ['.' for i in range(60)]
   for st in range(len(sts)):
     for hash in range(60):
       if hash >= sts[st]:
        if hash < ends[st]:
          newmin[hash] = '&'
   ev.append([month,day,guard,newmin])
     
def busyminute(ev,num):
  highest = -1
  hi = 0
  c = 0
  for m in range(60):
    c = 0
    for j in ev:
      if j[2] == num:
        if j[3][m] == '&':
           c = c + 1
        if c > hi:
            hi = c
            highest = m
  return highest
     
def bsyminhigh(ev,num):
  highest = -1
  hi = 0
  c = 0
  for m in range(60):
    c = 0
    for j in ev:
      if j[2] == num:
        if j[3][m] == '&':
           c = c + 1
        if c > hi:
            hi = c
            highest = m
  return hi
     
def findlazy(ev):
  c = 0
  highestct = 0
  highest = -1
  guards = []
  for i in range(10000):
    c = 0
    for j in ev:
      if j[2] == i:
        for m in j[3]:
          if m == '&':
            c = c + 1
    if c > highestct:
        highestct = c
        highest = i
  return highest
  
def monthdays(m):
    if m == 2:
        return 28
    if m == 3:
        return 31
    if m == 4:
        return 30
    if m == 5:
        return 31
    if m == 6:
        return 30
    if m == 7:
        return 31
    if m == 8:
        return 31
    if m == 9:
        return 30
    if m == 10:
        return 31
    if m == 11:
        return 30

f = open('18-4.txt','r')
b = f.read().split('\n')

#sort events
lst = []
for i in range(len(b)):
  ind = str(i)
  if i < 1000:
    ind = '0' + ind
  if i < 100:
    ind = '0' + ind
  if i < 10:
    ind = '0' + ind
  st = b[i][:18] + ind
  lst.append(st)
lst.sort()
ne = []
for i in lst:
 ne.append(b[int(i[18:])])
 
events = []
guard = 0
sts = []
ends = []
day = 1
month = 0
i = 0
while i < len(ne):
  ev = ne[i].split(' ')
  if ev[3][0] == '#':
    if i != 0:
      addev(events,sts,ends, day,month,guard)
      sts = []
      ends = []
    guard = int(ev[3][1:])
    day = int(ne[i][9:11])
    month = int(ne[i][6:8])
    if ne[i][12:14] == '23':
      day = day + 1
      if day > monthdays(month):
        day = 1
        month = month + 1
  else: 
    if ev[2] == 'falls':
      sts.append(int(ne[i][15:17]))
    if ev[2] == 'wakes':
      ends.append(int(ne[i][15:17]))
  i = i + 1
addev(events,sts,ends, day,month,guard)
l = findlazy(events)
b = busyminute(events, findlazy(events))
print 'part 1 -', l * b

gnum = -1
lazhigh = 0
for gd in range(10000):
  if lazhigh < bsyminhigh(events, gd):
    gnum = gd
    lazhigh = bsyminhigh(events, gd)
    
minute = busyminute(events,gnum)
print 'part 2 -', minute * gnum
