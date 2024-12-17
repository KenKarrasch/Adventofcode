f = open('24-17.txt').read().split('\n\n')

program = [int(i) for i in f[1].split(':')[1].split(',')]
a = int(f[0].split('\n')[0].split(':')[1])
b = int(f[0].split('\n')[1].split(':')[1])
c = int(f[0].split('\n')[2].split(':')[1])

#print(program,a,b,c)

class Computer:
    def __init__(self, program, a, b, c):
        self.program = program
        self.registers = {'A': a, 'B': b, 'C': c}
        self.ip = 0
        self.output = []

    def run(self):
        while self.ip < len(self.program):
        #for i in range(5):
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            print('a',self.registers['A'],'b',self.registers['B'],'c',self.registers['C'])
            self.execute(opcode, operand)
            print('self.ip',self.ip)
            if opcode != 3 or self.registers['A'] == 0:
                self.ip += 2
                print('self.ip',self.ip)
        print('Exiting: a',self.registers['A'],'b',self.registers['B'],'c',self.registers['C'])

    def execute(self, opcode, operand):
        print('opcode',opcode, 'operand',operand)
        if opcode == 0:   # adv
            self.registers['A'] //= 2 ** self.get_combo_value(operand)
        elif opcode == 1: # bxl
            self.registers['B'] ^= operand
        elif opcode == 2: # bst
            print('value',self.get_combo_value(operand))
            self.registers['B'] = self.get_combo_value(operand) % 8
            print('B',self.registers['B'])
        elif opcode == 3: # jnz
            if self.registers['A'] != 0:
                print('self.ip/operand',self.ip, operand)
                self.ip = operand 
                print('self.ip',self.ip)
        elif opcode == 4: # bxc
            self.registers['B'] ^= self.registers['C']
        elif opcode == 5: # out
            self.output.append(str(self.get_combo_value(operand) % 8))
            print(self.output)
        elif opcode == 6: # bdv
            self.registers['B'] = self.registers['A'] // 2 ** self.get_combo_value(operand)
        elif opcode == 7: # cdv
            self.registers['C'] = self.registers['A'] // 2 ** self.get_combo_value(operand)

    def get_combo_value(self, operand):
        if operand < 4:
            return operand
        elif operand == 4:
            return self.registers['A']
        elif operand == 5:
            return self.registers['B']
        elif operand == 6:
            return self.registers['C']
        else:
            raise ValueError("Invalid combo operand")

computer = Computer(program,a,b,c)
computer.run()
print(','.join(computer.output))
