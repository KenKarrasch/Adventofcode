import copy
f = open('22-17.txt').read().split('\n')

# Part 1 - Just like tetris, I wrote a tetris game 30yrs ago, came in handy knowing the rules. 

# Part 2 - Just look for a repeat pattern then extropolate.



r = []
r.append(['####'][::-1])
r.append(['.#.','###','.#.'][::-1])
r.append(['..#','..#','###'][::-1])
r.append(['#','#','#','#'][::-1])
r.append(['##','##'][::-1])

w = [4,3,3,1,2]


inst = [c for c in f[0]]

kinst = inst[:]

gd = []
for i in range(1000):
    ln = []
    for j in range(7):
        ln.append('.')
    gd.append(ln)

#two units away from the left wall and its bottom edge is three units abov

fall = 3
ofssr = 2
rt = 0
rh = fall+1
ofs = ofssr


rot = 0
nst = True

def pr():
    st = False
    pgd = copy.deepcopy(gd)
    for i in range(len(r[rt]))[::-1]:
      for j in range(len(r[rt][i])):        
        if r[rt][i][j] == '#':
         pgd[rh+i][j+ofs] = '@'
    for i in pgd[::-1]:
      if '@' in i:
        st = True
      if st:
        si = '|'
        for l in i:
          si += l
        si += '|'
        print(si)
    print('+-------+')

#pr()

def gethgst():
  ct = 0 
  for i in gd:    
    if '#' not in i:  
      return ct 
    else:
      ct += 1     

def coll():
    hit = False
    if rh < 0:
      return True
    for i in range(len(r[rt]))[::-1]:
      for j in range(len(r[rt][i])): 
        if r[rt][i][j] == '#':            
          if gd[rh+i][j+ofs] == '#':
            hit = True
    return hit

gr_b = True
freefall = False
ct = 0
rf = 0
rocks = 0
ht = 0
signature = []
srock = []
shgts = []
done = False

tgt = 1000000000000
#tgt = 2022
#tgt = 8000

htd = 0
thtd = 0
fnddup = False
numdups = 0

while not done:#rocks <=:#len(inst) > 0:
    pofs,prh = ofs,rh
    if gr_b:
       rh -= 1
       #print('gravity')
    else: 
      if not freefall:
       ch = inst[rf]
       rf = (rf+1)%len(inst)
       #print('rf',rf)       
       #print(ch,inst[::-1],len(inst))       
       if ch == '>': ofs += 1
       else: ofs -= 1      
       if ofs < 0: ofs = 0
       if ofs + len(r[rt][0]) > 7: ofs -= 1
       
       if rf == 0:
          sht = gethgst()-1
          bs = ''
          for i in range(40):
            for j in range(7):
               bs += gd[sht-i][j]               
          sig = (rh,ofs,rt,bs)
          if not fnddup:          
           if sig in signature:
            #pr()
            #print('double found')        
            dupn = 0
            for i in range(len(signature)):
                if signature[i] == sig:
                    #print('srock[i]','first',srock[i],'second',rocks)   
                    diff = rocks - srock[i]
                    #print('rock diff (period)',diff)
                    periods = (tgt - rocks)//diff
                    #print('periods required',periods)
                    rocks += periods*diff
                    #print('sig',sig,'i',i,'len(srock)',len(srock))
                    #print('signature[i]',signature[i])
                    htd = (sht+rot) - shgts[i]   
                    #print('shgts',shgts[i],sht,rot)                               
                    #print('htd',htd)               
                    thtd = periods*htd    
                    #print('new rocks',rocks)
                    fnddup = True                      
          if rocks > 2022:             
            signature.append(sig)  
            srock.append(rocks)
            shgts.append(sht+rot)


    gr_b = not gr_b   
    if coll() and gr_b:     
        ofs,rh = pofs,prh         
    if coll():       
      if not gr_b:
        rh += 1
      else:
        ofs,rh = pofs,prh
      for i in range(len(r[rt]))[::-1]:
        for j in range(len(r[rt][i])):
          if r[rt][i][j] == '#':      
            gd[rh+i][j+ofs] = '#'
      ht = gethgst()
      rh = fall + ht
      ofs = ofssr
      rt = (rt + 1)%5
      gr_b = False
      freefall = False
      rocks += 1
      buf = 50
      if ht > 2*buf:
        ngd = []
        for i in range(8*buf):
            ngd.append(gd[i+buf][:])
        for i in range(8*buf):              
            gd[i] = ['.','.','.','.','.','.','.']
        for i in range(8*buf):              
            gd[i] = ngd[i][:]
        rh -= buf        
        rot += buf
      if(rocks%5000 == 0):                
        print('scanning rock',rocks, ht+rot)
      if(rocks == 2022):                
        print('part 1 -',rocks, ht+rot)
      if(rocks == tgt):  
        print('part 2 -', thtd+ht+rot)     
        done = True               
