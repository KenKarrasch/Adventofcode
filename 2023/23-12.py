f = open('23-12.txt').read().split('\n')

# Solution recursively go through each character, as each character progresses memoize (cache/DP) the state of play

DP = {}

def expl(cd,rl,i,br,bln,depth,ln):
    if i == len(cd):  # got to the end, lets check to see if all the #'s are done
        if br == len(rl) and bln==0:
            #print('found possibility',ln,depth)
            return 1  # last block counted 
        if br == len(rl)-1 and rl[br]==bln:
            #print('found possibility',ln,depth)
            return 1  # is the last block
        return 0
    #print('i',i,', br',br,', bln',bln,', rule',rl[bi],', character cd[i]',cd[i], ', depth', depth)    
    cl = cd[i]  # current character
    #print(bi,i)    
    ty = 0
    rsz = len(rl)
    #print('depth',depth)
    if True:#f(depth < 10):      
      for c in ['.','#']:          
        if ((cl == '?' and c == '.') or (c=='.' and cl == '.')) and bln == 0: # move through the dots
        #print('bi',bi, len(rl))
        #if (c == '.') and bln == 0: # move through the dots
            #print('1: cl, c, bln, bsz',cl, c, bln, bsz)
            #print('assume dot')
            sgn = (i+1,br,0)
            if sgn in list(DP.keys()):
                ty += DP[sgn]
            else: 
                ty += expl(cd,rl,i+1,br,0,depth+1,ln+'.')
                DP[sgn] = ty
        if ((cl == '?' and c == '.') or (c == '.' and cl == '.')) and bln>0 and br<rsz and rl[br] == bln:
        #elif c == '.' and bln>0 and br<rsz and rl[br] == bln: 
            # reached the end of the current block of #'s, just got a dot(.) to go to the next block.
            # and more blocks groups to go.
            #print('1: cl, c, bln, rsz',cl, c, bln, rsz)
            #print('assume .')
            sgn = (i+1,br+1,0)
            if sgn in list(DP.keys()):
                ty += DP[sgn]
            else: 
                ty += expl(cd,rl,i+1,br+1,0,depth+1,ln+'.')
                DP[sgn] = ty
        if (cl == '?' and c == '#') or (c == '#' and cl == '#'): # Just got a #, register we have gotten a new hash #, increment the block number
            # (bln + 1)
            #print('2: cl, c, bln, bsz',cl, c, bln, bsz)
            #print('assume #',cl)
            sgn = (i+1,br,bln+1)
            if sgn in list(DP.keys()):
                ty += DP[sgn]
            else: 
                ty += expl(cd,rl,i+1,br,bln+1,depth+1,ln+'#')     
                DP[sgn] = ty    
    return ty

rp = 5
pt1,pt2 = '',''
for rp in [1,5]:
  tot = 0
  for ln in f:
    print(ln)
    cr = ln.split()  # code , block rules
    c = cr[0]      
    if rp == 5:
        c = c+'?'+c+'?'+c+'?'+c+'?'+c        
    DP = {}  
    
    r = cr[1]
    if rp == 5:
        ri = r+','+r+','+r+','+r+','+r
    else: ri = r
    r = [int(y) for y in ri.split(',')]
    #print(r)
    #print('r length',len(r),r,c)
    ty = expl(c,r,0,0,0,0,'')
    
    print(ty)
    tot += ty

  if rp == 1: 
      pt1 = tot
      print('part 1',tot)
  if rp == 5: 
      pt2 = tot
      #print('part 2',tot)
print('part 1',pt1)
print('part 1',pt2)
