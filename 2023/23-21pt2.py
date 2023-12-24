
import copy

# Alot of playing around getting the triangles sorted out. Refining results, double checking
# size with the smaller sample.

# Needed to take into account the flickering, on and off.

# beware the secluded areas that the elves cannot get into.

# elves spread in a diamond shape

# Need to do a smaller diamond that has corners (say 4 times the map with), small triangles, and large triangles.  Then extrapolate

# It is safe to assume that the elves get to all corners at the same time (unlike the sample!)

# DP did not work for this puzzle, just use a grid


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
    
#print gr
def prt(elf,rythm):
 print(rythm)
 for r in range(len(gr)):
    ln = ''
    for c in range(len(gr[r])):
        ltf = False
        if rythm:
         if [r,c] in elfl:                      
            ltf = True          
        if not rythm:
         if [r,c] in elfli:                      
            ltf = True
        if [r,c] in elf:            
            ltf = True
        if ltf: ln += 'o'
        if not ltf:
          if gr[r][c] == '.':
            ln += '_'
          else: ln += gr[r][c]
    print (ln)
    
def prtgr(elf,rythm,x,y):
 print(rythm)
 ct = 0
 for r in range(len(gr)):
    ln = ''
    for c in range(len(gr[r])):
        ltf = False
        if rythm:
         if [r,c] in elfl:                      
            ltf = True          
        if not rythm:
         if [r,c] in elfli:                      
            ltf = True
        if [r,c] in elf:            
            ltf = True
        if ltf: 
          ln += 'o'
        if not ltf:
         if rythm: 
          if bgr[r+bf*l+x*l][c+bf*l+y*l] == '.':
            ln += '_'
          else: ln += bgr[r+bf*l+x*l][c+bf*l+y*l]
          if bgr[r+bf*l+x*l][c+bf*l+y*l] == 'o':
            ct += 1
         else:
          if bgri[r+bf*l+x*l][c+bf*l+y*l] == '.':
            ln += '_'
          else: ln += bgri[r+bf*l+x*l][c+bf*l+y*l]
          if bgri[r+bf*l+x*l][c+bf*l+y*l] == 'o':
            ct += 1
        
    print (ln)
 print(ct) 
 return ct

l =  len(f)

print ('mod',steps%l,'div',steps//l, l)

modn = (steps-(1+(l//2)))%l
divn = (steps-(1+(l//2)))//l

tr = modn - (l//2)
bt = tr + l

print('modn',modn)
print('divn',divn)
print('tr',tr)
print('bt',bt)

divn = steps//l

m = l//2 # 65
p = l-1
print(m)
print(p)

oc = [[st],  [[m,0]],[[m,p]],[[0,m]],[[p,m]],  [[0,0]],[[0,p]],[[p,p]],[[p,0]],  [[0,0]],[[0,p]],[[p,p]],[[p,0]]]
cycl = [steps, modn,modn,modn,modn, tr,tr,tr,tr, bt,bt,bt,bt]
# 0 centre sq, 1 - 4 Corners, 5-8 small triangles, 9 - 12 big triangles

l =  len(f)

#rg = 4+5
#sps = 26501365//l
steps = 26501365
sp = (steps//l)-1
print('sp',sp)
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



print('pls',pls) 

print('cm',cm)

mf = [cm, 1,1,1,1, sp,sp,sp,sp, sp-1,sp-1,sp-1,sp-1]
print('mf',mf)

#     *  
#    ***  
#   *****  
#  *******  
# *********
#  *******  
#   *****  
#    ***  
#     *  


#     o  
#    o+o  
#   oo*oo  
#  o+*+*+o
#   oo*oo  
#    o+o  
#     o  
       
#     o  
#    o+o  
#   oo*oo  
#  o+*+*+o
#   oo*oo  
#    o+o  
#     o  


stc = []
sgns = []
sgna = []

tsl = 0

rs = len(f[0])
cs = len(f)

total = 0

modmode = False

elves,elfl,elfli = [],[],[]

prt([],True)

for ocs in range(len(oc))[0:1]:
 elves,elfl,elfli = [],[],[]
 cyc = cycl[ocs]
 elf = oc[ocs]
 rythm = 0 
 print('elf,cyc',elf,cyc)
 for s in range(cyc):
  #print(s,len(elfl),len(elfli))
  if rythm == 0: rythm = 1
  else: rythm = 0  
  nelf = []  
  for el in range(len(elf)):
     e = elf[el]     
     for d in [0,1,2,3]:
       cc = e[1]+R[d]
       rc = e[0]+C[d]
       if True:
       #if 0 <= cc < cs:
        #if 0 <= rc < rs:       
         #if gr[rc][cc] != '#' : 
         if gr[rc%l][cc%l] != '#' : 
         #if bgr[rc+bf*l][cc+bf*l] != '#' : 
          if not modmode:
          #if [rc,cc] not in nelf:
           if rythm:
             if bgr[rc+bf*l][cc+bf*l] != 'o':
               nelf.append([rc,cc])                
               bgr[rc+bf*l][cc+bf*l] = 'o'
           else:
             if bgri[rc+bf*l][cc+bf*l] != 'o':
               nelf.append([rc,cc])                
               bgri[rc+bf*l][cc+bf*l] = 'o'               
          if modmode:
           if [rc,cc] not in elfl: 
            if [rc,cc] not in elfli:
             nelf.append([rc,cc])     
             if rythm: 
              if [rc,cc] not in elfl:                 
                elfl.append([rc,cc])
             else: 
              if [rc,cc] not in elfli:                 
                elfli.append([rc,cc])  
               
  elf = copy.deepcopy(nelf)  
  if s == cyc:
    #prt(elf,rythm)
    if rythm:
      print('elves',len(elfl))     
    else:
      print('elves inv',len(elfli))

 if s == cyc-1: 
   cntr = prtgr(elf,rythm,0,0)
   cntrn = prtgr(elf,rythm,0,1)
   
   bcnr = prtgr(elf,rythm,4,0)
   tcnr = prtgr(elf,rythm,-4,0)
   rcnr = prtgr(elf,rythm,0,4)
   lcnr = prtgr(elf,rythm,0,-4)
   
   setrs = prtgr(elf,rythm,4,1)
   swtrs = prtgr(elf,rythm,4,-1)
   netrs = prtgr(elf,rythm,-4,1)
   nwtrs = prtgr(elf,rythm,-4,-1)

   setrl = prtgr(elf,rythm,3,1)
   swtrl = prtgr(elf,rythm,3,-1)
   netrl = prtgr(elf,rythm,-1,3)
   nwtrl = prtgr(elf,rythm,-1,-3)

 if rythm:
   print('elves',len(elfl))
   total += len(elfl) * mf[ocs]
 else:
   print('elves inv',len(elfli))  
   total += len(elfli) * mf[ocs] 
 print(total)

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
print(len(elfli),len(elfl))
print(ct)
print(total)

print('smtr,bgtr,pls,mns',smtr,bgtr,pls,mns)

print(cntr,cntrn)
print(bcnr,tcnr,rcnr,lcnr)
print(setrs,swtrs,netrs,nwtrs)
print(setrl, swtrl , netrl , nwtrl)

tsqs = pls * cntr + mns * cntrn
tcnrs = bcnr + tcnr + rcnr + lcnr
tstr = smtr * (setrs + swtrs + netrs + nwtrs)
tltr = bgtr * (setrl + swtrl + netrl + nwtrl)
        
print('part 2',tsqs + tcnrs + tstr + tltr)


# 600336060511101 correct answer
# 598740005759841

# 1000 steps = 857085
# 131 + 131 + 131 + 131 + 65 steps = 297357
# 131 + 131 + 131 + 65 steps = 179936
# 131 + 131 + 65 steps = 91853
