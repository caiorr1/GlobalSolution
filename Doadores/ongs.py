from funcoes.formatacao import lin, title
import funcoes.autodefs_ongs as autodefs_ongs
import funcoes.autodefs_empresas as autodefs_empresas

def ongs():
    title(title1='Bem vindo à area para ONGs!')
    
    
    loop = True
    while loop:
        
        escolha_menu = input('Digite (1) se deseja se cadastrar.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        lista_escolha_menu = ['1', '2', '3']
        
        if escolha_menu not in lista_escolha_menu:
            print('\nOpção inválida! Tente novamente\n')
            
        elif escolha_menu in lista_escolha_menu[2]:
            autodefs_empresas.go_to_menu()
            
           
        elif escolha_menu == lista_escolha_menu[0]:
            autodefs_ongs.registrar_ongs()
        
        
        elif escolha_menu == lista_escolha_menu[1]:
            json_validado_ongs = autodefs_ongs.carregarjson_ongs()
            autodefs_ongs.login_ongs(json_validado_ongs)