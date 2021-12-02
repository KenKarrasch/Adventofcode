f = open("17-16.txt").read().split(',')
s,ct,dm,d,fd = 'abcdefghijklmnop',0,[],0,False

def getl(s,l):
    for i in range(len(s)):
        if l == s[i]:
            return i

while not fd:
    for i in f:   
        ct += 1    
        if i[0] == 's':        
            s = s[-1*int(i[1:]):] + s[:-1*int(i[1:])]        
        if i[0] == 'x':
            r = [int(j) for j in i[1:].split('/')]
            s1 = [j for j in s]        
            s1[r[0]],s1[r[1]] = s1[r[1]],s1[r[0]]
            s = ''
            for j in s1: s += j
        if i[0] == 'p':        
            rl = i[1:].split('/')        
            r = [getl(s,rl[0]),getl(s,rl[1])]        
            s1 = [j for j in s]        
            s1[r[0]],s1[r[1]] = s1[r[1]],s1[r[0]]
            s = ''
            for i in s1: s += i
    if s in dm:        
        print('part 2 -',dm[(1000000000%(d+1))+1])
        fd = True
    if d == 0: print('part 1 -',s)
    dm.append(s)
    d += 1
