from funcoes.formatacao import title, lin
import json
import funcoes.autodefs_empresas as autodefs_empresas


# função para verificar se o usuario e o email já estão registrados   
def is_user_registered_pessoa(login_pessoa, email_pessoa):
    with open('Json/pessoas.json') as file:
        pessoas_json = json.load(file)
    
    pessoas_way = pessoas_json["pessoas_cadastradas"]
    
    for login, email_validation_pessoa in pessoas_way.items():
        if login == login_pessoa:
            return "USER_EXISTS"
        elif "email_pessoa" in email_validation_pessoa and email_validation_pessoa["email_pessoa"] == email_pessoa:
            return "EMAIL_EXISTS"
    
    return None


# função para ler o json das pessoas fisicas
def readjson_pessoas(login_pessoa):
    with open ('Json/pessoas.json') as file:
        pessoas_json = json.load(file)
    
    pessoas_way = pessoas_json["pessoas_cadastradas"]
    pessoas_insert = login_pessoa in pessoas_way
    file.close()
    
    return pessoas_way, pessoas_insert


# função para inserir os dados no json das pessoas fisicas
def insertjson_pessoas(login_pessoa, name_pessoa, address_pessoa, email_pessoa, password_pessoa, checkedpassord_pessoa, donated_alimentos_pessoa, pessoas_way, pessoas_insert):
    if not pessoas_insert:
        if password_pessoa == checkedpassord_pessoa:
            pessoas_way[login_pessoa] = {
                "senha" : checkedpassord_pessoa,
                "nome_pessoa" : name_pessoa,
                "endereco_pessoa" : address_pessoa,
                "email_pessoa" : email_pessoa,
                "alimentos_doados" : donated_alimentos_pessoa,            
            }
            print('\nOk! Seu cadastro foi salvo... Caso queira alterar, adicionar ou exibir suas informações, faça o login.\n')
            
            with open('Json/pessoas.json', 'r') as file:
                data = json.load(file)
        
            data["pessoas_cadastradas"].update(pessoas_way)
        
            with open('Json/pessoas.json', 'w') as file:
                json.dump(data, file, indent=4)
            
            
# funcao para carregar o json, usada para validação das pessoas fisicas
def loadjson_pessoas():
    with open('Json/pessoas.json') as arquivo_validado:
        validation_file_pessoas = json.load(arquivo_validado)
        
        validation_json_pessoas = validation_file_pessoas["pessoas_cadastradas"]
    
    return validation_json_pessoas


# função para fazer o cadastro das pessoas fisicas                           
def make_register_pessoa():
    print('Ok... Vamos fazer o seu cadastro !\n')
    
    looplogin = True
    while looplogin:  
        login_pessoa = input('Digite seu nome de usuário:\n')
        email_pessoa = input('\nDigite o seu email:\n')
        
        # verifica se o usuário já está cadastrado no JSON
        result_pessoa = is_user_registered_pessoa(login_pessoa, email_pessoa)
        if result_pessoa == "USER_EXISTS":
            print('\nUsuário já cadastrado. Por favor, escolha outro nome de usuário.\n')
        elif result_pessoa == "EMAIL_EXISTS":
            print('\nE-mail já cadastrado. Por favor, utilize outro e-mail.\n')
        else:
            break
            
    name_pessoa = input('\nDigite o seu nome :\n')
    address_pessoa = input('\nDigite o seu endereço :\n')
    
    loop2 = True
    while loop2:
        password_pessoa = input('\nDigite sua senha:\n')
        checkedpassord_pessoa = input('\nConfirme sua senha:\n')
        if password_pessoa != checkedpassord_pessoa:
            print('\nSenhas não conferem. Digite novamente.\n')
        elif password_pessoa == checkedpassord_pessoa:
            break 
            
    donated_alimentos_pessoa = input('\nÓtimo! Seu cadastro está quase completo... Por último, digite os alimentos que gostaria de doar:\n')
    donated_alimentos_pessoa = [donated_alimentos_pessoa]
    
    print('\nCadastro completo! Salvando...\n')
    pessoas_way, pessoas_insert = readjson_pessoas(login_pessoa)
    
    insertjson_pessoas(login_pessoa, name_pessoa, address_pessoa, email_pessoa, password_pessoa, checkedpassord_pessoa, donated_alimentos_pessoa, pessoas_way, pessoas_insert)
    
    print('\nTudo Ok!\n')
    
    
    title(title1='Bem vindo à area para Pessoas Fisícas!')
    
    
def make_login_pessoa(validation_json_pessoas):
    print('\nOk... Vamos fazer o login!\n')
    
    looplogin = True
    while looplogin:
    
        login_pessoa = input('Digite o seu usuário:\n')
        password_pessoa = input('\nDigite a sua senha:\n')
        
        validation_json_pessoas = loadjson_pessoas()
        
        if login_pessoa in validation_json_pessoas and password_pessoa == validation_json_pessoas[login_pessoa]["senha"]:
            title(title1=f'Bem vindo {login_pessoa}!')
           
            looplogin = False
            
            while True:
                choice2 = input('\nDigite (1) para exibir suas informações.\nDigite (2) para alterar informações. \nDigite (3) para adicionar mais alimentos na sua lista\nDigite (4) para voltar ao menu principal.\n')
                
                if choice2 == '1':
                    print('\nOk... Vamos exibir suas informações!\n')
                    
                    if login_pessoa in validation_json_pessoas:
                        lin()
                        print('Informações do Usuário:')
                        print(f'Nome: {validation_json_pessoas[login_pessoa]["nome_pessoa"]}')
                        print(f'Endereço: {validation_json_pessoas[login_pessoa]["endereco_pessoa"]}')
                        print(f'Contato: {validation_json_pessoas[login_pessoa]["email_pessoa"]}')
                        print(f'Alimentos doados: {validation_json_pessoas[login_pessoa]["alimentos_doados"]}')
                        lin()
                    else:
                        print('\nUsuário não encontrado.\n')
                    
                elif choice2 == '2':
                    print('\nOk... Vamos alterar informações!\n')
                    
                    new_cadaster_pessoa = validation_json_pessoas
                    
                    if login_pessoa in new_cadaster_pessoa:
                        print('\nVamos refazer o seu cadastro!\n')
                        
                        current_pessoa = new_cadaster_pessoa[login_pessoa]
                        
                        new_name_pessoa = input('Digite o seu novo nome:\n')
                        current_pessoa['nome_pessoa'] = new_name_pessoa
                        
                        new_address_pessoa = input('\nDigite o novo endereço:\n')
                        current_pessoa['endereco_pessoa'] = new_address_pessoa
                        
                        new_email_pessoa = input('\nDigite o novo email:\n')
                        current_pessoa['email_pessoa'] = new_email_pessoa

                        with open('Json/pessoas.json', 'r') as file:
                            data = json.load(file)
                        
                        data['pessoas_cadastradas'] = new_cadaster_pessoa
                        
                        with open('Json/pessoas.json', 'w') as file:
                            json.dump(data, file, indent=4)

                        print('\nInformações salvas com sucesso!\n')
                        title(title1='Bem vindo à area para Pessoas Fisícas!')
                        
                elif choice2 =='3':
                    print('\nOk...Vamos adicionar alimentos a sua lista!\n')
                    
                    with open('Json/pessoas.json', 'r+') as file2:
                        data_pessoas = json.load(file2)
                    
                    
                    if login_pessoa in data_pessoas["pessoas_cadastradas"]:
                        lista_pessoas = data_pessoas["pessoas_cadastradas"][login_pessoa]["alimentos_doados"]
                        
                        loopstring = True
                        while loopstring:
    
                            new_alimento = input('Digite os alimentos que deseja adicionar na lista.\n')
                            if new_alimento.isnumeric():
                                print('\nDigite alimentos.\n')

                            else:
                                lista_pessoas.append(new_alimento)
                                loopstring = False
                                print('Salvando...')

                        data_pessoas["pessoas_cadastradas"][login_pessoa]["alimentos_doados"] = lista_pessoas
                        with open('Json/pessoas.json', 'w') as file:
                            json.dump(data_pessoas,file, indent=4)
                            
                            print('\nA lista foi salva com êxito!\n')
                            
                            lin()
                            print(f'Bem vindo {login_pessoa}!')
                            lin()    
                            
                elif choice2 == '4':
                    autodefs_empresas.go_to_menu()
                    break
                    
                else:
                    print('\nOpção inválida! Tente novamente.\n')
        else:
            print('\nUsuário e senha não encontrados. Digite novamente.\n')
    