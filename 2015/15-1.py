f = open('15-1.txt').read()
#print f
sb,fb = 0,0
fd = False
for i in range(len(f)):
  if f[i] == '(':
      sb += 1
  if f[i] == ')':
      fb += 1
  if sb-fb == -1:
    if not fd:
      print 'part 2 -', i+1
      fd = True
print 'part 1 -', sb - fb
