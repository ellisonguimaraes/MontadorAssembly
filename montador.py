
class Label:
    def __init__(self, ILC, Name):
        self.ILC = ILC
        self.Name = Name

class Instruction:
    def __init__(self, opcode, op1, op2, ILC, len):
        self.opcode = opcode
        self.op1 = op1
        self.op2 = op2
        self.ILC = ILC
        self.len = len



Labels = []
Instructions = []

file = open("portao.asm", 'r')

for i in file:
    # Tirando tabulações
    i = i.strip('\t')


    if(i[0] != ';' and not(i.isspace())):
        print(i, end="")



file.close()


