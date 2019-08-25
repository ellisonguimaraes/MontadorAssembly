import library.filehandling as fh

def get_ilc(instruction):
    if instruction[0] in ['call', 'syscall', 'ret', 'jne', 'jmp', 'je']:
        return opcodes_hexa[instruction[0]][0][2:]
    elif instruction[0] in ['cmp']:
        if instruction[1] == 'ah' and instruction[2] == 'al':
            return opcodes_hexa[instruction[0]][0][2:]
        elif 'bx' in instruction[1]:
            return opcodes_hexa[instruction[0]][1][2:]
    elif instruction[0] in ['mov']:
        movs = opcodes_hexa[instruction[0]]
        for i in movs:
            if i[0] in instruction[1]:
                return i[2:]

    return None


opcodes_hexa = {
    'mov': [['bx', 'immed', 'bb', 5],
            ['ax', 'immed', 'b8', 5],
            ['di', 'immed', 'bf', 5],
            ['dx', 'immed', 'ba', 5],
            ['si', 'immed', '47 be', 10],  # movabs
            ['al', 'immed', '8a 04 25', 7],  # al, byte[sinput]
            ['ah', 'immed', 'b4', 2]],

    'cmp': [['ah', 'al', '38 c4', 2],
            ['bx', 'immed', '48 83 fb', 4]],

    'call': [[None, None, 'e8 89 ff ff ff ff', 5]],  # JE 0x401000
    'syscall': [[None, None, '0f 05', 2]],
    'ret': [[None, None, 'c3', 1]],
    'jne': [[None, None, '75 25', 2]], # JnE 0x4020b0

    # ['je', 'None', 'None', '74 45', 2], # JE 0x4010C9
    # ['je', 'None', 'None', '0f 84 86', 6], # JE 0x401114
    # ['je', 'None', 'None', '0f 84 c7', 6], # JE 0x40115f
    # ['je', 'None', 'None', '0f 84 08 01', 6], # JE 0x4011aa
    # ['je', 'None', 'None', '0f 84 43 01', 6], # JE 0x4011ef
    'je': [[None, None, '0f 84', 6]], #TALVEZ ERRADO

    # ['jmp', 'None', 'None', 'eb 8e', 2], # JE 0x401057
    # ['jmp', 'None', 'None', 'e9 5b 01', 5], # JE 0x40124f
    # ['jmp', 'None', 'None', 'e9 03 fe ff ff', 5], # JE 0x401057
    'jmp': [[None, None, 'e9 5b', 5]], #Talvez errado
}


# lendo arquivo
with open("portao.asm", 'r') as file:
    ProcessFile = fh.FileHandling(file)
    section_data, section_bss, section_text = ProcessFile.file_handling()


# TRATANDO MACRO
macro = section_text[1:6]
section_text = section_text[7:]

i = 0
size = len(section_text)
while i < size:
    if section_text[i][0] == 'print':
        l1 = macro[2][0:2] + [section_text[i][1]]
        l2 = macro[3][0:2] + [section_text[i][2]]

        section_text[i] = macro[0]
        section_text.insert(i+1, macro[1])
        section_text.insert(i+2, l1)
        section_text.insert(i+3, l2)
        section_text.insert(i+4, macro[4])

        size += 4

    i += 1


# REMOVENDO GLOBAL
section_text.remove(['global', '_start'])


# PASS 1
instructions_table = []
symbols_table = []
i = 0
ILC = 0

while i < len(section_text):
    if ':' in section_text[i][0]:
        LABEL = section_text.pop(i)[0]
        symbols_table.append([LABEL, ILC])

    OPCODE, SIZE = get_ilc(section_text[i])
    instructions_table.append([LABEL, OPCODE, section_text[i][0], section_text[i][1:], SIZE, ILC])
    ILC = ILC + SIZE
    i += 1


print(f"TABELA DE OPCODE\n{'RÓTULO':18}\t{'OPCODE':10}\t{'OPCODE HEX':17}{'COMPRIM.':8}\t{'ILC':3}\t{'OPERANDOS'}", "\t\t")
for i in instructions_table:
    print(f"{i[0]:18}\t{i[2]:10}\t{i[1]:17}{i[4]:7}\t{i[5]:3}\t{i[3]}", "\t\t")


print(f"\n\nTABELA DE SIMBOLOS\n{'SÍMBOLO':18}\t{'ILC'}")
for i in symbols_table:
    print(f"{i[0]:18}\t{i[1]}")





