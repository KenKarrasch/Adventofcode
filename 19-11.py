import sys
import collections

#part 1 - 2093
#part 2 -
# ###....##.###..#..#.#......##.#..#.###.
# #..#....#.#..#.#.#..#.......#.#..#.#..#
# ###.....#.#..#.##...#.......#.#..#.#..#
# #..#....#.###..#.#..#.......#.#..#.###.
# #..#.#..#.#.#..#.#..#....#..#.#..#.#...
# ###...##..#..#.#..#.####..##...##..#...

# Incorporated the panel calculations in the Intcode program
# which may backfire in future intcode puzzles.
# Still getting used to lists over arrays.
# Took a while trying to get a meaningful picture of code for part 2.

r = list(map(int, open('19-11.txt').read().split(',')))

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

for a in [0,1]:       
    f = collections.defaultdict(lambda: 0, enumerate(r))
    outputs,ps,dr,rob,op,rb = [],{(0,0):a},0,(0,0),0,0
    d = [[0,-1],[1,0],[0,1],[-1,0]]#ULDR
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
             if rob in ps:
              f[a1+f[op+1]] = ps[rob]              
             else:
              f[a1+f[op+1]] = 0
        if o  == '04':
            outputs.append(op1)
            if len(outputs) > 1:       
                ps[rob] = outputs[0]
                if outputs[1]:
                  dr += 1
                else:
                  dr -= 1
                outputs = []
                dr = dr % 4              
                rob = (rob[0] + d[dr][0], rob[1] + d[dr][1])                
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
  
    if a == 0: print('part 1 -',len(ps))
    if a == 1:
      print ('part 2 -')
      for y in range(6):
        line = ""
        for x in range(39):
          if (x+1,y) in ps:
            if ps[(x+1,y)] == 0:              
              line += '.'
            else:
              line += '#'
          else:
            line += '#'
        print(line)
