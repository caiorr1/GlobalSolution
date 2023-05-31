import formatacao
import main
import json

def go_to_menu():
    print('\nOk...Voltando para o menu principal\n')
    formatacao.formatting()
    print('- Bem vindo ao SeedS, aquecendo corações! -')
    formatacao.formatting()
    main.main_menu()
   
#função para ler o json das empresas
def readjson_empresas(login):
    with open('Json/empresas.json') as file:
        empresas_json = json.load(file)

    empresas_way = empresas_json["empresas_cadastradas"]
    empresas_insert = login in empresas_way
    file.close()

    return empresas_way, empresas_insert
 
 #função para inserir os dados no json das empresas   
def insertjson_empresas(login, nome_empresa, endereco_empresa, senha, senha_confirmada, alimentos_doados, empresas_way, empresas_insert):
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

#funcao para carregar o json, usada para validação das empresas
def loadjson_empresas():
    with open('Json/empresas.json') as arquivo_validado:
        validation_file = json.load(arquivo_validado)
        
        validation_json = validation_file['empresas_cadastradas']
    
    return validation_json

#função para fazer o registro das empresas
def make_register_empresas():
    print('Ok... Vamos cadastrar sua empresa!\n')
            
    login = input('Digite seu nome de usuário:\n')
    
    nome_empresa = input('\nDigite o nome da sua empresa:\n')
    endereco_empresa = input('\nDigite o endereço da sua empresa:\n')
    
    loop2 = True
    while loop2:
        senha = input('\nDigite sua senha:\n')
        senha_confirmada = input('\nConfirme sua senha:\n')
        if senha != senha_confirmada:
            print('\nSenhas não conferem. Digite novamente.\n')
        elif senha == senha_confirmada:
            break 
            
    alimentos_doados = input('\nÓtimo! Seu cadastro está quase completo... Por último, digite os alimentos que pretende doar:\n')
    alimentos_doados = [alimentos_doados]
    
    empresas_way, empresas_insert = readjson_empresas(login)
    
    insertjson_empresas(login, nome_empresa, endereco_empresa, senha, senha_confirmada, alimentos_doados, empresas_way, empresas_insert)

#função para fazer o login das empresas
def make_login_empresas(validation_json, nome_empresa, endereco_empresa, alimentos_doados):
    print('\nOk... Vamos fazer o login!\n')
    login = input('Digite o seu usuário:\n')
    senha = input('\nDigite a sua senha:\n')
    
    if login in validation_json and senha == validation_json[login]['senha']:
        formatacao.formatting()
        print(f'Bem-vindo, {login}!')
        formatacao.formatting()
        
        while True:
            choice2 = input('\nDigite (1) para exibir suas informações.\nDigite (2) para adicionar informações.\nDigite (3) para voltar ao menu principal.\n')
            
            if choice2 == '1':
                print('\nOk... Vamos exibir suas informações!\n')
                
                if login in validation_json:
                    print('Informações da empresa:')
                    print(f'Nome: {validation_json[login][nome_empresa]}')
                    print(f'Endereço: {validation_json[login][endereco_empresa]}')
                    print(f'Alimentos doados: {validation_json[login][alimentos_doados]}')
                else:
                    print('Empresa não encontrada.')
                
            elif choice2 == '2':
                print('\nOk... Vamos adicionar informações!\n')
                # Lógica para adicionar informações da empresa
                
            elif choice2 == '3':
                go_to_menu()
                break
                
            else:
                print('\nOpção inválida! Tente novamente.\n')
                        
                    
#função para fazer o cadastro das ongs                           
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