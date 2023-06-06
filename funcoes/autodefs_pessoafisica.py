from funcoes.formatacao import title, lin
import json
import funcoes.autodefs_empresas as autodefs_empresas


# função para verificar se o usuario e o email já estão registrados   
def pessoasfisicas_cadastradas(login_pessoa, email_pessoa):
    with open('json/pessoas.json') as file:
        pessoas_json = json.load(file)
    
    pessoas_way = pessoas_json["pessoas_cadastradas"]
    
    for login, email_validado_pessoa in pessoas_way.items():
        if login == login_pessoa:
            return "usuario_existe"
        elif "email_pessoa" in email_validado_pessoa and email_validado_pessoa["email_pessoa"] == email_pessoa:
            return "email_existe"
    
    return None


# função para ler o json das pessoas fisicas
def lerjson_pessoasfisicas(login_pessoa):
    with open ('json/pessoas.json') as file:
        pessoas_json = json.load(file)
    
    pessoas_way = pessoas_json["pessoas_cadastradas"]
    pessoas_insert = login_pessoa in pessoas_way
    file.close()
    
    return pessoas_way, pessoas_insert


# função para inserir os dados no json das pessoas fisicas
def inserirjson_pessoasfisicas(login_pessoa, name_pessoa, address_pessoa, email_pessoa, password_pessoa, checkedpassord_pessoa, alimentos_a_doar, pessoas_way, pessoas_insert):
    if not pessoas_insert:
        if password_pessoa == checkedpassord_pessoa:
            pessoas_way[login_pessoa] = {
                "senha" : checkedpassord_pessoa,
                "nome_pessoa" : name_pessoa,
                "endereco_pessoa" : address_pessoa,
                "email_pessoa" : email_pessoa,
                "alimentos_a_doar" : alimentos_a_doar,            
            }
            print('\nOk! Seu cadastro foi salvo... Caso queira alterar, adicionar ou exibir suas informações, faça o login.\n')
            
            with open('json/pessoas.json', 'r') as file:
                data = json.load(file)
        
            data["pessoas_cadastradas"].update(pessoas_way)
        
            with open('json/pessoas.json', 'w') as file:
                json.dump(data, file, indent=4)
            
            
# funcao para carregar o json, usada para validação das pessoas fisicas
def carregarjson_pessoasfisicas():
    with open('json/pessoas.json') as arquivo_validado:
        arquivo_validado_pessoas = json.load(arquivo_validado)
        
        json_validado_pessoas = arquivo_validado_pessoas["pessoas_cadastradas"]
    
    return json_validado_pessoas


# função para fazer o cadastro das pessoas fisicas                           
def registrar_pessoafisica():
    print('Ok... Vamos fazer o seu cadastro !\n')
    
    looplogin = True
    while looplogin:  
        login_pessoa = input('Digite seu nome de usuário:\n')
        email_pessoa = input('\nDigite o seu email:\n')
        
        # verifica se o usuário já está cadastrado no JSON
        result_pessoa = pessoasfisicas_cadastradas(login_pessoa, email_pessoa)
        if result_pessoa == "usuario_existe":
            print('\nUsuário já cadastrado. Por favor, escolha outro nome de usuário.\n')
        elif result_pessoa == "email_existe":
            print('\nE-mail já cadastrado. Por favor, utilize outro e-mail.\n')
        else:
            break
            
    name_pessoa = input('\nDigite o seu nome:\n')
    address_pessoa = input('\nDigite o seu endereço:\n').lower()
    
    loop2 = True
    while loop2:
        password_pessoa = input('\nDigite sua senha:\n')
        checkedpassord_pessoa = input('\nConfirme sua senha:\n')
        if password_pessoa != checkedpassord_pessoa:
            print('\nSenhas não conferem. Digite novamente.\n')
        elif password_pessoa == checkedpassord_pessoa:
            break 
            
    alimentos_a_doar = input('\nÓtimo! Seu cadastro está quase completo... Por último, digite os alimentos que gostaria de doar:\n').lower().replace(" ", ",")
    alimentos_a_doar = alimentos_a_doar.split(",")
    
    print('\nCadastro completo! Salvando...\n')
    pessoas_way, pessoas_insert = lerjson_pessoasfisicas(login_pessoa)
    
    inserirjson_pessoasfisicas(login_pessoa, name_pessoa, address_pessoa, email_pessoa, password_pessoa, checkedpassord_pessoa, alimentos_a_doar, pessoas_way, pessoas_insert)
    
    print('\nTudo Ok!\n')
    
    
    title(title1='Bem vindo à area para Pessoas Fisícas!')
    
    
def login_pessoafisica(json_validado_pessoasfisicas):
    print('\nOk... Vamos fazer o login!\n')
    
    looplogin = True
    while looplogin:
    
        login_pessoa = input('Digite o seu usuário:\n')
        password_pessoa = input('\nDigite a sua senha:\n')
        
        json_validado_pessoasfisicas = carregarjson_pessoasfisicas()
        
        if login_pessoa in json_validado_pessoasfisicas and password_pessoa == json_validado_pessoasfisicas[login_pessoa]["senha"]:
            title(title1=f'Bem vindo {login_pessoa}!')
           
            looplogin = False
            
            while True:
                choice2 = input('\nDigite (1) para exibir suas informações.\nDigite (2) para alterar informações. \nDigite (3) para adicionar mais alimentos na sua lista\nDigite (4) para voltar ao menu principal.\n')
                
                if choice2 == '1':
                    print('\nOk... Vamos exibir suas informações!\n')
                    
                    if login_pessoa in json_validado_pessoasfisicas:
                        lin()
                        print('Informações do Usuário:')
                        print(f'Nome: {json_validado_pessoasfisicas[login_pessoa]["nome_pessoa"]}')
                        print(f'Endereço: {json_validado_pessoasfisicas[login_pessoa]["endereco_pessoa"]}')
                        print(f'Contato: {json_validado_pessoasfisicas[login_pessoa]["email_pessoa"]}')
                        print(f'Alimentos doados: {json_validado_pessoasfisicas[login_pessoa]["alimentos_a_doar"]}')
                        lin()
                    else:
                        print('\nUsuário não encontrado.\n')
                    
                elif choice2 == '2':
                    print('\nOk... Vamos alterar informações!\n')
                    
                    novo_cadastro_pessoafisica = json_validado_pessoasfisicas
                    
                    if login_pessoa in novo_cadastro_pessoafisica:
                        print('\nVamos refazer o seu cadastro!\n')
                        
                        pessoafisica_atual = novo_cadastro_pessoafisica[login_pessoa]
                        
                        novo_nome_pessoafisica = input('\nEscreva o seu novo nome:\n')
                        pessoafisica_atual['nome_pessoa'] = novo_nome_pessoafisica
                        
                        novo_endereco_pessoafisica = input('\nEscreva o novo endereço:\n').lower()
                        pessoafisica_atual['endereco_pessoa'] = novo_endereco_pessoafisica
                        
                        novo_email_pessoafisica = input('\nEscreva o novo email:\n')
                        pessoafisica_atual['email_pessoa'] = novo_email_pessoafisica

                        with open('json/pessoas.json', 'r') as file:
                            dados_pessoafisica = json.load(file)
                        
                        dados_pessoafisica['pessoas_cadastradas'] = novo_cadastro_pessoafisica
                        
                        with open('json/pessoas.json', 'w') as file:
                            json.dump(dados_pessoafisica, file, indent=4)

                        print('\nInformações salvas\n')
                        title(title1='Bem vindo à area para Pessoas Fisícas!')
                        
                elif choice2 =='3':
                    print('\nVamos adicionar alimentos a sua lista!\n')
                    
                    with open('json/pessoas.json', 'r+') as file2:
                        caminho_pessoasfisicas = json.load(file2)
                    
                    
                    if login_pessoa in caminho_pessoasfisicas["pessoas_cadastradas"]:
                        lista_pessoas = caminho_pessoasfisicas["pessoas_cadastradas"][login_pessoa]["alimentos_a_doar"]
                        
                        loopstring = True
                        while loopstring:
    
                            novo_alimento = input('Por favor, digite os alimentos que deseja adicionar na lista.\n').lower().replace(" ", ",").split(",")
                            valida_string = True
                            for alimento_string in novo_alimento:
                                if not alimento_string.isnumeric():
                                    valida_string = False
                                    break
                                
                            if valida_string:
                                print('\nDigite alimentos.\n')

                            else:
                                lista_pessoas.extend(novo_alimento)
                                loopstring = False
                                print('Salvando...')


                        with open('json/pessoas.json', 'w') as file:
                            json.dump(caminho_pessoasfisicas,file, indent=4)
                            
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
    