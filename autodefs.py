import formatacao
import main
import json


#função que leva ao menu principal
def go_to_menu():
    print('\nOk...Voltando para o menu principal\n')
    formatacao.title(title1='- Bem vindo ao SeedS, aquecendo corações! -')
    main.main_menu()


#função para verificar se o usuario e o email já estão registrados   
def is_user_registered(login_empresas,email_empresa):
    with open('Json/empresas.json') as file:
        empresas_json = json.load(file)
    
    empresas_way = empresas_json["empresas_cadastradas"]
    
    for login, email_validation_empresas in empresas_way.items():
        if login == login_empresas:
            return "USER_EXISTS"
        elif "email_empresa" in email_validation_empresas and email_validation_empresas["email_empresa"] == email_empresa:
            return "EMAIL_EXISTS"
    
    return None


#função para ler o json das empresas
def readjson_empresas(login_empresas):
    with open('Json/empresas.json') as file:
        empresas_json = json.load(file)

    empresas_way = empresas_json["empresas_cadastradas"]
    empresas_insert = login_empresas in empresas_way
    file.close()

    return empresas_way, empresas_insert
 
 #função para inserir os dados no json das empresas   


#função para inserir os dados no json das empresas
def insertjson_empresas(login_empresas, nome_empresa, endereco_empresa,email_empresa, password_empresas, checkedpassword_empresas, donated_alimentos_empresas, empresas_way, empresas_insert):
    if not empresas_insert:
        if password_empresas == checkedpassword_empresas:
            empresas_way[login_empresas] = {
                "senha" : checkedpassword_empresas,
                "nome_empresa" : nome_empresa,
                "endereco_empresa" : endereco_empresa,
                "email_empresa" : email_empresa,
                "alimentos_doados" : donated_alimentos_empresas,
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
    
    looplogin = True
    while looplogin:  
        login_empresas = input('Digite seu nome de usuário:\n')
        email_empresa = input('\nDigite o seu email:\n')
        # Verifica se o usuário já está cadastrado no JSON
        result = is_user_registered(login_empresas, email_empresa)
        if result == "USER_EXISTS":
            print('\nUsuário já cadastrado. Por favor, escolha outro nome de usuário.\n')
        elif result == "EMAIL_EXISTS":
            print('\nE-mail já cadastrado. Por favor, utilize outro e-mail.\n')
        else:
            break
            
    nome_empresa = input('\nDigite o nome da sua empresa:\n')
    endereco_empresa = input('\nDigite o endereço da sua empresa:\n')
    
    loop2 = True
    while loop2:
        password_empresas = input('\nDigite sua senha:\n')
        checkedpassword_empresas = input('\nConfirme sua senha:\n')
        if password_empresas != checkedpassword_empresas:
            print('\nSenhas não conferem. Digite novamente.\n')
        elif password_empresas == checkedpassword_empresas:
            break 
            
    donated_alimentos_empresas = input('\nÓtimo! Seu cadastro está quase completo... Por último, digite os alimentos que pretende doar:\n')
    donated_alimentos_empresas = [donated_alimentos_empresas]
    
    empresas_way, empresas_insert = readjson_empresas(login_empresas)
    
    insertjson_empresas(login_empresas, nome_empresa, endereco_empresa,email_empresa, password_empresas, checkedpassword_empresas, donated_alimentos_empresas, empresas_way, empresas_insert)


#função para fazer o login das empresas
def make_login_empresas(validation_json, nome_empresa, endereco_empresa, donated_alimentos_empresas):
    print('\nOk... Vamos fazer o login!\n')
    login_empresas = input('Digite o seu usuário:\n')
    password_empresas = input('\nDigite a sua senha:\n')
    
    if login_empresas in validation_json and password_empresas == validation_json[login_empresas]['senha']:
        formatacao.lin()
        print(f'Bem-vindo, {login_empresas}!')
        formatacao.lin()
        
        while True:
            choice2 = input('\nDigite (1) para exibir suas informações.\nDigite (2) para adicionar informações.\nDigite (3) para voltar ao menu principal.\n')
            
            if choice2 == '1':
                print('\nOk... Vamos exibir suas informações!\n')
                
                if login_empresas in validation_json:
                    print('Informações da empresa:')
                    print(f'Nome: {validation_json[login_empresas][nome_empresa]}')
                    print(f'Endereço: {validation_json[login_empresas][endereco_empresa]}')
                    print(f'Alimentos doados: {validation_json[login_empresas][donated_alimentos_empresas]}')
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
                        

def readjson_ongs(login_ong):
    with open ('Json/empresas.json') as file:
        ongs_json = json.load(file)

                   
#função para fazer o cadastro das ongs                           
def make_register_ongs():
    print('Ok...Vamos cadastrar sua ONG.\n')
            
    login_ong = input('Digite o seu nome de usuário\n')
    
    with open ('ongs.json') as file:
        ongs_json = json.load(file)
        
    ongs_way = ongs_json["ongs_cadastradas"]
    ongs_insert = login_ong in ongs_json
    
    nome_ong = input('\nDigite o nome da sua ONG\n')
    endereco_ong = input('\nDigite o endereço da sua ONG\n') 
    
    loop2 = True
    while loop2:
        password_ong = input('\nDigite sua senha.\n')
        checkedpassword_ong = input('\nConfirme sua senha.\n')
        if password_ong != checkedpassword_ong:
            print('\nSenhas não conferem. Digite novamente.\n')
        elif password_ong == checkedpassword_ong:
            break
        
    recive_alimentos_ong = input('Legal! Seu cadastro está quase acabando... Por último, escreva os alimentos que gostaria de receber.\n')       
    recive_alimentos_ong = []