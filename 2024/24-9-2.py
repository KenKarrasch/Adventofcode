# nice fun one, not as efficient as it could be

input_sequence = open('24-9.txt').read()
#input_sequence = '2333133121414131402'

print(input_sequence)

def generate_sequence(input_string):
    result = []
    for i, num in enumerate(input_string):
        count = int(num)
        if i % 2 == 0:
            for j in range(count):
                result.append(str(i // 2))
        else:
            for j in range(count):
                result.append('.')   
    return result
 
output = generate_sequence(input_sequence)
 
def analyze_number_sequence(sequence):
    result = []
    current_num = None
    start_index = 0
    count = 0 
    for i, char in enumerate(sequence):
        if char.isdigit():
            num = int(char)
            if num != current_num:
                if current_num is not None:
                    result.append((current_num, start_index, count))
                current_num = num
                start_index = i
                count = 1
            else:
                count += 1
        elif char == '.' and current_num is not None:
            result.append((current_num, start_index, count))
            current_num = None 
    if current_num is not None:
        result.append((current_num, start_index, count)) 
    return result
 
def analyze_dot_sequence(sequence):
    result = []
    current_char = None
    start_index = 0
    count = 0 
    for i, char in enumerate(sequence):
        if char != current_char:
            if current_char is not None:
                if not current_char.isdigit():
                    result.append(('.', start_index, count))
            current_char = char
            start_index = i
            count = 1
        else:
            count += 1 
    # Add the last run
    if current_char is not None:
        if not current_char.isdigit():
            result.append(('.', start_index, count)) 
    return result
 
def insertbit(da,n,al):
    nda = []
    for i in da[0:n]:
        nda.append((i[0],i[1],i[2]))    
    nda.append((al[0],al[1],al[2]))
    for i in da[n:]:
        nda.append((i[0],i[1],i[2]))
    return nda
 
 
def rearrange_sequence(sequence):    
    
    # get a list of fileIDs (FILEID, position, run)
    na = analyze_number_sequence(sequence)
    na.reverse()       
    # get a list of dots (dot, position, run)
    da = analyze_dot_sequence(sequence)       
    for i in range(len(na)):
        dn = False
        for j in range(len(da)):
            if not dn:
                if da[j][0] == '.':
                    if na[i][1] > da[j][1]:                
                        szd = na[i][2] - da[j][2]
                        if szd == 0: # hole is the same size as the FileID, delete hole, insert FILEid
                            da[j] = (na[i][0],da[j][1],na[i][2])
                            dn = True
                            na[i] = (-1,-1,-1)                        
                        if szd < 0:     # hole is bigger than as the FileID, hole = FILEiD + smaller hole
                            da = insertbit(da,j,na[i])
                            da[j] = (da[j][0],da[j+1][1],da[j][2])
                            da[j+1] = (da[j+1][0],da[j+1][1]+da[j][2],da[j+1][2]-+da[j][2])
                            dn = True
                            na[i] = (-1,-1,-1)

        print(i,len(na))
    
    chksum = 0

    for i in da:  # holes list with inserted FILEId's, count FILEids only
        if i[0] != '.':
            for k in range(i[2]):
                chksum += i[0] * (i[1]+k)
    for i in na:  # FILEid's that did not have a new home 
        if i[0] != -1:
            for k in range(i[2]):
                chksum += i[0] * (i[1]+k)
    
    print('part 2 -',chksum)                   
rearrange_sequence(output)
