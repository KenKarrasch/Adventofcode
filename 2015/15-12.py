import json
t = json.loads(open('15-12.txt').read())

def gb(tt,p):
    if isinstance(tt,dict): return gbr(tt,p)    
    if isinstance(tt,list): return gsq(tt,p)
    return tt

def gbr(ts,p):  
 tl = 0
 for i in ts:
    ng = gb(ts[i],p)      
    if isinstance(ng,str):
      if (ng == 'red') and (p == 2): return 0
    else: tl += ng
 return tl

def gsq(ts,p):
 i,ty = 0,0 
 while i < len(ts):
   if isinstance(gb(ts[i],p),int): ty += gb(ts[i],p) 
   i += 1
 return ty

print('part 1 -',gsq(t,1))
print('part 2 -',gsq(t,2))
