import re

s = open('20-4.txt').read().split('\n')
# Data processing puzzle, my code is a bit dirty but it works

# update: fixed code to better detect invalid inputs
# problems found with the original solution:
# - did not detect hex numbers correctly (#123abz was counted as a valid solution)
# - did not check year numbers had exactly four digits
# - did not check height record had 'in' and 'cm' at the end ('cm190' was incorrectly counted as a valid input)
# - did not check that haircolor had 6 hexdigits

# - part one is still dodgy

# I have made use of regular expressions for practice

t = 0
st = [-1]

for p in range(len(s)):
    if s[p] == "":
        st.append(p)

st.append(len(s)+1)
fre = []
for r in range(len(st)-1):
    rec = s[st[r]+1:st[r+1]]
    recs = ''
    for r in rec:        
        recs = recs + ' ' + r
    fre.append(recs)

v = 0
vs = []
for e in fre:
    if (('byr' in e) and
       ('iyr' in e) and
       ('eyr' in e) and
       ('hgt' in e) and
       ('hcl' in e) and
       ('ecl' in e) and
       ('pid' in e)):
        vs.append(e)
print('part 1 -',len(vs))

def g(ss,t):
    s = t.split(ss)
    ts = s[1].split(':')
    tx = ts[1].split(' ') 
    return(tx[0])

v = 0
for e in vs:
    vd = True
    byr = g('byr',e)
    if(not re.match(r'^[\d]{4}$',byr)):
        vd = False
    byr = int(byr)
    if (byr < 1920) or (byr > 2002):
        vd = False
    iyr = g('iyr',e)
    if(not re.match(r'^[\d]{4}$',iyr)):
        vd = False
    iyr = int(iyr)
    if (iyr < 2010) or (iyr > 2020):
        vd = False
    eyr = g('eyr',e)
    if(not re.match(r'^[\d]{4}$',eyr)):
        vd = False
    eyr = int(eyr)
    if (eyr < 2020) or (eyr > 2030):
        vd = False
    hgt = g('hgt',e)
    #if ('cm' not in hgt) and ('in' not in hgt):
    if (not hgt.endswith('cm')) and (not hgt.endswith('in')):
        vd = False
    if 'cm' in hgt:
        ht = int(hgt.split('cm')[0])        
        if (ht < 150) or (ht > 193):
            vd = False
    if 'in' in hgt:
        ht = int(hgt.split('in')[0])
        if (ht < 59) or (ht > 76):
            vd = False
    hcl = g('hcl',e)
    if (hcl[0] not in '#'):
        vd = False
    #for i in range(len(hcl)-1):        
        #if hcl[i+1] not in '1234567890abcdef':
        
    if(not re.match(r'^#[\da-f]{6}$',hcl)):
        vd = False
    ecl = g('ecl',e)
    if ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
        vd = False
    pid = g('pid',e)
    #if len(pid) != 9:
        #vd = False
    #for i in pid:        
        #if i not in '1234567890':
    if(not re.match(r'^[\d]{9}$',pid)):
            vd = False
    if vd:
        v += 1

print('part 2 -',v)
