from funcoes.formatacao import title
import funcoes.autodefs_empresas as autodefs_empresas

def empresas():
    title(title1='Bem vindo à area para Empresas!')
    
    loop = True
    while loop:
        
        escolha_menu = input('Digite (1) se deseja fazer cadastro.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        lista_escolha_menu = ['1', '2', '3']
        
        if escolha_menu not in lista_escolha_menu:
            print('\nOpção inválida! Tente novamente\n')
        
        
        elif escolha_menu in lista_escolha_menu[2]:
            autodefs_empresas.go_to_menu()
        
           
        elif escolha_menu == lista_escolha_menu[0]:
            autodefs_empresas.registrar_empresas()
                    
        
        elif escolha_menu == lista_escolha_menu[1]:
            json_validado = autodefs_empresas.carregar_json()
            autodefs_empresas.fazer_login(json_validado)
            
                            
                    