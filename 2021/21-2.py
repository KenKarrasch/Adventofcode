r,x,y = [i.split() for i in open('21-2.txt').read().split('\n')],0,0
for i in r:
    if i[0] == 'forward': x += int(i[1])
    if i[0] == 'down': y += int(i[1])
    if i[0] == 'up': y -= int(i[1])    
print('part 1 -',x*y)
x,y,aim = 0,0,0
for i in r:
    if i[0] == 'forward':
        x += int(i[1])
        y += aim * int(i[1]) 
    if i[0] == 'down': aim += int(i[1])
    if i[0] == 'up': aim -= int(i[1]) 
print('part 2 -',x*y)
