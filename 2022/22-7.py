f = open('22-7.txt').read().split('\n')
# Struggled with this one, read too much into the technical wording of the problem and thought they were asking to do
# something weird, e.g. double counting the subdirectories.  But it turned out to be simpler than I thought,
# I should have simply went with what the storyline was asking for.
pth = ['/']
ds = {}
for i in f[1::]:
    c = i.split()
    print(c)
    if c[0] == '$':
        if c[1] == 'cd':
            if (c[2] != '..'):
                pth.append(c[2])
            else:             
                pth.pop()            
    else:
        if c[0] != 'dir':
            path = ''
            for i in pth:
                path += '/' + i
                if path in ds.keys():
                    ds[path] += int(c[0])
                else:
                    ds[path] = int(c[0])
t = 0
for k,v in ds.items():
    print(k,v)
    if v <= 100000:
        t += v
print('part 1 -',ds['//'])
cd = []
for k,v in ds.items():
    if 30000000 < v + 70000000 - ds['//']:
        cd.append(v)
print('part 2 -',min(cd))
