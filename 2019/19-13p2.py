import sys
import collections

# another fun intcode puzzle, needed to code some basic ai to control the
# paddle.  Simply follows the ball x-coordinate. The last few blocks take a
# a while to get.  One would have to wonder whether it is possible for
# some puzzles to be uncompletable.

r = list(map(int, open('19-13.txt').read().split(',')))

def pad(st):
  g = ''
  for u in range(5-len(st)): g += '0'
  return g + st

def gmd(m,rb):
    a1 = a2 = a3 = 0
    if m[2] == '2': a1 = rb 
    if m[1] == '2': a2 = rb
    if m[0] == '2': a3 = rb
    return([a1,a2,a3])

def printgame(os,printmap):
        global alldone
        if printmap: print('os',len(os))
        maxx,maxy = 0,0
        for a in range(int(len(os)/3)):          
          if os[(a*3)+0] > maxx:
            maxx = os[(a*3)+0]
        for a in range(int(len(os)/3)):          
          if os[(a*3)+1] > maxy:
            maxy = os[(a*3)+1]
        bd = {}
        ct = 0
        score = 0
        for a in range(int(len(os)/3)):
          if os[a*3] != -1:
            bd[(os[a*3],os[(a*3)+1])] = os[(a*3)+2]
          if os[a*3] == -1:
            score = os[a*3+2]
        if printmap: print('score',score)            
        for y in range(maxy):
          ln = ''
          for x in range(maxx):
            if (x,y) in bd:
             if bd[(x,y)] == 0:
               ln += ' '
             if bd[(x,y)] == 1:
               ln += '|'
             if bd[(x,y)] == 2:
               ln += '#'
               ct += 1
             if bd[(x,y)] == 3:
               ln += '='
               paddle = x
             if bd[(x,y)] == 4:
               ln += 'o'
               ball = x               
            else:
             ln += ' '
          if printmap:
            print(ln)
            
        if ct < 1:
          alldone = True
        if printmap:
           print('blocks left',ct)
        return ball,paddle
      
def game(g): 
    f = collections.defaultdict(lambda: 0, enumerate(r))
    s = g
    f[0] = g
    os = []
    view = 0
    lk = 0
    ps,dr,rob,op,rb = {(0,0):s},0,(0,0),0,0
    d = [[0,-1],[1,0],[0,1],[-1,0]]#ULDR
    if True:    
      os = []
      while f[op] != 99:    
        i = pad(str(f[op]))
        o = i[-2:]
        [a1,a2,a3] = gmd(i[:3],rb)
        if int(o) < 10:
           if i[2] == '1':
              op1 = f[op+1]
           else:
              op1 = f[a1+f[op+1]]
        if int(o) in [1,2,5,6,7,8]:
            if i[1] == '1':
               op2 = f[op+2]
            else:
               op2 = f[a2+f[op+2]]
        if o == '01':
            f[a3+f[op+3]] = op1+op2
            op += 2
        if o == '02':
            f[a3+f[op+3]] = op1*op2
            op += 2
        if o == '03':
              if (view % 1000 == 0) or alldone:
                ball,paddle = printgame(os,True)
              else:
                ball,paddle = printgame(os,False)
              view += 1              
              if ball > paddle:
                f[a1+f[op+1]] = 1
              if ball < paddle:
                f[a1+f[op+1]] = -1
              if ball == paddle:
                f[a1+f[op+1]] = 0              
                
        if o  == '04':            
            os.append(op1)
            lk
            if op1 == -1:
               lk = 0
            if lk == 2:
               print('score - ',op1)
            lk += 1
               
        if o == '05':
            if op1 != 0:
                op = op2 - 2
            else:
                op += 1
        if o == '06':
            if op1 == 0:
               op = op2 - 2
            else:
               op += 1
        if o == '07':
            if op1 < op2:
              f[f[op+3]+a3] = 1
            else:
              f[f[op+3]+a3] = 0
            op += 2
        if o == '08':
            if op1 == op2:
                 f[f[op+3]+a3] = 1
            else:
                 f[f[op+3]+a3] = 0
            op += 2
        if o == '09':            
            rb += op1
        op += 2
      return(os)
    
alldone = False
    
game(1)

os = game(2)
