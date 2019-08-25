
class FileHandling:
    def __init__(self, file):
        self.file = file

    def del_comm_wl_tab(self, i):        
        i = i.strip('\t') # Tirando tabulações
        i = i.strip('\n') # Tirando quebra de linha
        # Tirando comentários
        if(';' in i):
            i = i[:i.find(';')]

        return i

    def file_handling(self):
        FileList = []
        section_data = []
        section_bss = []
        section_text = []

        #TRATANDO AS LINHAS: Retirando comentários, linhas em branco e tabulações e quebra de linha
        for i in self.file:
            i = self.del_comm_wl_tab(i)
            if(i):
                FileList.append(i)

        #SEPARANDO SESSÕES EM LISTAS DIFERENTES
        SectionIndexes = sorted(((FileList.index("section .bss"), "section .bss"), 
                                (FileList.index("section .data"), "section .data"),
                                (FileList.index("section .text"), "section .text")))

        for i in range(len(SectionIndexes)):
            l = FileList[SectionIndexes[i][0]+1 : SectionIndexes[i+1][0] if i < len(SectionIndexes)-1 else len(FileList)]
            if(SectionIndexes[i][1] == "section .data"):
                section_data = l
            elif(SectionIndexes[i][1] == "section .bss"):
                section_bss = l
            else:
                section_text = l

        return section_data, section_bss, self.handling_text(section_text)

    def handling_text(self, section_text):
        #PERCORRENDO A SESSÃO DE TEXT E SEPARANDO OPERANDOS NA LISTA DE INSTRUÇÕES
        for i in range(len(section_text)):
            section_text[i] = list(section_text[i].replace('\t', '*').replace(',', '*').replace(' ', '*').split('*'))

            while '' in section_text[i]:
                section_text[i].remove('')

        return section_text