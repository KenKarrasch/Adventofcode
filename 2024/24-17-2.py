f = open('24-17.txt').read().split('\n\n')

# Hardcoded version

program = [int(i) for i in f[1].split(':')[1].split(',')]

def process_values(A,B,C):    
    B = A % 8        
    B = B ^ 3        
    C = A // (2 ** B)        
    A = A // 8        
    B = B ^ C        
    B = B ^ 5
    return (B%8)    

possibleanswers = []

def search(program, tc, bestsofar):
    if len(tc) == 0:  # no more digits to search for, previous trial must have been correct        
        possibleanswers.append(bestsofar//8)  # add it to possible candidates. Remove the last octet as not requried 
        # Probably don't need to search any further as the smallest candidate is the first to be found. Doing it for interest only.
        return -1
    for tr in range(8):  # look at the best number so far, try changing the last octet to 0,1,2,3,4,5,6, or 7
        trial = (bestsofar & ~0x7) + tr        
        o = process_values(trial,0,0) # only need the first output number
        if o != tc[-1]:  
            continue # this octet trial did not appear to work, move onto the next trial
        # we made it this far, so trial appears to match the program so far, lets look at the next digit (recurse)
        sch = search(program,tc[:-1],trial*8)  # trial * 8, effectively shifts the trial over one octet
        if sch > -1: 
            return sch # Found a valid number so pass back the good news.
    return -1  # this trial appears to never have found a way forward, nevermind, go back previous octet trial

search(program,program,0)
print('possible',len(possibleanswers),'possible answers')
for i in possibleanswers:
    print(i)
print('best',min(possibleanswers))
 
