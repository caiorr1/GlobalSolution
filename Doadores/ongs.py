import formatacao
import main
import json
import funcoes.autodefs_ongs as autodefs_ongs
import funcoes.autodefs_empresas as functionmenu

def get_ongs():
    formatacao.formatting()
    print('Bem vindo à area para ONGs!')
    formatacao.formatting()
    
    
    loop = True
    while loop:
        
        choice = input('Digite (1) se deseja se cadastrar.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        choice_list = ['1', '2', '3']
        
        if choice not in choice_list:
            print('\nOpção inválida! Tente novamente\n')
            
        elif choice in choice_list[2]:
            functionmenu.go_to_menu()
            
        #CONTINUAR A OPCAO DE CADASTRO    
        elif choice == choice_list[0]:
            autodefs_ongs.make_register_ongs()
        #CONTINUAR A OPCAO DE LOGIN
        elif choice == choice_list[1]:
            print('CONTINUA')  