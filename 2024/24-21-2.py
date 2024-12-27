
from collections import deque

# Work out the best paths between each keyboard key, make a dictionary to reference
# Using some heuristics work out the best path between keys, e.g. no zigzags. Up then right, rather than right then up.
# Use dynamic programming DP for memoisation, if the the path being searched for is already
# been calculated, dont try to recalculate it, just use the book record.  If not add the detail to the book record.

f = open('24-21.txt').read().split('\n')    
tly = 0
for ln in f:
    seq = ln
    num = int(seq[:-1])

    # keypad
    gd = [[None,None,None,None,None],[None,'7','8','9',None],[None,'4','5','6',None],[None,'1','2','3',None],[None,None,'0','A',None],[None,None,None,None,None]]
    # dpad
    gda = [[None,None,None,None,None],[None,None,'^','A',None],[None,'<','v','>',None],[None,None,None,None,None]]
    
    dr = {'^': -1, 'v': 1, '>': 0,'<': 0}
    dc = {'^': 0, 'v': 0, '>': 1,'<': -1}

    def getloc(ltr):  # get coordinates of keypad button
        for r in range(6):
            for c in range(5):
                if gd[r][c] == ltr:
                    return (r,c)
                
    def getloca(ltr):  # get coordinates of dpad button
        for r in range(4):
            for c in range(5):
                if gda[r][c] == ltr:
                    return (r,c)

    ct = 0
    fd = False

    # Numeric keypad, work out the valid key sequences for the keypad.
    # probably could be sped up by pre-calculating paths

    seq = 'A' + seq
    fpths = [[]]
    for ls in range(len(seq) - 1):
        start = getloc(seq[ls])
        Q = [(start[0]-1,start[1],'v',0,[])]    
        end = getloc(seq[ls+1])
        dist = abs(end[0] - start[0]) + abs(end[1] - start[1])
        pths = []
        while Q:
            Q.sort()
            r, c, but, steps, pth = Q.pop()
            if gd[r + dr[but]][c + dc[but]] != None:
                r,c = r + dr[but], c + dc[but]
            else: continue
            if (r,c) == end: pths.append(pth)    
            for ky in ['^','<','>','v']:
                npth = pth[:]
                npth.append(ky)
                if steps < dist:
                    Q.append((r,c,ky,steps+1,npth))
        npths = []
        for i in fpths:        
            for j in pths:
                npths.append(i[:] + j[:] + ['A'])
        fpths = []
        for i in npths:
            fpths.append(i[:])        

    numpaths = []
    for i in npths:
        numpaths.append(i[:])    
    
    bk = {}

    ltrs = ['v','<','>','^','A']

    bk = {}

    # Set best paths between each dpad key for future reference
    for l1 in ltrs:
        for l2 in ltrs:            
                ## Arrow keypad
                npths = [l1,l2]
                if True:
                #for i in npths:
                    nnpths = []                    
                    seq = ''.join(npths)
                    #seq = 'A' + seq
                    fpths = [[]]
                    for ls in range(len(seq) - 1):
                        start = getloca(seq[ls])
                        Q = [(start[0]-1,start[1],'v',0,[])]
                        end = getloca(seq[ls+1])
                        dist = abs(end[0] - start[0]) + abs(end[1] - start[1])
                        pths = []
                        while Q:
                            Q.sort()
                            r, c, but, steps, pth = Q.pop()
                            if gda[r + dr[but]][c + dc[but]] != None:
                                r,c = r + dr[but], c + dc[but]
                            else: continue
                            if (r,c) == end: pths.append(pth)    
                            for ky in ['^','<','>','v']:
                                npth = pth[:]
                                npth.append(ky)
                                if steps < dist:
                                    Q.append((r,c,ky,steps+1,npth))
                        npths = []
                        for i in fpths:        
                            for j in pths:
                                npths.append(i[:] + j[:] + ['A'])
                        fpths = []
                        for i in npths:
                            fpths.append(i[:])        

                    for i in npths:                        
                        nnpths.append(i)
                bpths = []
                for i in nnpths:                
                    bpths.append(''.join(i[:]))                    
                bk[(l1,l2)] = bpths

    # Heuristics - Best Paths between keys, no zigzags, favour up then right, rather than 
    # right then up. etc
    bk[('<','A')] = ['>>^A']
    bk[('>','^')] = ['<^A']
    bk[('v','A')] = ['^>A']
    bk[('^','>')] = ['v>A']
    bk[('A','<')] = ['v<<A']
    bk[('A','v')] = ['<vA']
    
    # Starting points and location memory for every robot keypad (25 keypads)
    location = ['A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A''A']
    
    DP = {}

    def getdist(path,depth):  
        lc = location[depth]         
        if (path,depth,lc) in DP:
            return DP[(path,depth,lc)] # We have seen this keypad before use previously calculated keypresses
        if(depth == 0):                      
            return 1     # Last keypad is a human keypad - 1 button press per key           
        dist = 0
        bestpath = location[depth]        
        for i in bk[path][0]:            
            bestpath = bestpath + i                    
        for s in range(len(bestpath)-1):               
            gd = getdist((bestpath[s],bestpath[s+1]),depth-1)
            location[depth] = bestpath[s+1]
            dist += gd        
        DP[(path,depth,lc)] = dist  # Haven't seen this path before, add it to the dictionary for future use
        return dist
    
    DP = {}
    
    robots = 3
    robots = 26

    tdist = 0    
    tdists = []
    for i in numpaths: # go through each of the suggested paths for keypad
        dist = 0                
        ni = ['A'] + i
        for j in range(len(ni)-1):                 
            dist += getdist((ni[j],ni[j+1]),robots - 1)        
        tdists.append(dist)           
    print(num,min(tdists))   
    tly += num*min(tdists)  
print('part 2 -',tly)    
