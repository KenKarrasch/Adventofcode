f = open('15-23.txt').read().split('\n')
//Would have made it in the top 50 if I did this in 2015
reg = {'a': 1, 'b': 0}
def gv(c):   
   if ord(c[0]) >= ord('a'):
     if ord(c[0]) <= ord('z'):
        return reg[c]
   return int(c)
for i in [0,1]:
  reg['a'] = i
  reg['b'] = 0
  p = 0  
  while p < len(f) :   
    s = f[p].split()    
    if 'hlf' in s: reg[s[1]] = int(gv(s[1])/2)
    if 'tpl' in s: reg[s[1]] = gv(s[1])*3
    if 'inc' in s: reg[s[1]] += 1     
    if 'jmp' in s: p += int(s[1])-1
    if 'jie' in s: 
       if gv(s[1][:-1])%2==0:
         p += int(s[2])-1
    if 'jio' in s:        
      if gv(s[1][:-1])==1:
         p += int(s[2])-1
    p += 1    
  print ('part',i+1,'-',reg['b'])   
