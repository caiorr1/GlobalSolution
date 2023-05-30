import formatacao
import main
import json

def get_natural_person():
    formatacao.formatting()
    print('Bem vindo à area de Pessoa Fisíca!')
    formatacao.formatting()
    
    loop = True
    while loop:
        
        choice = input('Digite (1) se deseja se cadastrar.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        choice_list = ['1', '2', '3']
        
        if choice not in choice_list:
            print('\nOpção inválida! Tente novamente\n')
            
        elif choice in choice_list[2]:
            print('\nOk...Voltando para o menu principal\n')
            formatacao.formatting()
            print('- Bem vindo ao SeedS, aquecendo corações! -')
            formatacao.formatting()
            main.main_menu()
        #CONTINUAR A OPCAO DE CADASTRO    
        elif choice == choice_list[0]:
            print('Ok...Vamos te cadastrar.\n')
            
            login = input('Digite o seu nome de usuário\n')
            
            with open ('pessoas.json') as file:
                pessoafisica_json = json.load(file)
                
            pessoafisica_way = pessoafisica_json["ongs_cadastradas"]
            pessoafisica_insert = login in pessoafisica_json
            
            nome_pessoa = input('\nDigite o nome da sua ONG\n')
            endereco_pessoa = input('\nDigite o endereço da sua ONG\n') 
            
            loop2 = True
            while loop2:
                senha = input('\nDigite sua senha.\n')
                senha_confirmada = input('\nConfirme sua senha.\n')
                if senha != senha_confirmada:
                    print('\nSenhas não conferem. Digite novamente.\n')
                elif senha == senha_confirmada:
                    break
                
            alimentos_doados = input('Legal! Seu cadastro está quase acabando... Por último, escreva os alimentos que gostaria de receber.\n')       
            alimentos_doados = []
        #CONTINUAR A OPCAO DE LOGIN
        elif choice == choice_list[1]:
            print('CONTINUA') 