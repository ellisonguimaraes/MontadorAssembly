
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


def DeleteCommWhileLines(i):
    # Tirando tabulações
    i = i.strip('\t')
    i = i.strip('\n')
    #Tirando comentários
    if(';' in i):
        i = i[:i.find(';')]
    #Tirando linhas em branco
    if(i):
        return i

    return None


Labels = []
Instructions = []

file = open("portao.asm", 'r')


for i in file:
    i = DeleteCommWhileLines(i)

    if(i):
        if("section .bss" in i):
            print(i)






file.close()


