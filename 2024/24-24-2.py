# Not a general solution
# Only posting for interest.  


def simulate_gates(initial_values, gate_connections):
    wires = initial_values.copy()
    
    def get_wire_value(wire):
        return wires.get(wire, None)
    
    def set_wire_value(wire, value):
        wires[wire] = value
    
    def evaluate_gate(gate_type, input1, input2):
        if gate_type == 'AND':
            return input1 & input2
        elif gate_type == 'OR':
            return input1 | input2
        elif gate_type == 'XOR':
            return input1 ^ input2
    
    while True:
        changes = False
        for connection in gate_connections:
            parts = connection.split()
            if len(parts) == 5:  # Normal gate operation
                input1, gate_type, input2, _, output = parts
            elif len(parts) == 3:  # Direct assignment
                input1, _, output = parts
                gate_type = 'ASSIGN'
            else:
                continue  # Skip invalid connections
            
            if gate_type == 'ASSIGN':
                if input1 in wires and output not in wires:
                    set_wire_value(output, wires[input1])
                    changes = True
            elif input1 in wires and input2 in wires and output not in wires:
                result = evaluate_gate(gate_type, wires[input1], wires[input2])
                set_wire_value(output, result)
                changes = True
        
        if not changes:
            break
    
    return wires


def parse_input(input_text):
    lines = input_text.strip().split('\n')
    initial_values = {}
    gate_connections = []    
    for line in lines:
        if ':' in line:
            wire, value = line.split(':')
            initial_values[wire.strip()] = int(value.strip())
        elif '->' in line:
            gate_connections.append(line.strip())
    
    return initial_values, gate_connections

input_text = open('24-24m3.txt').read()


              
cd = [['z11','vkq']]
for i in cd:
    c1 = i[0]
    c2 = i[1]
    for t in range(len(input_text)):                             
        if input_text[t].endswith('-> ' + c1):                       
            input_text[t] = input_text[t].replace(c1,c2)                    
        if input_text[t].endswith('-> ' + c2):                    
            input_text[t] = input_text[t].replace(c2,c1)

print('z11',input_text[190])


it = input_text.split('\n')  
#if False:
#for pg in [['pwp','mmk'],['fnc','srb'],['pvb','qdq']]:
if False:
    #for pg in [['pwp','mmk']]:    
    for t in range(len(it)):                    
        if it[t].endswith('-> ' + pg[0]):  
            it[t] = it[t].replace(pg[0],pg[1])                    
        if it[t].endswith('-> ' + pg[1]):  
            it[t] = it[t].replace(pg[1],pg[0])                    

                
itn = '\n'.join(it)
#input_text = itn

txt = input_text.split('\n\n')[1].split('\n')
prog = []
for i in txt:
    #print(i)
    prog.append(i.split())



replacelist = {}
print('-------------------------------')
for i in prog:
    if i[4].startswith('z') and len(i[4]) == 3:
        for opn in [0,2]:            
            if not i[0].startswith('x') and not i[0].startswith('y'):
                w1 = i[opn]
                r1 = str(opn) + '-' + i[4]     
                replacelist[r1] = w1
                #print('replacement added',w1,r1,replacelist[r1],r1)               
                for w in range(len(prog)):
                    for op in range(len(prog[w])):
                        if prog[w][op] == w1:                           
                            prog[w][op] = r1
                            

#for i in prog:
    #print(i)
 #   print(' '.join(i))

print('-------------------------------')

for i in prog:
    if i[0][2] == 'z':
        if len(i[4]) == 3 and 'z' not in i[4]:
            w1 = i[4]
            r1 = '3-' + i[0][2] + i[0][3] + i[0][4]
            replacelist[r1] = w1
            #print('replacement added',w1,r1,replacelist[r1],r1)                                                                 
            for w in range(len(prog)):
                for op in range(len(prog[w])):
                    if prog[w][op] == w1:                                               
                        prog[w][op] = r1

#for i in prog:
    #print(i)
   # print(' '.join(i))


print('-------------------------------')

for rd in [5,6,7,8]:
    for i in prog:
        if i[4][2] == 'z':
            if len(i[0]) == 3 and i[0][0] not in 'xy' and 'z' not in i[0]:
                w1 = i[0]
                nrd = 0
                r1 = str(nrd) + '-' + i[4][2] + i[4][3] + i[4][4]
                while r1 in replacelist.keys():
                    nrd += 1
                    r1 = str(nrd) + '-' + i[4][2] + i[4][3] + i[4][4]                    
                replacelist[r1] = w1
                #print('replacement added',w1,r1,replacelist[r1],r1)    
                for w in range(len(prog)):
                    for op in range(len(prog[w])):
                        if prog[w][op] == w1:                                                        
                            prog[w][op] = r1

#for i in prog:
    #print(i)
    #print(' '.join(i))

print('-------------------------------')

for rd in [1,2,3,4]:
    for i in prog:
        if i[4][2] == 'z':
            if len(i[2]) == 3 and i[2][0] not in 'xy' and 'z' not in i[2]:
                w1 = i[2]
                nrd = 0
                r1 = str(nrd) + '-' + i[4][2] + i[4][3] + i[4][4]
                while r1 in replacelist.keys():
                    nrd += 1
                    r1 = str(nrd) + '-' + i[4][2] + i[4][3] + i[4][4]                                        
                replacelist[r1] = w1
                #print('replacement added',w1,r1,replacelist[r1],r1)    
                for w in range(len(prog)):
                    for op in range(len(prog[w])):
                        if prog[w][op] == w1:                                  
                            prog[w][op] = r1

#for i in prog:
    #print(i)
    #print(' '.join(i))


print('-------------------------------')
strs = []
for i in prog:
    #print(' '.join(i))
    strs.append(' '.join(i))

print('-------------------------------')

#for i in prog:
    #print(i)
    #for j in [0,2,4]:
       # if len(i[j]) == 3 and i[j][0] not in 'xzy':
            #print(i[j])   

strs.sort()
problems = []

#print(replacelist)

for sign in range(45)[8:16]:
    ors = ands = xors = 0
    ct = 0
    print('searching for',sign)
    signs = str(sign)
    if sign < 10:
        signs = '0' + signs    
    signs = 'z' + signs            
    for i in strs:
        if i.endswith(signs):
            if i.split(' -> ')[1] in replacelist.keys():
                print(i,'(' + replacelist[i.split('-> ')[1]]+ ')')
            else:
                print(i,'(' + i.split('-> ')[1] + ')')
            ct += 1
            if ' AND ' in i: ands += 1
            if ' OR ' in i: ors += 1
            if ' XOR ' in i: xors += 1

    if ct != 5:
        problems.append(sign)
    print('aox',ands,ors,xors)    
    if (ands,ors,xors) != (2,3,2):
        if sign not in problems:
            problems.append(sign)
    print()
  


#print('problem gates',problems)
#print('replace list:',replacelist)
#for k,v in replacelist.items():
#    print('replacement',k,'with',v)



realproblems = []
for i in problems:
    if i != 0 and i != 1 and i != 44:
        realproblems.append(i)

#print('realproblems',realproblems)
#print('replacelist',replacelist)

realproblems = [24,25]
#realproblems = [12,13]

swapcandidates = []

for pr in range(len(realproblems)//2):
    swapcandidate = []
    c1 = str(realproblems[2*pr])
    if realproblems[pr] < 10:
        c1 = '0' + c1   
    c2 = str(realproblems[2*pr+1])
    if realproblems[pr] < 10:
        c2 = '0' + c2
    #print('candidate 1 & 2',c1,c2)
    for i in range(len(prog)):
        for c in [c1,c2]:            
            if c in prog[i][4]:
                #print('candidate',prog[i][4])
                if prog[i][4] not in list(replacelist.keys()):
                    #print(prog[i][4])
                    swapcandidate.append(prog[i][4])
                else:
                    #print(replacelist[prog[i][4]])
                    swapcandidate.append(replacelist[prog[i][4]])
    swapcandidates.append(swapcandidate)
#print('swapcandidates',swapcandidates)



#realproblems = [24,25]
#swapcandidates = []
if False:#for pr in range(3):#len(realproblems)//2):
    swapcandidate = []
    c1 = str(realproblems[0])
    if realproblems[0] < 10:
        c1 = '0' + c1   
    c2 = str(realproblems[1])
    if realproblems[1] < 10:
        c2 = '0' + c2
    c3 = str(realproblems[2])
    if realproblems[2] < 10:
        c3 = '0' + c3
    #print('candidate 1 & 2',c1,c2)
    for i in range(len(prog)):
        for c in [c1,c2,c3]:            
            if c in prog[i][4]:
                #print('candidate',prog[i][4])
                if prog[i][4] not in list(replacelist.keys()):
                    #print(prog[i][4])
                    swapcandidate.append(prog[i][4])
                else:
                    #print(replacelist[prog[i][4]])
                    swapcandidate.append(replacelist[prog[i][4]])
    swapcandidates.append(swapcandidate)
#print('swapcandidates',swapcandidates)



#------------------------------

txt = input_text.split('\n\n')[1].split('\n')
prog = []
for i in txt:
    #print(i)
    prog.append(i.split())

# find X/y ands
prs = []
ipr = []

#for ao in ['AND','OR','XOR']:
for sc in swapcandidates[0:1]:
    for ao in ['AND','XOR']:
        ipr = []
        for g in prog:
            for c in sc:
                if g[4] == c:
                    if g[1] == ao:                    
                        if g[0][0] in 'xy':                            
                            ipr.append(c)
        prs.append(ipr)
    for ao in ['AND','XOR','OR']:
        ipr = []
        for g in prog:
            for c in sc:
                if g[4] == c:
                    if g[1] == ao:                    
                        if g[0][0] not in 'xy':                            
                            ipr.append(c)
        prs.append(ipr)

#print('pairs',prs)


def get_bit(number, bit_position):
    return (number >> (bit_position)) & 1


#print('input text',input_text[:])

found = []

aprobs = []


if False:
#for bt in range(2**len(prs)):        
    it = input_text.split('\n')  
    #if False:
    if False:
    #for pg in [['pwp','mmk'],['fnc','srb'],['pvb','qdq']]:
        for t in range(len(it)):                    
            if it[t].endswith('-> ' + pg[0]):  
                it[t] = it[t].replace(pg[0],pg[1])                    
            if it[t].endswith('-> ' + pg[1]):  
                it[t] = it[t].replace(pg[1],pg[0])                    
    for btf in range(len(prs)):        
        if get_bit(bt, btf):
            for t in range(len(it)):                    
                if it[t].endswith('-> ' + prs[btf][0]):       
                    print('swapping',prs[btf][0],prs[btf][1])                                 
                    it[t] = it[t].replace(prs[btf][0],prs[btf][1])                    
                if it[t].endswith('-> ' + prs[btf][1]):                    
                    it[t] = it[t].replace(prs[btf][1],prs[btf][0])

cd = [['fnc','srb'],['pvb','qdq']]
if False:
    #for i in cd:
    c1 = i[0]
    c2 = i[1]
    for t in range(len(it)):                             
        if it[t].endswith('-> ' + c1):                       
            it[t] = it[t].replace(c1,c2)                    
        if it[t].endswith('-> ' + c2):                    
            it[t] = it[t].replace(c2,c1)
        
#swapcandidates = [['pwp','mmk']]


#print(len(swapcandidates))
#if False:
# mmk <-> Z24
# pvb <-> qdq
# vkq <-> z11
# z38 <-> hqh

seq = ['mmk', 'z24', 'pvb', 'qdq', 'vkq', 'z11', 'z38', 'hqh']
seq.sort()
print('answer',seq)

#for sp in [['z11','vkq']]:        
if True:
        #print(sp)
        #c1 = sp[0]
        #c2 = sp[1]
        it = input_text.split('\n')  
        #for t in range(len(it)):                             
        #    if it[t].endswith('-> ' + c1):                       
        #        it[t] = it[t].replace(c1,c2)                    
        #    if it[t].endswith('-> ' + c2):                    
        #        it[t] = it[t].replace(c2,c1)
        #print('swapping',c1,c2)
        itn = '\n'.join(it)

        
        itn = '\n'.join(it)
        txt = itn.split('\n\n')[1].split('\n')
        prog = []
        for i in txt:
            #print(i)
            prog.append(i.split())


        replacelist = {}
        #print('-------------------------------')
        for i in prog:
            if i[4].startswith('z') and len(i[4]) == 3:
                for opn in [0,2]:            
                    if not i[0].startswith('x') and not i[0].startswith('y'):
                        w1 = i[opn]
                        r1 = str(opn) + '-' + i[4]     
                        replacelist[r1] = w1
                        #print('replacement added',w1,r1,replacelist[r1],r1)               
                        for w in range(len(prog)):
                            for op in range(len(prog[w])):
                                if prog[w][op] == w1:                           
                                    prog[w][op] = r1
                                    

        #for i in prog:
            #print(i)
        #   print(' '.join(i))

        #print('-------------------------------')

        for i in prog:
            if i[0][2] == 'z':
                if len(i[4]) == 3 and 'z' not in i[4]:
                    w1 = i[4]
                    r1 = '3-' + i[0][2] + i[0][3] + i[0][4]
                    replacelist[r1] = w1
                    #print('replacement added',w1,r1,replacelist[r1],r1)                                                                 
                    for w in range(len(prog)):
                        for op in range(len(prog[w])):
                            if prog[w][op] == w1:                                               
                                prog[w][op] = r1

        #for i in prog:
            #print(i)
        # print(' '.join(i))


        #print('-------------------------------')

        for rd in [5,6,7,8]:
            for i in prog:
                if i[4][2] == 'z':
                    if len(i[0]) == 3 and i[0][0] not in 'xy' and 'z' not in i[0]:
                        w1 = i[0]
                        nrd = 0
                        r1 = str(nrd) + '-' + i[4][2] + i[4][3] + i[4][4]
                        while r1 in replacelist.keys():
                            nrd += 1
                            r1 = str(nrd) + '-' + i[4][2] + i[4][3] + i[4][4]                    
                        replacelist[r1] = w1
                        #print('replacement added',w1,r1,replacelist[r1],r1)    
                        for w in range(len(prog)):
                            for op in range(len(prog[w])):
                                if prog[w][op] == w1:                                                        
                                    prog[w][op] = r1

        #for i in prog:
            #print(i)
            #print(' '.join(i))

        #print('-------------------------------')

        for rd in [1,2,3,4]:
            for i in prog:
                if i[4][2] == 'z':
                    if len(i[2]) == 3 and i[2][0] not in 'xy' and 'z' not in i[2]:
                        w1 = i[2]
                        nrd = 0
                        r1 = str(nrd) + '-' + i[4][2] + i[4][3] + i[4][4]
                        while r1 in replacelist.keys():
                            nrd += 1
                            r1 = str(nrd) + '-' + i[4][2] + i[4][3] + i[4][4]                                        
                        replacelist[r1] = w1
                        #print('replacement added',w1,r1,replacelist[r1],r1)    
                        for w in range(len(prog)):
                            for op in range(len(prog[w])):
                                if prog[w][op] == w1:                                  
                                    prog[w][op] = r1

        #for i in prog:
            #print(i)
            #print(' '.join(i))


        #print('-------------------------------')
        strs = []
        for i in prog:
            #print(' '.join(i))
            strs.append(' '.join(i))

        #print('-------------------------------')

        #for i in prog:
            #print(i)
            #for j in [0,2,4]:
            # if len(i[j]) == 3 and i[j][0] not in 'xzy':
                    #print(i[j])   

        strs.sort()
        problems = []
        score = 0
        for sign in range(45):
            ors = ands = xors = 0
            ct = 0
            print('searching for',sign)
            signs = str(sign)
            if sign < 10:
                signs = '0' + signs    
            signs = 'z' + signs            
            for i in strs:
                if i.endswith(signs):
                    if i.split(' -> ')[1] in replacelist.keys():
                        print(i,'(' + replacelist[i.split('-> ')[1]]+ ')')
                    else:
                        print(i,'(' + i.split('-> ')[1] + ')')
                    ct += 1
                    if ' AND ' in i: ands += 1
                    if ' OR ' in i: ors += 1
                    if ' XOR ' in i: xors += 1

            if ct != 5:
                problems.append(sign)
            print('aox',ands,ors,xors,abs(ands-2), abs(ors-1), abs(xors-2))  
            score += abs(ands-2) + abs(ors-1) + abs(xors-2)  
            if (ands,ors,xors) != (2,1,2):                
                if sign not in problems:
                    problems.append(sign)
            print()
        aprobs.append([problems,score,c1,c2])
        print('swapping',c1,c2,problems,score)

for i in aprobs:
    if len(i[0]) < 9:
        print(i)




code = {}
for i in prog:
    code[i[4]] = [i[0],i[1],i[2]]
    
    
#print(code)


def getdetail(gate,gatenumber):
    if gate in code.keys():
        stf = code[gate][:]
        fr = []           
        for op in [0,1,2]:                        
            if stf[op][0] not in 'xy' and stf[op] not in ['AND','OR','XOR']:                    
                if gatenumber in stf[op]:
                    fr.append(getdetail(stf[op],gatenumber))                
                else:
                    fr.append(stf[op])
            else:                
                fr.append(stf[op])
        return fr   
    return gate



for bt in range(1,46):   
    gate = bt
    gs = str(gate) 
    i = 0
    if gate < 10:
        gs = '0' + gs
    if gate < 1:
        gs = '0' + gs       
    #print('gs',gs)     
    for n in range(len(prog)):
        #print(prog[n],prog[n][4],'z' + gs)
        if prog[n][4] == 'z' + gs:
            i = n
    gd = []           
    #print(gs,i)
    #print(prog[i])
    gd = getdetail(prog[i][4], gs)
    print(gate,gd)

print('answer',','.join(seq))
