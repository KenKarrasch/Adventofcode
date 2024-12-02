
# Online Python - IDE, Editor, Compiler, Interpreter

f = open("24-2.txt").read().split('\n')
print(f)

ct = 0
for i in f:
    ns = [int(i) for i in i.split()]
    
    gd = True
    inc = True
    dec = True
    for j in range(len(ns)-1):
        
        if ns[j] < ns[j+1]:
            dec = False
        if ns[j] > ns[j+1]:
            inc = False
        if ns[j] == ns[j+1]:
            gd = False
        if abs(ns[j] - ns[j+1]) < 0:
            gd = False
        if abs(ns[j] - ns[j+1]) > 3:
            gd = False
    if gd:
        print(gd,inc,dec)
        if inc or dec:
            
            print(inc,dec)
            print('good',i)
            ct += 1
print(ct)
