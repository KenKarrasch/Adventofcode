import itertools
import copy
f = open('15-21.txt').read().split('\n')
hp = int(f[0].split(':')[1])
d = int(f[1].split(':')[1])
a = int(f[2].split(':')[1])      
nbk = [[100,0,0],[hp,d,a]]
tt = ['player','boss']
tn = 0
       # Cost, Damage, Armor
wbk= [[  8,4,0],\
      [ 10,5,0],\
      [ 25,6,0],\
      [ 40,7,0],\
      [ 74,8,0],\
      
      [  0,0,0],\
      [ 13,0,1],\
      [ 31,0,2],\
      [ 53,0,3],\
      [ 75,0,4],\
      [102,0,5],\

      [  0,0,0],\
      [  0,0,0],\
      [ 25,1,0],\
      [ 50,2,0],\
      [100,3,0],\
      [ 20,0,1],\
      [ 40,0,2],\
      [ 80,0,3]]

p1,p2 = [],[]
war = []
for w in [0,1,2,3,4]: # one weapon
 for a in [0,1,2,3,4,5,6]: # armor 
  for r1 in [0,1,2,3,4,5,6,7]: # ring 1
   for r2 in [0,1,2,3,4,5,6,7]: # ring 2
    if r1 != r2:
     war = [w,a+5,r1+11,r2+11]     
     bk = copy.deepcopy(nbk)     
     tn = 0
     for i in war:
      bk[0][1] += wbk[i][1]  # Damage
      bk[0][2] += wbk[i][2]  # Armor     
     while (bk[0][0] > 0) and (bk[1][0] > 0):    
      dam = bk[tn][1] - bk[(tn+1)%2][2]
      if dam < 1: dam = 1
      bk[(tn+1)%2][0] -= dam          
      tn = (tn+1)%2
     c = 0
     for i in war: c += wbk[i][0]           
     if bk[0][0] > 0: p1.append(c)      
     if bk[0][0] < 1: p2.append(c)
p1.sort()
p2.sort()
print('part 1 -',p1[0])
print('part 2 -',p2[-1])
