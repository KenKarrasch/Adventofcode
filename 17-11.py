f = open("17-11.txt").read().split(',')
p,d,md = [0,0],[0,0],0
mp = {'ne':[1,1],'n':[0,2],'nw':[-1,1],'sw':[-1,-1],'s':[0,-2],'se':[1,-1]}
for i in f:
    p,d = [p[0]+mp[i][0],p[1]+mp[i][1]],[abs(p[0]),abs(p[1])]           
    if 2*d[1]>d[0]: ds = d[0]+(d[1]-d[0])/2
    else: ds = d[0]
    if md < ds: md = ds
print('part 1 -',ds)
print('part 2 -',md)
