f = open('22-1.txt').read().split('\n')

els,el = [],0
for i in f:
    if len(i) > 0:
        el += int(i)
    else:
        els.append(el)
        el = 0
els.sort()
print 'part 1 -',els[-1]
print 'part 2 -',sum(els[-3::])
