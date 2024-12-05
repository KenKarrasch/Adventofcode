
# Online Python - IDE, Editor, Compiler, Interpreter
import functools
g = open('24-5.txt').read()

pu = []

pn = []


for i in g.split('\n\n')[0].split('\n'):
        print(i)
        pu.append(i)

for i in g.split('\n\n')[1].split('\n'):
    for b in i.split('\n'):
        pn.append([j for j in i.split(',')])


#print(pu)
print(pn,len(pn))

strs = []

for y in pu:
    i = y.split('|')
    for j in [0,1]:
        if i[j] not in strs:
            strs.append(i[j])

print(strs)
def check_order(string_book, rules):
    for rule in rules:
        string1, string2 = rule.split('|')
        if string1 in string_book and string2 in string_book:
            if string_book.index(string1) > string_book.index(string2):
                return False
    return True

# Example usage
string_book = ['apple', 'banana', 'cherry', 'date']
rules = ['apple|cherry', 'banana|date']
ct = 0
for i in pn:
    #result = check_order(string_book, rules)
    result = check_order(i, pu)
    print(result,i)
    if(result):
        ct += int(i[len(i)//2])
print('part 1 -',ct)



