from functools import cache
from itertools import combinations
f = open('25-10.txt').read().split('\n')
# 10   14280  13524  *******

#  Initially tried searching by trying each button until it could reach the required joltage, but was taking too long.
#  Then tried a set union similar to AOC2020- day 21 by trying amounts of button presses and eliminating amount when they went over the joltage,
#  however, this did not appear to be providing any simplification in results.

#  Then it dawned on me that the problem is simply a solution of simultaneous equations.  The only problem, as the question
#  implied, by saying there was mulitple solutions and "we had to choose the smallest". So of course the equations don't resolve.
#  Then I remembered on AOC2023 day24 people using Microsoft Z3 tool to resolve simulataneous equations.  Python also has a similar tool
#  called Scipy which does the same thing. I will post that too.

#  I didn't want to simply use this tool, it was too easy.  Also something didn't feel right about using
#  a proprietry tool which I do not know how it works.

#  So implemented this solution, noting the profile of the joltages, odd/even is important, and related to part 1.
#  After working out how to bring the joltage profile to simply even numbers, it is possible to recursively work the joltage profiles
#  down, noting butons pressed twice resulted in even advances.


btns = []
nmss = []

for dt in f:    # Pare inputs
    bt = dt.split(']')[1].split('{')[0].split()
    bt1 = [x.replace(')','').replace('(','') for x in bt]
    bts = [[int(y) for y in x.split(',')] for x in bt1]
    nms = [int(y) for y in dt.split('{')[1].split('}')[0].split(',')]
    btsa = []
    for i in range(len(bts)):
        bb = [0]*len(nms)
        for b in bts[i]:
            bb[b] = 1
        btsa.append(tuple(bb))        
    btns.append(btsa)
    nmss.append(nms)

bsp = {}            
@cache
def expl(jolts):
    result = 999999999	# worst case	
    dn = True    
    for i in jolts: # all zeros - finished 
        if i != 0:
            dn = False
    if dn:
        return 0   # We have reached the required amount, exit         
    for sgn, bspr in bsp.items(): # go through the dictionary       
        gd = True   
        for pos in range(len(jolts)):
            s = sgn[pos]
            j = jolts[pos]
            if not(s <= j and s%2==j%2): 
                gd = False  # discard if over the required joltage, and both odd or even
        if gd:        
            ng = [0]*len(jolts)
            for i in range(len(jolts)):  
                ng[i] = (jolts[i] - sgn[i])//2  # joltages are a multiple of 2 (light on and off), search for how many buttons to press to get to the new (lower amount)
            new_jolts = tuple(ng)
            minbutns = 2 * expl(new_jolts) + bspr  # find out how many buttons are required to get to the new amount. 
                # Note that the buttons required are 2 times the new jolts (even profile) plus to the number to get to the odd even profile of the target joltage
            if minbutns < result: # If we did better than previous record that.
                result = minbutns
    return result

tly = 0

for p in range(len(nmss)):
        tgt = nmss[p]
        lt = len(tgt)        
        nb = len(btns[p])
        bsp = {} # Dictionary of how many buttons are pressed to get to a state (signature)
        for pl in range(nb+1):
            cmbs = list(combinations(range(nb),pl)) # Try every combination of buttons, noting we are not interested in pressing any buttons twice
            for c in cmbs:
                sgn = [0]*lt                
                for b in c:                       
                    bc = btns[p][b]                    
                    for ltr in range(len(bc)):                        
                        sgn[ltr] += bc[ltr]                
                if tuple(sgn) not in bsp:
                    bsp[tuple(sgn)] = pl # Populate  the possibilities       
        expl.cache_clear() # clear the cache
        butnspressed = expl(tuple(tgt))
        print('solved', butnspressed, tgt,',',p+1,'in',len(nmss)) 
        tly += butnspressed

print(tly)

# 16613
