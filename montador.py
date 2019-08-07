import library.filehandling as fh


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


with open("portao.asm", 'r') as file:
    ProcessFile = fh.FileHandling(file)
    section_data, section_bss, section_text = ProcessFile.file_handling()

for i in section_text:
    print(i)



