from funcoes.formatacao import lin
import funcoes.autodefs_ongs as autodefs_ongs
import funcoes.autodefs_empresas as autodefs_empresas

def get_ongs():
    lin()
    print('Bem vindo à area para ONGs!')
    lin()
    
    
    loop = True
    while loop:
        
        choice = input('Digite (1) se deseja se cadastrar.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        choice_list = ['1', '2', '3']
        
        if choice not in choice_list:
            print('\nOpção inválida! Tente novamente\n')
            
        elif choice in choice_list[2]:
            autodefs_empresas.go_to_menu()
            
        #CONTINUAR A OPCAO DE CADASTRO    
        elif choice == choice_list[0]:
            autodefs_ongs.make_register_ongs()
        
        #CONTINUAR A OPCAO DE LOGIN
        elif choice == choice_list[1]:
            validation_json_ongs = autodefs_ongs.loadjson_ongs
            autodefs_ongs.make_login_ongs(validation_json_ongs)