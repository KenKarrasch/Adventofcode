import re

f =  open('16-4.txt').read().split('\n')
lts = ['a','b','c','d','e','f','g','h','i','j','k', \
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def keyw(elem):
    return(elem[1])

nums = 0

for cd in f:
    lt = re.findall("[a-z]",cd.split('[')[0])
    x,ss = [],''
    sid = int(ss.join([x for x in re.findall("[0-9]",cd)]))
    lt.sort()
    for i in lts: x.append([i,lt.count(i)])
    x.sort(key=keyw,reverse=True)
    keyn = cd.split('[')[1][:-1]
    tp = ''
    for i in [0,1,2,3,4]:
        tp += x[i][0]
    if keyn == tp:
        nums += sid        
print('part 1 -',nums)

for cd in f:    
    cp = [x for x in cd.split('[')[0]]
    sid = int(ss.join([x for x in re.findall("[0-9]",cd)]))
    line = ''
    for ch in cp:
        if ch in '-':
            line += ' '
        else:
            line += (chr(ord('a')+(ord(ch)-ord('a')+sid)%26))
    line = line[0:-3]
    if 'north' in line:
        print ('part 2 -',sid)        
