f = open('16-25.txt').read().split('\n')
reg = {'a': 1, 'b': 0, 'c': 0, 'd': 0}

def gv(c):
   if ord(c[0]) >= ord('a'):
     if ord(c[0]) <= ord('z'):
        return reg[c]
   return int(c)

fd,a = False,0
while not fd:  
  a += 1  
  hp,p,adn,o = 100,0,False,[]
  reg['a'] = a  
  while (p < len(f)) and not adn:   
    s = f[p].split()
    if 'cpy' in s:
      reg[s[2]] = gv(s[1])
    if 'jnz' in s:
      if gv(s[1]) != 0:
        p += int(s[2])-1
    if 'inc' in s:
      reg[s[1]] += 1
    if 'dec' in s:
      reg[s[1]] -= 1
    if 'out' in s:      
      op = gv(s[1])      
      if len(o) == 0:      
        o.append(op)
      else:        
        if o[-1]^op:     
          hp -= 1
          if hp < 0:
            adn = True
            fd = True
        else:
         adn = True
        o.append(op)      
    p += 1    
print ('part 1 -',a)
