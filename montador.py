import library.filehandling as fh


with open("portao.asm", 'r') as file:
    ProcessFile = fh.FileHandling(file)
    section_data, section_bss, section_text = ProcessFile.file_handling()

for i in section_text:
    print(i)



