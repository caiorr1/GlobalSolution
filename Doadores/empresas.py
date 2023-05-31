import formatacao
import autodefs
import os

def get_companies():
    formatacao.formatting()
    print('Bem vindo à area para Empresas!')
    formatacao.formatting()
    
    loop = True
    while loop:
        
        choice = input('Digite (1) se deseja fazer cadastro.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        choice_list = ['1', '2', '3']
        
        if choice not in choice_list:
            print('\nOpção inválida! Tente novamente\n')
        
        #condicion makes user go to menu
        elif choice in choice_list[2]:
            autodefs.go_to_menu()
        
        #condicion makes user register    
        elif choice == choice_list[0]:
            autodefs.make_register_empresas()
                    
        #CONTINUAR A OPCAO DE LOGIN
        elif choice == choice_list[1]:
            validation_json = autodefs.loadjson_empresas()
            nome_empresa = 'nome_empresa'
            endereco_empresa = 'endereco_empresa'
            alimentos_doados = 'alimentos_doados'
            autodefs.make_login_empresas(validation_json, nome_empresa, endereco_empresa, alimentos_doados)
            
                            
                    