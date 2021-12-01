f = open('15-8.txt').read().split('\n')
t,et,ex = 0,0,0
for l in f:
  et += len(l)
  ch,ct = 1,0
  while ch < len(l)-1:
      if l[ch] == '\\':
        ch += 1
        if l[ch] == 'x':
          ch += 2
      ct += 1
      ch += 1
  ex += 2
  for c in l:
    if c == '\"' or c == '\\':
      ex += 1
    ex += 1
  t += ct
print 'part 1 -',et - t
print 'part 2 -',ex - et
