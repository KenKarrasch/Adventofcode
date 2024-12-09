
# Online Python - IDE, Editor, Compiler, Interpreter
input_sequence = open('24-9.txt').read()

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


def rearrange_sequence(sequence):
    # Separate numbers and dots
    numbers = [char for char in sequence if char.isdigit()]
    dots = [i for i, char in enumerate(sequence) if char == '.']
    
    # Reverse the numbers to start from the end
    numbers.reverse()
    
    # Create a list of the sequence
    result = list(sequence)
    ct = 0
    
    # Replace dots with numbers
    for i, dot_index in enumerate(dots):
        if i < len(numbers):
                result[dot_index] = numbers[i]
                ct += 1
        else:
            break
    
    return result, ct  #''.join(result),ct

new_sequence,ct = rearrange_sequence(output)

nns = []
for i in new_sequence[0:-ct]:
    nns.append(i)
chksm = 0
for i in range(len(nns)):
    chksm += i*int(nns[i])
print(chksm)

