f = open('23-10.txt').read().split('\n')

# Straightforward BFS for part 1 and 2.  I got around the adjacent pipes by expanding the grid out x2. 

g = [[y for y in l] for l in f]

if len(f[0]) > len(f):    
    for i in range(len(f[0]) - len(f)):
        ln = ''
        for j in range(len(f[0])):
            ln += '.'
        f.append(ln)
#print(f)

my = len(f)
mx = len(f[0])

#print(g)
#[up-down,left-right]
dr = {'.': [],'|': [[1,0],[-1,0]], '-': [[0,1],[0,-1]], 'F': [[1,0],[0,1]], 'J': [[-1,0],[0,-1]],'L': [[0,1],[-1,0]], '7': [[1, 0],[0, -1]], 'S': []  }

c = []
for i in range(len(g)):
    for j in range(len(g[i])):    
        if 'S' == g[i][j]:
            print('Start',i,j)
            c = [i,j]

bn = [[0 for y in l] for l in f]
bg = [[' ' for y in range(len(f[0])*2)] for l in range(len(f)*2)]


been = []
dist = []
v = []

def bd(c):
    if 0 <= c[0] < mx:
        if 0 <= c[1] < my:
            return True
    return False

def bgd(c):
    if 0 <= c[0] < mx*2:
        if 0 <= c[1] < my*2:
            return True
    return False


i,j = c
#print('i,j',i,j)
been.append([c[0],c[1]])
bn[c[0]][c[1]] = 0

bg[(c[0])*2][(c[1])*2] = 'x'

if bd([i+1,j]):  
    #print('[i+1,j]',g[i+1][j])
    if g[i+1][j] in '|JL':
        v.append([c[0]+1,c[1],1])
        been.append([c[0]+1,c[1]])
        bn[c[0]+1][c[1]] = 1
        bg[(c[0]+1)*2-1][(c[1])*2] = 'x'
        bg[(c[0]+1)*2][(c[1])*2] = 'x'
if bd([i,j-1]):  
    #print('[i,j-1]',g[i][j-1])
    if g[i][j-1] in '-FL':
        v.append([c[0],c[1]-1,1])
        been.append([c[0],c[1]-1])
        bn[c[0]][c[1]-1] = 1
        bg[(c[0])*2][(c[1]-1)*2] = 'x'
        bg[(c[0])*2][(c[1]-1)*2+1] = 'x'
        
if bd([i,j+1]):     
    #print('[i,j+1]',g[i][j+1])
    if g[i][j+1] in '-7J':
        v.append([c[0],c[1]+1,1])
        been.append([c[0],c[1]+1])
        bn[c[0]][c[1]+1] = 1
        bg[(c[0])*2][(c[1]+1)*2] = 'x'
        bg[(c[0])*2][(c[1]+1)*2-1] = 'x'
if bd([i-1,j]):
    #print('[i-1,j]',g[i-1][j])
    if g[i-1][j] in '|F7':
        v.append([c[0]-1,c[1],1])
        been.append([c[0]-1,c[1]])
        bn[c[0]-1][c[1]] = 1
        bg[(c[0]-1)*2][(c[1])*2] = 'x'
        bg[(c[0]-1)*2+1][(c[1])*2] = 'x'

#print('been',been)
#print('v',v) 


def draw():
    print('====================')
    for i in range(len(g)):
        ln = ''
        for j in range(len(g[i])):
            if(bn[i][j] != 0):
                if bn[i][j] < 10:
                    ln += str(bn[i][j])
                else:
                    ln += str(bn[i][j])[1]
            else: ln += ' '
        print(ln)
    print('====================')
    for i in range(len(g)):
        ln = ''
        for j in range(len(g[i])):
            ln += g[i][j]                
        print(ln)
    print('====================')

def drawbg():
    print('====================')
    for i in range(len(bg)):
        ln = ''
        for j in range(len(bg[i])):
            ln += bg[i][j]                
        print(ln)
    print('====================')


#drawbg()
ct = 0

dist = 0
lsti,lstj = 0,0  

lb = []


while True:
    ct += 1
    #print(v)
    if len(v) == 0:
        break
    if len(v) == 2:
        #print('v',v)
        lb = [v[0][:],v[1][:]]
        #draw()
    expl = v.pop(0)
    dist = expl[2]
    for di,dj in dr[g[expl[0]][expl[1]]]:           
        i = expl[0]+di
        j = expl[1]+dj            
        if bd([i,j]):            
            if [i,j] not in been:           
                #print('at',g[expl[0]][expl[1]],expl[0],expl[1])     
                #print('going to',i,j,'delta',di,dj,g[i][j])
                been.append([i,j])
                bn[i][j] = expl[2]+1
                v.append([i,j,expl[2]+1])                   
                bg[i*2][j*2] = 'x'
                bg[i*2-di][j*2-dj] = 'x'
                #print('drawing bg')
                #drawbg()

#print(lb)
bg[lb[0][0] + lb[1][0]][lb[0][1] + lb[1][1]] = 'x'
#drawbg()
print('part 1', dist)

l = len(bg)-1

def getxs(ch):
    ct = 0
    ijs = []
    for i in range(len(bg)):
        for j in range(len(bg)):
          if i%2 == 0:
            if j%2 == 0:
                if bg[i][j] == ch:
                    ct += 1
                    ijs.append([i,j])

    #print(ijs)
    return ct
                
xs = getxs('x')

os = []
been = []

for i in range(len(bg)):
    if bg[0][i] == ' ':
        os.append([0,i])
        been.append([0,i])
    if bg[l][i] == ' ':
        os.append([l,i])
        been.append([l,i])
    if bg[i][0] == ' ':
        os.append([i,0])
        been.append([i,0])
    if bg[i][l] == ' ':
        os.append([i,l])
        been.append([i,l])

for i in been:
    bg[i[0]][i[1]] = 'o'

#print(len(bg))

while True:
    if len(os) == 0:
        break
    nos = os.pop()
    for d in [[-1,-1],[-1,0],[-1,1], [0,-1],[0,1], [1,-1],[1,0],[1,1]]:
        if bgd([nos[0]+d[0],nos[1]+d[1]]):             
            if [nos[0]+d[0],nos[1]+d[1]] not in been:                
                if bg[nos[0]+d[0]][nos[1]+d[1]] != 'x':
                    #print('ok',nos[0]+d[0],nos[1]+d[1])
                    os.append([nos[0]+d[0],nos[1]+d[1]])
                    been.append([nos[0]+d[0],nos[1]+d[1]])
                    bg[nos[0]+d[0]][nos[1]+d[1]] = 'o'
                    if len(been)%1000 == 0: 
                        print(len(been), 'of', str(len(bg)*len(bg)),'max')
#drawbg()

print(len(bg[0])*len(bg))
xs = getxs(' ')
print('part 2', xs)

oss = 0
#print(been)
for i in been:
    if i[0]%2 == 0:
        if i[1]%2 == 0:
            oss += 1
#print(been)
#print('oss,xs',oss,xs)     

ls = l * l
#print(len(bg)*len(bg)/4)    
tot = (ls/4) - (oss + xs)
#print(tot)

