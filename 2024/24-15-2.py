fi = open('24-15.txt').read().split('\n\n')

# Used Visual Basic for part 1 as my daughter and I had basically written the same thing for
# a game.  Python for part 2.  

f = fi[0].split('\n')
w = len(f[0])
h = len(f[0])
g, m = [],[]
for i in range(h):
    ln = []
    for j in range(w):
        if f[i][j] == '#':
            ln.append('#')
            ln.append('#')
        if f[i][j] == '.':
            ln.append('.')
            ln.append('.')
        if f[i][j] == 'O':
            ln.append('[')
            ln.append(']')
        if f[i][j] == '@':
            ln.append('.')
            ln.append('.')
            m = [i,j*2]
    g.append(ln[:])
mb = []

def ib(x,y): # In bounds
    if 0 <= x <= h:
        if 0 <= y <= 2*w:
            return True
    return False

def printgrid():
    for i in range(len(g)):
        ln = ''
        for j in range(len(g[i])):
            if i == m[0] and j == m[1]:
                ln = ln + '@'
            else:
                ln = ln + g[i][j]
        print(ln)

def canmoveboxh(x,y,dy,dpth):
    if not ib(x,y+dy):
        print('out of bounds')
        return False
    if g[x][y] == '#':
        return False
    if g[x][y] == '.':
        return True
    if g[x][y] == '[':
        right = canmoveboxh(x,y+2,dy,dpth+1)
        if right:
            mb.append([x,y,x,y+1])
        return right
    if g[x][y] == ']':
        left = canmoveboxh(x,y-2,dy,dpth+1)
        if left:
            mb.append([x,y-1,x,y-2])
        return left
    return False


def canmovebox(x,y,dx,dpth):
    if not ib(x+dx,y):
        return False
    if g[x][y] == '#':
        return False
    if g[x][y] == '.':
        return True
    if g[x][y] == '[':
        left = canmovebox(x+dx,y,dx,dpth+1)
        right = canmovebox(x+dx,y+1,dx,dpth+1)
        if left and right:
            if [x,y,x+dx,y] not in mb:
                mb.append([x,y,x+dx,y])
        return left and right
    if g[x][y] == ']':
        left = canmovebox(x+dx,y-1,dx,dpth+1)
        right = canmovebox(x+dx,y,dx,dpth+1)
        if left and right:
            if [x,y-1,x+dx,y-1] not in mb:
                mb.append([x,y-1,x+dx,y-1])
        return left and right
    return False
ct = 0
fd = False
for i in fi[1]:
    ct += 1
    mb = []
    moved = False
    nm = True
    if i == '>':
        if ib(m[0],m[1]+1):
            if g[m[0]][m[1]+1] == '.':
                m[1] = m[1] + 1
                nm = False
            if g[m[0]][m[1]+1] in '[]' and nm:
                if canmoveboxh(m[0],m[1]+1,1,1):
                    m[1] = m[1] + 1
                    moved = True
    if i == '<':
        if ib(m[0],m[1]-1):
            if g[m[0]][m[1]-1] == '.':
                m[1] = m[1] - 1
                nm = False
            if g[m[0]][m[1]-1] in '[]' and nm:
                if canmoveboxh(m[0],m[1]-1,-1,1):
                    m[1] = m[1] - 1    
                    moved = True
    if i == 'v':
        if ib(m[0]+1,m[1]):
            if g[m[0]+1][m[1]] == '.':
                m[0] = m[0] + 1
                nm = False
            if g[m[0]+1][m[1]] in '[]' and nm:
                if canmovebox(m[0]+1,m[1],1,1):
                    m[0] = m[0] + 1
                    moved = True
    if i == '^':
        if ib(m[0]-1,m[1]):
            if g[m[0]-1][m[1]] == '.':
                #print('up .')
                m[0] = m[0] - 1
                nm = False
            if g[m[0]-1][m[1]] in '[]' and nm:
                if canmovebox(m[0]-1,m[1],-1,1):
                    #print('up []')
                    m[0] = m[0] - 1
                    moved = True
    if moved:
        for b in mb:
            g[b[0]][b[1]] = '.'
            g[b[0]][b[1]+1] = '.'
            g[b[2]][b[3]] = '['
            g[b[2]][b[3]+1] = ']'

tly = 0
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == '[':
            tly += 100 * i + j
print(tly)
