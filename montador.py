import library.filehandling as fh
import os

opcodes_hexa = {
    'mov': [['bx', 'immed', 'bb', 5],
            ['ax', 'immed', 'b8', 5],
            ['di', 'immed', 'bf', 5],
            ['dx', 'immed', 'ba', 5],
            ['si', 'immed', '48be', 10],  # movabs
            ['al', 'immed', '8a0425', 7],  # al, byte[sinput]
            ['ah', 'immed', 'b4', 2]],
    'cmp': [['ah', 'al', '38c4', 2],
            ['bx', 'immed', '4883fb', 4]],
    'call': [[None, None, 'e889ffffff', 5]],  # JE 0x401000
    'syscall': [[None, None, '0f05', 2]],
    'ret': [[None, None, 'c3', 1]],
    'jne': [[None, None, '7525', 2]], # JnE 0x4020b0
    'je': [[None, None, '0f84', 6]], # TALVEZ ERRADO
    'jmp': [[None, None, 'e95b', 5]], # Talvez errado
}

je = ['7445', '0f8486000000', '0f84c7000000', '0f8408010000', '0f8443010000', '741d']
jmp = ['eb8e', 'e95b010000', 'e93b010000', 'e910010000', 'e9f0000000', 'e9c5000000', 'e9a5000000', 'eb7d', 'eb60', 'eb3d', 'eb00', 'e903feffff']
jne = ['7525', '7525', '7525', '7522']


# Função responsável por indetificar a instrução na tabela de opcodes.
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


# LENDO O ARQUIVO .asm
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

'''
print(f"TABELA DE CALCULO DE ILC\n{'RÓTULO':18}\t{'OPCODE':10}\t{'OPCODE HEX':17}{'COMPRIM.':8}\t{'ILC':3}\t{'OPERANDOS'}", "\t\t")
for i in instructions_table:
    print(f"{i[0]:18}\t{i[2]:10}\t{i[1]:17}{i[4]:7}\t{i[5]:3}\t{i[3]}", "\t\t")


print(f"\n\nTABELA DE SIMBOLOS\n{'SÍMBOLO':18}\t{'ILC'}")
for i in symbols_table:
    print(f"{i[0]:18}\t{i[1]}")
'''

# Montando tabela de EQU e DB
equ_dict = {}
db_table = []
ilc_data = []
ILC = 0
for i in range(len(section_data)):
    if type(section_data[i][1]) is type([]):
        dt = section_data[i][1]
        SIZE = 0

        for j in range(len(dt)):
            if dt[j] == '0xa':
                SIZE += 1
                ilc_data.append([ILC, '0xA'])
                ILC += 1
            else:
                for k in dt[j]:
                    SIZE += 1
                    ilc_data.append([ILC, k])
                    ILC += 1

        db_table.append([section_data[i][0], ILC - SIZE])
    else:
        equ_dict[section_data[i][0]] = [section_data[i][1], ILC]


# Escrevendo section .data e parte inicial no arquivo
with open("portao.out", 'w') as file:
    file.writelines(fh.return_object_initial())
    file.write('\n')
    str_print = "***************************************\n************ SECTION .DATA ************\n***************************************\n"

    if len(ilc_data) % 2:
        ilc_data.append([len(ilc_data), None])

    i = 0
    while i < len(ilc_data)-1:
        strwrite = ""
        for j in range(16):
            if j % 2 == 0:
                if ilc_data[i][1] == '0xA':
                    strwrite += "0a"
                else:
                    strwrite += f"{hex(ord(ilc_data[i][1]))[2:]}"
            else:
                if ilc_data[i][1] == '0xA':
                    strwrite += "0a "
                else:
                    if ilc_data[i][1] is None:
                        strwrite += "00 "
                    else:
                        strwrite += f"{hex(ord(ilc_data[i][1]))[2:]} "
            i += 1

        strwrite = strwrite.strip() + '\n'
        str_print += strwrite
        file.writelines(strwrite)

    print(str_print, '\n\n\n')


# Calculando as constantes que utilizam $ através do ILC
for i, j in equ_dict.items():
    if type(j[0]) is type(''):
        for k in range(len(db_table)):
            if db_table[k][0] == j[0]:
                equ_dict[i] = j[1] - db_table[k][1]
    else:
        equ_dict[i] = equ_dict[i][0]


# Tratando os operandos: Atribuindo valores das constantes.
for i in range(len(instructions_table)):
    new_operands = []
    for j in range(len(instructions_table[i][3])):
        if instructions_table[i][3][j].isnumeric():
            new_operands.append(f"{hex(int(instructions_table[i][3][j]))[2:]:0>2}")
        elif '0x' in instructions_table[i][3][j]:
            new_operands.append(f"{instructions_table[i][3][j][2:]:0>2}")
        else:
            for c, v in equ_dict.items():
                if instructions_table[i][3][j] == c:
                    h = hex(v)[2:]

                    if len(h) == 3:
                        new_operands.append(f"{h[1:]}{h[0]:0>2}")
                    elif len(h) == 4:
                        new_operands.append(f"{h[2:]}{h[:2]}")
                    else:
                        new_operands.append(f"{h:0>2}")

    code = instructions_table[i][1] + "".join(new_operands)
    while len(code) < instructions_table[i][4]*2:
        code += '0'

    instructions_table[i].append(code)


# Separando escrita em hexadecimal do instruction_table
list_write = []
for i in instructions_table:
    list_write.append(i[-1])


# Trocando número hexadecimal de opcodes da mesma função com hexa diferente.
for i in range(len(list_write)):
    if list_write[i] == '0f8400000000':
        list_write[i] = je.pop(0)
    elif list_write[i] == 'e95b000000':
        list_write[i] = jmp.pop(0)
    elif list_write[i] == '7525':
        list_write[i] = jne.pop(0)


# ESCREVENDO section .text e parte final no arquivo.
with open("portao.out", 'a') as file:
    str_print = "***************************************\n************ SECTION .TEXT ************\n***************************************\n"
    breakline = 0
    four = 0

    for i in list_write:
        for j in i:
            str_print += j
            file.write(j)

            four += 1

            if four == 4:
                four = 0
                breakline += 1
                if breakline < 8:
                    file.write(' ')
                    str_print += ' '

            if breakline == 8:
                breakline = 0
                file.write('\n')
                str_print += '\n'

    file.writelines(fh.return_object_finals())
    print(str_print)
    print("Arquivo portao.out gerado. (Arquivo Hexadecimal)")
    file.close()
    os.system("xxd -r -ps portao.out portao.o") # Este comando pega o hexadecimal que geramos e transforma em um arquivo com formatacao de objeto
    print("Arquivo portao.o gerado. (Arquivo Objeto)")








