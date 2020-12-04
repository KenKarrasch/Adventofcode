s = open('20-4.txt').read().split('\n')
# Data processing puzzle, my code is a bit dirty but it works
t = 0
st = [-1]

for p in range(len(s)):
    if s[p] == "":
        st.append(p)

st.append(len(s)+1)
re = []
for r in range(len(st)-1):
    rec = s[st[r]+1:st[r+1]]
    recs = ''
    for r in rec:        
        recs = recs + ' ' + r
    re.append(recs)

v = 0
vs = []
for e in re:
    if (('byr' in e) and
       ('iyr' in e) and
       ('eyr' in e) and
       ('hgt' in e) and
       ('hcl' in e) and
       ('ecl' in e) and
       ('pid' in e)):
        v += 1
        vs.append(e)
print('part 1 -',len(vs))

def getinfo(ss,t):
    s = t.split(ss)
    ts = s[1].split(':')
    tx = ts[1].split(' ') 
    return(tx[0])

v = 0
for e in vs:
    vd = True
    byr = int(getinfo('byr',e))
    if (byr < 1920) or (byr > 2002):
        vd = False
    iyr = int(getinfo('iyr',e))
    if (iyr < 2010) or (iyr > 2020):
        vd = False
    eyr = int(getinfo('eyr',e))
    if (eyr < 2020) or (eyr > 2030):
        vd = False
    hgt = getinfo('hgt',e)
    if ('cm' not in hgt) and ('in' not in hgt):
        vd = False
    if 'cm' in hgt:
        ht = int(hgt.split('cm')[0])        
        if (ht < 150) or (ht > 193):
            vd = False
    if 'in' in hgt:
        ht = int(hgt.split('in')[0])
        if (ht < 59) or (ht > 76):
            vd = False
    hcl = getinfo('hcl',e)
    if (hcl[0] not in '#'):
        vd = False
    for i in range(len(hcl)-1):        
        if hcl[i+1] not in '1234567890qwertyuiopasdfghjklzxcvbnm':
            vd = False
    ecl = getinfo('ecl',e)
    if ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
        vd = False
    pid = getinfo('pid',e)
    if len(pid) != 9:
        vd = False
    for i in pid:        
        if i not in '1234567890':
            vd = False
    if vd:
        v += 1

print('part 2 -',v)
