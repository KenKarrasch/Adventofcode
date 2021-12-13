f = open('21-13.txt').read().split('\n')
# nice fun one, couldn't view the solution on my 
# phone due to font
# ended up having to email to my work computer 

c = []
ct = []

for i in f:
    if ',' in i:
      cs = i.split(',')
      c.append([int(cs[0]),int(cs[1])])
    else:
      if '=' in i:
        dt = i.split()[2].split('=')
        ct.append([dt[0],int(dt[1])])

x,y = 0,0

dts = []

mx,my = 0,0

def pt():
    for i in range(my):
      st = ''
      for j in range(mx):
        if [j,i] in dts:
            st += '#'
        else:
            st += '.'
      print st
    print

for i in c:
  x = i[0]
  y = i[1]
  dts.append([x,y])
  if mx < x+1:
      mx = x+1
  if my < y+1:
      my = y+1
r = 0
for fd in ct:
   ndts = [i[:] for i in dts]
   if fd[0] == 'y':
      for i in range(len(dts)):
         if dts[i][1] > fd[1]:
            ndts[i][1] = (-ndts[i][1])%fd[1]
            
   if fd[0] == 'x':
      for i in range(len(dts)):
         if dts[i][0] > fd[1]:
            ndts[i][0] = (-ndts[i][0])%fd[1]
   dts = [i[:] for i in ndts]
            
   if r == 0:
    fd = []
    for i in dts:
     if i not in fd:
        fd.append(i)
    print 'part 1 -',len(fd)
   r += 1
   
mx,my = 0,0
for i in dts:
  x = i[0]
  y = i[1]
  if mx < x+1:
      mx = x+1
  if my < y+1:
      my = y+1
#print mx,my
print 'part 2 -'
pt()
