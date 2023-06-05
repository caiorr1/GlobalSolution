from funcoes.formatacao import lin, title
import main
import funcoes.autodefs_pessoafisica as autodefs_pessoafisica

def pessoasnaturais():
    title(title1='Bem vindo à area de Pessoa Fisíca!')
    
    loopvalidando = True
    while loopvalidando:
        
        escolha_menu = input('Digite (1) se deseja se cadastrar.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        lista_escolha_menu = ['1', '2', '3']
        
        if escolha_menu not in lista_escolha_menu:
            print('\nOpção inválida! Tente novamente\n')
            
        elif escolha_menu in lista_escolha_menu[2]:
            print('\nOk...Voltando para o menu principal\n')
            lin()
            print('- Bem vindo ao SeedS, aquecendo corações! -')
            lin()
            main.menu_principal()
           
        elif escolha_menu == lista_escolha_menu[0]:
            autodefs_pessoafisica.registrar_pessoafisica()
       
        
        elif escolha_menu == lista_escolha_menu[1]:
            json_validado_pessoasfisicas = autodefs_pessoafisica.carregarjson_pessoasfisicas()
            autodefs_pessoafisica.login_pessoafisica(json_validado_pessoasfisicas)