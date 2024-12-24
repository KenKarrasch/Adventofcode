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

input_text = open('24-24.txt').read()

initial_values, gate_connections = parse_input(input_text)
final_wires = simulate_gates(initial_values, gate_connections)

prt = []
for k,v in final_wires.items():
    prt.append(k + ':' + str(v))
prt.sort()
num = 0
ml = 1
for i in prt:
    if i[0] == 'z':
        num += int(i.split(':')[1])*ml
        ml *= 2

print(num)
