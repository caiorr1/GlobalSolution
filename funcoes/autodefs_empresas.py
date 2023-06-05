from funcoes.formatacao import title, lin
import main
import json


#função que leva ao menu principal
def go_to_menu():
    print('\nOk...Voltando para o menu principal\n')
    title(title1='- Bem vindo ao SeedS, aquecendo corações! -')
    main.main_menu()


#função para verificar se o usuario e o email já estão registrados   
def is_user_registered_empresas(login_empresas,email_empresa):
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
def insertjson_empresas(login_empresas, name_empresa, address_empresa,email_empresa, password_empresas, checkedpassword_empresas, donated_alimentos_empresas, empresas_way, empresas_insert):
    if not empresas_insert:
        if password_empresas == checkedpassword_empresas:
            empresas_way[login_empresas] = {
                "senha" : checkedpassword_empresas,
                "nome_empresa" : name_empresa,
                "endereco_empresa" : address_empresa,
                "email_empresa" : email_empresa,
                "alimentos_doados" : donated_alimentos_empresas,
            }
            print('\nOk! Seu cadastro foi salvo... Caso queira alterar, adicionar ou exibir suas informações, faça o login.\n')
            
            with open('Json/empresas.json', 'r') as file:
                data = json.load(file)
        
            data["empresas_cadastradas"].update(empresas_way)
        
            with open('Json/empresas.json', 'w') as file:
                json.dump(data, file, indent=4)
 

#funcao para carregar o json, usada para validação das empresas
def loadjson_empresas():
    with open('Json/empresas.json') as arquivo_validado:
        validation_file = json.load(arquivo_validado)
        
        validation_json = validation_file["empresas_cadastradas"]
    
    return validation_json


#função para fazer o registro das empresas
def make_register_empresas():
    print('Ok... Vamos cadastrar sua empresa!\n')
    
    looplogin = True
    while looplogin:  
        login_empresas = input('Digite seu nome de usuário:\n')
        email_empresa = input('\nDigite o seu email:\n')
        
        # Verifica se o usuário já está cadastrado no JSON
        result = is_user_registered_empresas(login_empresas, email_empresa)
        if result == "USER_EXISTS":
            print('\nUsuário já cadastrado. Por favor, escolha outro nome de usuário.\n')
        elif result == "EMAIL_EXISTS":
            print('\nE-mail já cadastrado. Por favor, utilize outro e-mail.\n')
        else:
            break
            
    name_empresa = input('\nDigite o nome da sua empresa:\n')
    address_empresa = input('\nDigite o endereço da sua empresa:\n').lower()
    
    loop2 = True
    while loop2:
        password_empresas = input('\nDigite sua senha:\n')
        checkedpassword_empresas = input('\nConfirme sua senha:\n')
        if password_empresas != checkedpassword_empresas:
            print('\nSenhas não conferem. Digite novamente.\n')
        elif password_empresas == checkedpassword_empresas:
            break 
            
    donated_alimentos_empresas = input('\nÓtimo! Seu cadastro está quase completo... Por último, digite os alimentos que pretende doar:\n').lower().replace(" ", ",")
    donated_alimentos_empresas = [donated_alimentos_empresas]
    
    print('\nCadastro completo! Salvando...\n')
    empresas_way, empresas_insert = readjson_empresas(login_empresas)
    
    insertjson_empresas(login_empresas, name_empresa, address_empresa,email_empresa, password_empresas, checkedpassword_empresas, donated_alimentos_empresas, empresas_way, empresas_insert)
    
    print('\nTudo Ok!\n')
    
    title(title1='Bem vindo à area para Empresas!')
    

#função para fazer o login das empresas
def make_login_empresas(validation_json):
    print('\nOk... Vamos fazer o login!\n')
    
    looplogin = True
    while looplogin:
    
        login_empresas = input('Digite o seu usuário:\n')
        password_empresas = input('\nDigite a sua senha:\n')
        
        if login_empresas in validation_json and password_empresas == validation_json[login_empresas]["senha"]:
            title(title1=f'Bem vindo {login_empresas}!')
           
            looplogin = False
            
            while True:
                choice2 = input('\nDigite (1) para exibir suas informações.\nDigite (2) para alterar informações. \nDigite (3) para adicionar mais alimentos na sua lista\nDigite (4) para voltar ao menu principal.\n')
                
                if choice2 == '1':
                    print('\nOk... Vamos exibir suas informações!\n')
                    
                    if login_empresas in validation_json:
                        print('Informações da empresa:')
                        print(f'Nome: {validation_json[login_empresas]["nome_empresa"]}')
                        print(f'Endereço: {validation_json[login_empresas]["endereco_empresa"]}')
                        print(f'Contato: {validation_json[login_empresas]["email_empresa"]}')
                        print(f'Alimentos doados: {validation_json[login_empresas]["alimentos_doados"]}')
                    else:
                        print('Empresa não encontrada.')
                    
                elif choice2 == '2':
                    print('\nOk... Vamos alterar informações!\n')
                    
                    new_cadaster_empresas = validation_json
                    
                    if login_empresas in new_cadaster_empresas:
                        print('\nVamos refazer o seu cadastro!\n')
                        
                        current_empresa = new_cadaster_empresas[login_empresas]
                        
                        new_name_empresas = input('Digite o novo nome da empresa:\n')
                        current_empresa['nome_empresa'] = new_name_empresas
                        
                        new_address_empresas = input('\nDigite o novo endereço:\n').lower()
                        current_empresa['endereco_empresa'] = new_address_empresas
                        
                        new_email_empresa = input('\nDigite o novo email:\n')
                        current_empresa['email_empresa'] = new_email_empresa
                        
                        with open('Json/empresas.json', 'r') as file:
                            data = json.load(file)
        
                        data['empresas_cadastradas'] = new_cadaster_empresas
        
                        with open('Json/empresas.json', 'w') as file:
                            json.dump(data, file, indent=4)
                            
                        print('\nInformações salvas com sucesso!\n')
                        title(title1='Bem vindo à area para Empresas!')
                        
                elif choice2 =='3':
                    print('\nOk...Vamos adicionar alimentos a sua lista!\n')
                    
                    with open('Json/empresas.json', 'r+') as file2:
                        data = json.load(file2)
                    
                    
                    if login_empresas in data["empresas_cadastradas"]:
                        lista_empresas = data["empresas_cadastradas"][login_empresas]["alimentos_doados"]
                        
                        loopstring = True
                        while loopstring:
    
                            new_alimento = input('Digite os alimentos que deseja adicionar na lista.\n').lower().replace(" ", ",")
                            if new_alimento.isnumeric():
                                print('\nDigite alimentos.\n')

                            else:
                                lista_empresas.append(new_alimento)
                                loopstring = False
                                print('Salvando...')
                        
                        data["empresas_cadastradas"][login_empresas]["alimentos_doados"] = lista_empresas
                        with open('Json/empresas.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        
                            print('\nA lista foi salva com êxito!\n')
                            
                            lin()
                            print(f'Bem vindo {login_empresas}!')
                            lin()    
                            
                elif choice2 == '4':
                    go_to_menu()
                    break
                    
                else:
                    print('\nOpção inválida! Tente novamente.\n')
        else:
            print('\nUsuário e senha não encontrados. Digite novamente.\n')
      

