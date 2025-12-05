f = open('25-5.txt').read().split('\n\n')

ig = [int(x) for x in f[1].split('\n')]
iri = [x.split('-') for x in f[0].split('\n')]

ir = []
for h in iri:
    ir.append((int(h[0]),int(h[1])))

tly = 0
for i in ig:
    gd = False
    for j in ir:        
        if i > j[0] and i <= j[1]:
            gd = True
    if gd:
        tly += 1
print (tly)

# 8 min solve 
#  5     402   1717  **
