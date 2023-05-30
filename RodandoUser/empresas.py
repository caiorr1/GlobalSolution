import formatacao
import main
import json
import Alteracao.alterardados_empresas as alterardados_empresas


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
            print('Ok...Vamos cadastrar sua empresa!\n')
            
            login = input('Digite o seu nome de usuário\n')
            
            with open ('./../Json/empresas.json') as file:
                empresas_json = json.load(file)
    
            empresas_way = empresas_json["empresas_cadastradas"]
            empresas_insert = login in empresas_way
            file.close()
            
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
            alimentos_doados = [alimentos_doados]
            
            
            if not empresas_insert:
                if senha == senha_confirmada:
                    empresas_way[login] = {
                        "senha" : senha_confirmada,
                        "nome_empresa" : nome_empresa,
                        "endereco_empresa" : endereco_empresa,
                        "alimentos_doados" : alimentos_doados,
                    }
                    print('\nOk! Seu cadastro foi salvo... Caso queira alterar, adicionar ou exibir suas informações, faça o login.\n')
                    
                    with open('empresas.json', 'w') as final_file:
                        json.dump({"empresas_cadastradas" : empresas_way}, final_file)
                    final_file.close()
                    
                    
        #CONTINUAR A OPCAO DE LOGIN
        elif choice == choice_list[1]:
            print('\nOk...Vamos fazer o login!\n')
            login = input('Digite o seu usuário.\n')
            senha = input('\nDigite a sua senha.\n')
            
            with open('./../Json/empresas.json') as arquivo_validado:
                validation_json = json.load(arquivo_validado)
                
                empresas_way2 = validation_json["empresas_cadastradas"]
                
            if login in empresas_way2: 
                
                if senha == empresas_way2[login]['senha']:
                    print('ok')