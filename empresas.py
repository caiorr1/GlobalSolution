import formatacao
import main
import json

def get_companies():
    formatacao.formatting()
    print('Bem vindo à area para Empresas!')
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
            print('Ok...Vamos cadastrar sua empresa.\n')
            
            login = input('Digite o seu nome de usuário\n')
            
            with open ('empresas.json') as file:
                empresas_json = json.load(file)
    
            empresas_way = empresas_json["empresas_cadastradas"]
            empresas_insert = login in empresas_way
            
            nome_empresa = input('\nDigite o nome da sua empresa.\n')
            endereco_empresa = input('\nDigite o endereço da sua empresa.\n')
            
            loop2 = True
            while loop2:
                senha = input('\nDigite a sua senha.\n')
                senha_confirmada = input('\nConfirme a sua senha.\n')
                if senha != senha_confirmada:
                    print('\nSenhas não conferem. Digite novamente\n')
                elif senha == senha_confirmada:
                    break 
                    
            alimentos_doados = input('\nLegal! Seu cadastro está quase acabando... Por último, escreva os alimentos que pretende doar\n')
            alimentos_doados = []
            
            
            if not empresas_insert:
                if senha == senha_confirmada:
                    empresas_way[login] = {
                        "senha" : senha_confirmada,
                        "nome_empresa" : nome_empresa,
                        "endereco_empresa" : endereco_empresa,
                        "alimentos_doados" : alimentos_doados,
                    }
                    print('ok')
                    
                    with open('empresas.json', 'w') as final_file:
                        json.dumps({"empresas_cadastro" : empresas_way}, final_file)
                    final_file.close()
                    
                    
        #CONTINUAR A OPCAO DE LOGIN
        elif choice == choice_list[1]:
            print('CONTINUA')    