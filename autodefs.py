import formatacao
import main
import json

def go_to_menu():
    print('\nOk...Voltando para o menu principal\n')
    formatacao.formatting()
    print('- Bem vindo ao SeedS, aquecendo corações! -')
    formatacao.formatting()
    main.main_menu()

def make_register_empresas():
    print('Ok...Vamos cadastrar sua empresa!\n')
            
    login = input('Digite o seu nome de usuário\n')
    
    with open ('Json/empresas.json') as file:
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
            
            with open('Json/empresas.json', 'w') as final_file:
                json.dump({"empresas_cadastradas" : empresas_way}, final_file)
            final_file.close()

def make_login_empresas(): 
    print('\nOk...Vamos fazer o login!\n')
    login = input('Digite o seu usuário.\n')
    senha = input('\nDigite a sua senha.\n')
    
    with open('Json/empresas.json') as arquivo_validado:
        validation_file = json.load(arquivo_validado)
        
        validation_json = validation_file['empresas_cadastradas']
        
        loop = False
    
        if login in validation_json and senha == validation_json[login]['senha']:
            formatacao.formatting()
            print(f'Bem Vindo {login}!')
            formatacao.formatting()
            
            loop2 = True
            while loop2:
                choice2 = input('\nDigite (1) se deseja alterar informações.\nDigite (2) se deseja fazer adicionar informações\nDigite (3) se deseja voltar ao menu principal.\n')
                choice_list2 = ['1', '2', '3']
                
                if choice2 not in choice_list2:
                    print('\nOpção inválida! Tente novamente\n')
                
                elif choice_list2[2]:
                    go_to_menu()
                    
                    
def make_register_ongs():
    print('Ok...Vamos cadastrar sua ONG.\n')
            
    login = input('Digite o seu nome de usuário\n')
    
    with open ('ongs.json') as file:
        ongs_json = json.load(file)
        
    ongs_way = ongs_json["ongs_cadastradas"]
    ongs_insert = login in ongs_json
    
    nome_ong = input('\nDigite o nome da sua ONG\n')
    endereco_ong = input('\nDigite o endereço da sua ONG\n') 
    
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