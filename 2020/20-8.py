s = open('20-8.txt').read().split('\n')

g,b,p,d = 0,[0 for i in s],0,False
while (p < len(s)) and not d:
    i = s[p].split()
    if b[p] == 1:
        print 'part 1 -', g
        d = True
    else: b[p] = 1
    if i[0] == 'acc': g += int(i[1])
    if i[0] == 'jmp': p += int(i[1]) - 1
    p += 1

sp = []
for f in range(len(s)):
    if s[f].split()[0] == 'nop':
        sp.append(f)
    if s[f].split()[0] == 'jmp':
        sp.append(f)

for j in sp:
   sd = s[:]
   if 'nop' in s[j]: sd[j] = 'jmp ' + s[j].split()[1]
   if 'jmp' in s[j]: sd[j] = 'nop ' + s[j].split()[1]
   p,d,b,g = 0,False, [0 for i in s],0
   while (p < len(sd)) and not d:
    i = sd[p].split()
    if b[p] == 1:
        d = True
    else: b[p] = 1
    if i[0] == 'acc':
        g += int(i[1])
    if i[0] == 'jmp':
        p += int(i[1]) - 1
    p += 1
   if p == len(s):
      print 'part 2 -',g
