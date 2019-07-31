
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

    return i



section_data = []
section_bss = []
section_text = []
FileList = []


file = open("portao.asm", 'r')


#TRATANDO AS LINHAS: Retirando comentários, linhas em branco e tabulações e quebra de linha
for i in file:
    i = DeleteCommWhileLines(i)
    if(i):
        FileList.append(i)


#SEPARANDO SESSÕES EM LISTAS DIFERENTES
SectionIndexes = sorted(((FileList.index("section .bss"), "section .bss"),
     (FileList.index("section .data"), "section .data"),
     (FileList.index("section .text"), "section .text")))

for i in range(len(SectionIndexes)):
    l = FileList[SectionIndexes[i][0] : SectionIndexes[i+1][0] if i < len(SectionIndexes)-1 else len(FileList)]
    if(SectionIndexes[i][1] == "section .data"):
        section_data = l
    elif(SectionIndexes[i][1] == "section .bss"):
        section_bss = l
    else:
        section_text = l






#SectionData = FileList[FileList.index("section .data"): FileList.index("section .bss")]
#SectionBss = FileList[FileList.index("section .bss"): FileList.index("section .text")]
#SectionText = FileList[FileList.index("section .text"):]



file.close()


