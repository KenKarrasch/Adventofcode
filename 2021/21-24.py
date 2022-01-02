s = open('21-24.txt').read().split('\n')

# Commentary at the bottom of this file (to avoid spoilers)
v = {}

def gv(i):
    if i in 'wxyz':
        return v[i]
    return int(i)

p = 0
dn = False
sc = [False]
v1 = 18  


def check(n):
 ni = n 
 cmp = [] 
 n = str(ni)
 if '0' not in n:  
  for ver in [0,v1]:   
   n = str(ni)
   d = []
   for ch in n:
    d.append(int(ch))
    
   v['w'] = 0
   v['x'] = 0
   v['y'] = 0
   v['z'] = 0
   p = 0     
   bk = [] 
   cyc = 18  # for now only do one cycle
   #print('--------------------',ver)
   sc[0] = True
   if ver == v1:
    for c in range(14):   
     d1 = int(s[4+cyc*c].split()[2])
     a1 = int(s[5+cyc*c].split()[2])
     a2 = int(s[15+cyc*c].split()[2])   
     z = v['z']  
     if d[0]==(z%26)+a1: x = 0 
     else: x = 1               
     if d1 == 26 and x == 1: # If statment failed, save how far we got, sc[0]
        print(ni,'fail')  
        sc[0] = c
        return False
     if d1 == 1 and x == 0:   
        print(ni,'fail')                         
        sc[0] = c
        return False
     z = z//d1
     z = z*(25*x+1) + (d[0]+a2)*x
     y = d[0]+a2
     v['z'] = z
     v['y'] = y
     v['x'] = x
     v['w'] = d[0]
     #print(v)
     del d[0]     
     st = v1
     p += st
     for k in range(st): bk.append([0])     
   pr = p

   while (p < len(s)):
    i = s[p].split()        
    if i[0] == 'inp':       
      v[i[1]] = d[0]      
      del d[0]      
    if i[0] == 'add':       
      v[i[1]] = gv(i[1]) + gv(i[2])      
    if i[0] == 'mul': 
      v[i[1]] = gv(i[1])*gv(i[2])
    if i[0] == 'div': 
      v[i[1]] = gv(i[1])//gv(i[2])
    if i[0] == 'mod': 
      v[i[1]] = gv(i[1])%gv(i[2])
    if i[0] == 'eql': 
      if gv(i[1]) == gv(i[2]):
          v[i[1]] = 1
      else:
          v[i[1]] = 0
    p += 1
    bk.append([v['w'],v['x'],v['y'],v['z'],p])
    #if ver == 0 and (p)%18==0: print(v,i)

   cmp.append([k[:] for k in bk]) 
   #print('v',v)
  gds = 0
  diff = 0
  for i in range(len(cmp[0])):  
    if i >= pr:  
      if cmp[0][i] == cmp[1][i]:
        gds += 1
      else:
        diff += 1 # Debugging code to ensure simplifications worked
 print(ni,v)
 if v['z'] == 0:
    return True
 return False

can = 99999999999999
fd = False
i = 0
dig = 1
while not fd:    # Part 1
  fd = check(can)
  if fd: pt1 = can
  dig = sc[0]
  print(can)  
  can -= 10**(13-dig)

can = 11111111111111
fd = False
i = 0
dig = 1
while not fd:    # Part2
  fd = check(can)
  if fd: pt2 = can
  dig = sc[0]
  print(can)  
  can += 10**(13-dig)
print('part 1 -',pt1)  
print('part 2 -',pt2)

# The assembly language needed to be boiled down quite a bit to understand
# what was going on.  The 252 lines of code appeared to be the same 18 lines
# repeated 14 times, with only three variables changing.  'div z 1' (d1), 
# 'add x 10' (a1), and 'add y 5' (a2).
# 
# My code came down to this, 18 times:
#
# w = d[0]
# if d[0]==z%26+a1: x = 0 else: x = 1
# z = z//d1
# z = z*(25*x+1) + (d[0]+a2)*x
#
# The key was to get the if statement to be true whenever 'div z 1' appeared
# and false when 'div z 26' occurred.
#
# In order to acheive this start at the highest digit, 99999999999999, 
# and see how many if statements it gets through, then decrement one,
# 8999999999999, until the if statement gets further. When this happens move onto the
# next digit, until all digits are solved.  Pretty sure this problem 
# could be solved by hand.  My answer was 99919692496939.
#
# For part two do the opposite, start at 11111111111111, and increment.
#
#  Debugging code left in
