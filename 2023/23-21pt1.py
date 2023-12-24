
import copy

# Part 1 - Need cleaning up

f = open('23-21.txt').read().split('\n')

gr = []
st = []

sts = []

for i in range(len(f)):
    ln = []
    for j in range(len(f[0])):
        ln.append(f[i][j])
        if f[i][j] == 'S':
           st = [i,j]
        if f[i][j] == '#':
           sts.append([i,j])
    gr.append(ln)


l =  len(f)

bgr = []
bgri = []

#steps = 270
#steps = 26501365
#steps = 131 + 131 + 131 + 65

steps = 131 + 131 + 131 + 131 + 65
#steps = 131 + 131 + 65
#steps = 100

#steps = 1000

bf = 3+steps//l


for i in range((bf*2+1)*l):
    ln = []
    for j in range((bf*2+1)*l):
        ln.append(f[i%l][j%l])
    bgr.append(ln[:])
    bgri.append(ln[:])


R = [0,1,0,-1]
C = [1,0,-1,0]
    
  

l =  len(f)


modn = (steps-(1+(l//2)))%l
divn = (steps-(1+(l//2)))//l

tr = modn - (l//2)
bt = tr + l


divn = steps//l

m = l//2 # 65
p = l-1

oc = [[st],  [[m,0]],[[m,p]],[[0,m]],[[p,m]],  [[0,0]],[[0,p]],[[p,p]],[[p,0]],  [[0,0]],[[0,p]],[[p,p]],[[p,0]]]
cycl = [steps, modn,modn,modn,modn, tr,tr,tr,tr, bt,bt,bt,bt]
# 0 centre sq, 1 - 4 Corners, 5-8 small triangles, 9 - 12 big triangles

l =  len(f)


steps = 26501365
sp = (steps//l)-1
rg = sp + sp - 1 
cm = rg
fc = 1
for i in range(rg//2):
  cm += 2*fc
  fc += 2

pls = sp * sp
mns = (sp+1)*(sp+1)
smtr = sp + 1
bgtr = sp


stc = []
sgns = []
sgna = []

tsl = 0

rs = len(f[0])
cs = len(f)

total = 0


for ocs in [0]:
 cyc = 64
 elf = oc[ocs]
 rythm = 0 
 for s in range(cyc):
  if rythm == 0: rythm = 1
  else: rythm = 0  
  nelf = []  
  for el in range(len(elf)):
     e = elf[el]     
     for d in [0,1,2,3]:
       cc = e[1]+R[d]
       rc = e[0]+C[d]
       if 0 <= cc < cs:
        if 0 <= rc < rs:       
         if gr[rc][cc] != '#' :  
           if rythm:
             if bgr[rc+bf*l][cc+bf*l] != 'o':
               nelf.append([rc,cc])                
               bgr[rc+bf*l][cc+bf*l] = 'o'
           else:
             if bgri[rc+bf*l][cc+bf*l] != 'o':
               nelf.append([rc,cc])                
               bgri[rc+bf*l][cc+bf*l] = 'o'               

               
  elf = copy.deepcopy(nelf)  


ct = 0 
if rythm:
 for i in range((bf*2+1)*l):    
    for j in range((bf*2+1)*l):
       if bgr[i][j] == 'o':
          ct += 1  
else:
  for i in range((bf*2+1)*l):    
    for j in range((bf*2+1)*l):
       if bgri[i][j] == 'o':
          ct += 1  

print('part 1',ct)
