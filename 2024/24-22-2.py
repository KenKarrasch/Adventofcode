f = [int(i) for i in open('24-22.txt').read().split('\n')]

ns = f
sequences = {}
lseq = {}

def addseq(sq,nums):
    for i in range(len(nums)-4):
        seq = (sq[i],sq[i+1],sq[i+2],sq[i+3])
        if seq not in lseq:            
            lseq[seq] = nums[i+3]        

for n,nm in enumerate(ns):
    sn = nm
    ld = sn%10
    seq = []
    num = []
    print(n,nm)
    lseq = {}
    for i in range(2000):    
        sn = ((sn * 64)^sn)%16777216
        sn = ((sn//32)^sn)%16777216
        sn = ((sn*2048)^sn)%16777216    
        diff = (sn%10)-ld    
        ld = sn%10     
        num.append(ld)   
        seq.append(diff)
    addseq(seq,num)    
    for key,value in lseq.items():
        if key not in sequences:
            sequences[key] = value
        else:
            sequences[key] += value    
print(max(sequences.values()))
