
section .data

	;;; CONSTANTES_INICIO

	EXIT_SUCCESS equ 0 ; successful operation
	SYS_EXIT equ 60 ; call code for terminate

	STDOUT equ 1 ; standard output
	SYS_WRITE equ 1 ; call code for write
	STDIN equ 0 ; standard input
	SYS_READ equ 0 ; call code for read

	;;; CONSTANTES_FIM

	;;; MENSAGENS_INICIO

	; String do menu
	string_menu:	db "####### Menu #######", 0xa
	string_menu1:	db "##  1) Abrir      ##", 0xa
	string_menu2:	db "##  2) Fechar     ##", 0xa
	string_menu3:	db "##  3) fcf        ##", 0xa
	string_menu4:	db "##  4) fca        ##", 0xa
	string_menu5:	db "##  5) Emergencia ##", 0xa
	string_menu6:	db "##----------------##", 0xa
	string_menu_len equ $ - string_menu

	string_digite: db "Digite: "
	string_digite_len equ $ - string_digite

	; String do default do switch case
	error: db "Comando inexistente.", 0xa
	error_len equ $ - error



	abrindo:	db '----------------------            ---------------------', 0xa
	abrindo2:	db '     /     /    /   /|           /     /     /    /   /', 0xa
	abrindo3:	db '--------------------/|            -------------------  ', 0xa
	abrindo4:	db '    |     |     |  | |     -------------------    |  | ', 0xa
	abrindo5:	db '--------------------/|     |                 |-------  ', 0xa
	abrindo6:	db '      |      |     | |     |                 | |   |   ', 0xa
	abrindo7:	db '--------------------/|  x| |                 |-------  ', 0xa
	abrindo8:	db '    |     |     |  | |     |                 |   |   | ', 0xa
	abrindo9:	db '--------------------/      |                 |-------  ', 0xa
	abrindo10:	db '               fcf /       |0----()----()----|  fca    ', 0xa
	abrindo11:	db '                  /            /                       ', 0xa
	abrindo12:	db '                 /    --->    /                        ', 0xa
	abrindo13:	db '                /            /                         ', 0xa
	abrindo14:	db '               /            /                          ', 0xa
	abrindo15:	db '              /            /                           ', 0xa
	abrindo16:	db '             /            /                            ', 0xa
	abrindo17:	db '   / \                                                 ', 0xa
	abrindo18:	db '  /   \                                                ', 0xa
	abrindo19:	db '    |                                                  ', 0xa
	abrindo20:	db '    |                                                  ', 0xa
	abrindo21:	db '  |---|                                                ', 0xa
	abrindo22:	db '  | 0 | ba                                             ', 0xa
	abrindo23:	db '  | 0 | bf                                             ', 0xa
	abrindo24:	db '  |---|                                                ', 0xa
	abrindo_len equ $ - abrindo

	fechando:	db '----------------------            ---------------------', 0xa
	fechando2:	db '     /     /    /   /|           /     /     /    /   /', 0xa
	fechando3:	db '--------------------/|            -------------------  ', 0xa
	fechando4:	db '    |     |     |  | |     -------------------    |  | ', 0xa
	fechando5:	db '--------------------/|     |                 |-------  ', 0xa
	fechando6:	db '      |      |     | |     |                 | |   |   ', 0xa
	fechando7:	db '--------------------/|  x| |                 |-------  ', 0xa
	fechando8:	db '    |     |     |  | |     |                 |   |   | ', 0xa
	fechando9:	db '--------------------/      |                 |-------  ', 0xa
	fechando10:	db '               fcf /       |0----()----()----|  fca    ', 0xa
	fechando11:	db '                  /            /                       ', 0xa
	fechando12:	db '                 /    <---    /                        ', 0xa
	fechando13:	db '                /            /                         ', 0xa
	fechando14:	db '               /            /                          ', 0xa
	fechando15:	db '              /            /                           ', 0xa
	fechando16:	db '             /            /                            ', 0xa
	fechando17:	db '   / \                                                 ', 0xa
	fechando18:	db '  /   \                                                ', 0xa
	fechando19:	db '    |                                                  ', 0xa
	fechando20:	db '    |                                                  ', 0xa
	fechando21:	db '  |---|                                                ', 0xa
	fechando22:	db '  | 0 | ba                                             ', 0xa
	fechando23:	db '  | 0 | bf                                             ', 0xa
	fechando24:	db '  |---|                                                ', 0xa
	fechando_len equ $ - fechando

	fechado:	db '---------------------            -------------------------', 0xa
	fechado2:	db '    /     /    /   /|           /     /      /      /    /', 0xa
	fechado3:	db '-------------------/|            ----------------------   ', 0xa
	fechado4:	db '   |    |     |    |--------------------|    |    |    |  ', 0xa
	fechado5:	db '-------------------|                    |--------------   ', 0xa
	fechado6:	db '     |     |     | |                    |     |    |      ', 0xa
	fechado7:	db '-----------------x||                    |--------------   ', 0xa
	fechado8:	db '   |    |     |    |                    |    |    |    |  ', 0xa
	fechado9:	db '-------------------|                    |--------------   ', 0xa
	fechado10:	db '             fcf  /|0-----()-----()-----| fca             ', 0xa
	fechado11:	db '                 /            /                           ', 0xa
	fechado12:	db '                /            /                            ', 0xa
	fechado13:	db '               /            /                             ', 0xa
	fechado14:	db '              /            /                              ', 0xa
	fechado15:	db '             /            /                               ', 0xa
	fechado16:	db '            /            /                                ', 0xa
	fechado17:	db '    / \                                                   ', 0xa
	fechado18:	db '   /   \                                                  ', 0xa
	fechado19:	db '     |                                                    ', 0xa
	fechado20:	db '     |                                                    ', 0xa
	fechado21:	db '   |---|                                                  ', 0xa
	fechado22:	db '   | 0 | ba                                               ', 0xa
	fechado23:	db '   | 0 | bf                                               ', 0xa
	fechado24:	db '   |---|                                                  ', 0xa
	fechado_len equ $ - fechado

	aberto:		db '----------------------            ---------------------', 0xa
	aberto2:	db '     /     /    /   /|           /     /     /    /   /', 0xa
	aberto3:	db '--------------------/|            -------------------  ', 0xa
	aberto4:	db '    |     |     |  | |            ------------------- |', 0xa
	aberto5:	db '--------------------/|            |                 |-|', 0xa
	aberto6:	db '      |      |     | |            |                 | |', 0xa
	aberto7:	db '--------------------/|         x| |                 |-|', 0xa
	aberto8:	db '    |     |     |  | |            |                 | |', 0xa
	aberto9:	db '--------------------/             |                 |-|', 0xa
	aberto10:	db '               fcf /              |0----()----()----| |', 0xa
	aberto11:	db '                  /            /                       ', 0xa
	aberto12:	db '                 /            /                        ', 0xa
	aberto13:	db '                /            /                         ', 0xa
	aberto14:	db '               /            /                          ', 0xa
	aberto15:	db '              /            /                           ', 0xa
	aberto16:	db '             /            /                            ', 0xa
	aberto17:	db '   / \                                                 ', 0xa
	aberto18:	db '  /   \                                                ', 0xa
	aberto19:	db '    |                                                  ', 0xa
	aberto20:	db '    |                                                  ', 0xa
	aberto21:	db '  |---|                                                ', 0xa
	aberto22:	db '  | 0 | ba                                             ', 0xa
	aberto23:	db '  | 0 | bf                                             ', 0xa
	aberto24:	db '  |---|                                                ', 0xa
	aberto_len equ $ - aberto

	emergencia:		db "########### EMERGENCIA!!! ###########", 0xa
	emergencia2:	db "### (luzinhas vermelhas girando) ###", 0xa
	emergencia3:	db "### (iuiuiuiuiuiuiuiuiuiuiuiuiu) ###", 0xa
	emergencia4:		db "#####################################", 0xa
	emergencia_len equ $ - emergencia


	portaoNaoFechado: db "Portao nao esta fechado. fcf nao ativado!", 0xa
	portaoNaoFechado_len equ $ - portaoNaoFechado

	portaoNaoAberto: db "Portao nao esta fechado. fca nao ativado!", 0xa
	portaoNaoAberto_len equ $ - portaoNaoAberto

	portaoNaoAbrindo: db "Portao nao esta abrindo!", 0xa
	portaoNaoAbrindo_len equ $ - portaoNaoAbrindo

	portaoNaoFechando: db "Portao nao esta fechaNdo!", 0xa
	portaoNaoFechando_len equ $ - portaoNaoFechando

	error_emer: db "O sensor de emergencia so pode ser ativado quando o portao esta fechando!", 0xa
	error_emer_len equ $ - error_emer

	;;; MENSAGENS_FIM


; buffer dos valores entrada
section .bss
	sinput:     resb    1


section .text

	; Funcao print
	%macro print 2
		mov		rax, SYS_WRITE
		mov		rdi, STDOUT
		mov		rsi, %1
		mov		rdx, %2
		syscall
	%endmacro

	; Funcao scan
	scan:
		print string_digite, string_digite_len
		mov		rax, SYS_READ
		mov		rdi, STDIN
		mov		rsi, sinput
		mov		rdx, 2
		syscall
		ret


global _start
_start:

	mov		rbx, 0	; 0=fechado, 1=abrindo, 2=aberto, 3=fechando, 4=indefinido
	print	fechado, fechado_len

	; Label para voltar ao menu
	menu:

	print	string_menu, string_menu_len ; chamada da funcao print	
	
	call	scan ; chamada da funcao scan

	mov		al, byte[sinput]	; setando 1 byte do buffer de entrada no registrador para ser comparado
	
	mov		ah, 0x31 			; setando valor para ser comparado
	cmp		ah, al				; fazendo a comparacao
	je		case_1_abrir		; pulando para a label caso a comparacao seja verdadeira

	mov		ah, 0x32
	cmp		ah, al
	je		case_2_fechar

	mov		ah, 0x33
	cmp		ah, al
	je		case_3_fcf

	mov		ah, 0x34
	cmp		ah, al
	je		case_4_fca

	mov		ah, 0x35
	cmp		ah, al
	je		case_5_emergencia


	print error, error_len
	jmp		menu

	case_1_abrir:
		cmp		rbx, 0 ;;
		jne		interrupcao1 ;;
		mov		rbx, 1 ;;
		print	abrindo, abrindo_len
		jmp		break
		interrupcao1: ;;
			print	portaoNaoFechado, portaoNaoFechado_len;;
			jmp		break ;;

	case_2_fechar:
		cmp		rbx, 2 ;;
		jne		interrupcao3 ;;
		mov		rbx, 3 ;;
		print	fechando, fechando_len
		jmp		break
			interrupcao3: ;;
			print	portaoNaoAberto, portaoNaoAberto_len;;
			jmp		break ;;

	case_3_fcf:
		cmp		rbx, 3 ;;
		jne		interrupcao4 ;;
		mov		rbx, 0 ;;
		print	fechado, fechado_len
		jmp		break
			interrupcao4: ;;
			print	portaoNaoFechando, portaoNaoFechando_len;;
			jmp		break ;;

	case_4_fca:
		cmp		rbx, 1 ;;
		jne		interrupcao2 ;;
		mov		rbx, 2 ;;
		print	aberto, aberto_len
		jmp		break
			interrupcao2: ;;
			print	portaoNaoAbrindo, portaoNaoAbrindo_len;;
			jmp		break ;;

	case_5_emergencia:
		cmp		rbx, 3
		je		emer
		print	error_emer, error_emer_len
		jmp		break
		emer:
			mov		rbx, 1 ;;
			print	emergencia, emergencia_len
			print	abrindo, abrindo_len
			jmp		break
	

	break:
		jmp		menu ; volta para a label menu, fazendo assim um loop


	last:
		mov 	rax, SYS_EXIT ; Call code for exit
		mov		rdi, EXIT_SUCCESS ; Exit program with success
		syscall
