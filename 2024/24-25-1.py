f = open('24-25.txt').read().split('\n\n')

# quick and easy puzzle, bring on 2025

kys = []
tbrs = []
for i in f:
    br = i.split('\n')
    print(br)    
    if br[0] == '#####':
        ky = []
        for t in range(5):
            dn = False
            for b in range(7):
                if not dn:
                    if br[b][t] == '.':
                        ky.append(b-1)
                        dn = True
        kys.append(ky)
        print('key',ky)
    else:
        tbr = []
        for t in range(5):
            dn = False
            for b in range(7):
                if not dn:
                    if br[6-b][t] == '.':
                        tbr.append(b-1)
                        dn = True
        tbrs.append(tbr)
        print('tbr',tbr)

ct = 0
for t in tbrs:
    for k in kys:
        gd = True
        for tht in range(5):
            if t[tht] + k[tht] > 5:
                gd = False
        if gd: ct += 1
print(ct)  
