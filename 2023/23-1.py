fi = open('23-1.txt').read().split('\n')

# part 1 okay 10min, part 2, 30min - phone battery ran flat, when recharged, realised some numbers can overlap, e.g. "eightwo" is 82, solution to replace words eg. "one", replace with "one1one", 
# then run it through the same meatgrinder for part 1. Going through forums, it looks like other people had the the same thought.

ns = ['zero','one','two','three','four','five','six','seven','eight','nine']
nm = '1234567890'

t1 = t2 = 0

for n in fi:
   f = l = '-1'
   for lt in n:
       if lt in nm:
           if f != '-1':
              l = lt
           else: 
              l = f = lt
   if l != '-1':
      t1 += int(l) + int(f) * 10
      
for n in fi:
   f = l = '-1'
   for x in range(10):
       n = n.replace(ns[x],ns[x]+str(x)+ns[x])
   for lt in n:
       if lt in nm:
           if f != '-1':
              l = lt
           else: 
              l = f = lt
   
   if l != '-1':
      t2 += int(l) + int(f) * 10
      
print 'part 1', t1
print 'part 2', t2
           
