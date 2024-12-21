
from collections import deque


f = open('24-21.txt').read().split('\n')    

tly = 0

for i in f:
    seq = i
    num = int(seq[:-1])
    print(num)

    gd = [[None,None,None,None,None],[None,'7','8','9',None],[None,'4','5','6',None],[None,'1','2','3',None],[None,None,'0','A',None],[None,None,None,None,None]]
    gda = [[None,None,None,None,None],[None,None,'^','A',None],[None,'<','v','>',None],[None,None,None,None,None]]

    dr = {'^': -1, 'v': 1, '>': 0,'<': 0}
    dc = {'^': 0, 'v': 0, '>': 1,'<': -1}


    def getloc(ltr):
        for r in range(6):
            for c in range(5):
                if gd[r][c] == ltr:
                    return (r,c)
                
    def getloca(ltr):
        for r in range(4):
            for c in range(5):
                if gda[r][c] == ltr:
                    return (r,c)

    ct = 0
    fd = False

    ## Numeric

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

    for i in npths:
        print('path',''.join(i[:]))
    


    bk = {}

    ltrs = ['v','<','>','^','A']


    ## Arrow keypad
    nnpths = []
    for i in npths:
        seq = ''.join(i)
        seq = 'A' + seq
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

    for i in nnpths:
        print('path',''.join(i[:]))



    ## Arrow keypad
    nnnpths = []
    for i in nnpths:
        seq = ''.join(i)
        seq = 'A' + seq
        fpths = [[]]
        print(''.join(i))
        for ls in range(len(seq) - 1):
            start = getloca(seq[ls])
            Q = [(start[0]-1,start[1],'v',0,[])]
            end = getloca(seq[ls+1])
            dist = abs(end[0] - start[0]) + abs(end[1] - start[1])
            pths = []
            visited = []
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
            nnnpths.append(i)

    test = '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
    lgths = []
    for i in nnnpths:
        #st = ''.join(i[:])
        #print(st,len(st))
        lgths.append(len(''.join(i)))
        #if ''.join(i[:]) == test:
        #    print('found')
        
        #print('path',''.join(i[:]))
    tly += num*min(lgths)
    print(min(lgths))
print(tly)
        
