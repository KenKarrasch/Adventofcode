import re

f = open('20-19.txt').read().split('\n\n')

# Made use of the regular expressions in Python. Convert the format
# given in the puzzle to one compliant with Python.

# Had to remember how to do regex expressions.

rs = []
vs = f[0].split('\n')

def dd(tn,depth):
    for v in range(len(vs)):
        if vs[v].split(':')[0] == tn:
            return getj(vs[v].split(':')[1],depth)


def getj(tns,depth): # expect series of tokens e.g. "3 4 5"  or "2 3 | 4 5" or '"a"'
   os = ''
   if '"' in tns:
       return tns.replace('"','').replace(' ','')
   if '|' not in tns: # its a series of numbers e.g. "3 4 5"       
     for tn in tns.split(): # go through each token           
       if (tn == '8') or (tn == '11'):
           if depth < 10: #give it 10 recursions
               os = os + dd(tn,depth+1)
       else:        
           os = os + dd(tn,depth+1)
     return os
   else:
     tnsp = tns.split('|')
     os = '('
     for tn in tnsp[0].split(): # go through each token first part
        if (tn == '8') or (tn == '11'):
           if depth < 10: #give it 10 recursions
               os = os + dd(tn,depth+1)
        else:
            os = os + dd(tn,depth+1)         
     os = os + '|'
     for tn in tnsp[1].split(): # go through each token
        if (tn == '8') or (tn == '11'):
           if depth < 10: #give it 10 recursions
               os = os + dd(tn,depth+1)
        else:
            os = os + dd(tn,depth+1)
     return os + ')'

for v in range(len(vs)):
    if vs[v].split(':')[0] == '0':                
        start = v
tn = vs[start].split(':')[1]
nvs = getj(tn,0)
ms = 0
for st in f[1].split('\n'):  
    p = re.compile(nvs)
    m = p.match(st)
    ite = p.finditer(st)
    good = False    
    for match in ite:
        good = True
        bt = match.span()
        if bt[0] != 0: good = False
        if bt[1] != len(st): good = False        
    if good: ms += 1   
print('part 1 -',ms)

for v in range(len(vs)):
    if vs[v].split(':')[0] == '0':                
        start = v
    if vs[v].split(':')[0] == '8':
        vs[v] = '8: 42 | 42 8'
    if vs[v].split(':')[0] == '11':
        vs[v] = '11: 42 31 | 42 11 31'

nvs = getj(tn,0)
ms = 0
for st in f[1].split('\n'):  
    p = re.compile(nvs)
    m = p.match(st)
    ite = p.finditer(st)
    good = False    
    for match in ite:
        good = True
        bt = match.span()
        if bt[0] != 0: good = False
        if bt[1] != len(st): good = False        
    if good: ms += 1   
print('part 2 -',ms)
