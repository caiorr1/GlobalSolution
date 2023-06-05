from funcoes.formatacao import title, lin
import main
import json


#função que leva ao menu principal
def go_to_menu():
    print('\nOk...Voltando para o menu principal\n')
    title(title1='- Bem vindo ao SeedS, aquecendo corações! -')
    main.menu_principal()


#função para verificar se o usuario e o email já estão registrados   
def usuario_cadastrado(login_empresas,email_empresa):
    with open('Json/empresas.json') as file:
        empresas_json = json.load(file)
    
    empresas_way = empresas_json["empresas_cadastradas"]
    
    for login, email_empresas in empresas_way.items():
        if login == login_empresas:
            return "usuario_existe"
        elif "email_empresa" in email_empresas and email_empresas["email_empresa"] == email_empresa:
            return "email_existe"
    
    return None


#função para ler o json das empresas
def ler_json(login_empresas):
    with open('Json/empresas.json') as file:
        empresas_json = json.load(file)

    empresas_way = empresas_json["empresas_cadastradas"]
    empresas_insert = login_empresas in empresas_way
    file.close()

    return empresas_way, empresas_insert
 
 #função para inserir os dados no json das empresas   


#função para inserir os dados no json das empresas
def inserir_json(login_empresas, name_empresa, address_empresa,email_empresa, password_empresas, checkedpassword_empresas, alimentos_a_doar, empresas_way, empresas_insert):
    if not empresas_insert:
        if password_empresas == checkedpassword_empresas:
            empresas_way[login_empresas] = {
                "senha" : checkedpassword_empresas,
                "nome_empresa" : name_empresa,
                "endereco_empresa" : address_empresa,
                "email_empresa" : email_empresa,
                "alimentos_a_doar" : alimentos_a_doar,
            }
            print('\nOk! Seu cadastro foi salvo... Caso queira alterar, adicionar ou exibir suas informações, faça o login.\n')
            
            with open('Json/empresas.json', 'r') as file:
                data = json.load(file)
        
            data["empresas_cadastradas"].update(empresas_way)
        
            with open('Json/empresas.json', 'w') as file:
                json.dump(data, file, indent=4)
 

#funcao para carregar o json, usada para validação das empresas
def carregar_json():
    with open('Json/empresas.json') as arquivo_validado:
        arquivo_validado = json.load(arquivo_validado)
        
        json_validado = arquivo_validado["empresas_cadastradas"]
    
    return json_validado


#função para fazer o registro das empresas
def registrar_empresas():
    print('Ok... Vamos cadastrar sua empresa!\n')
    
    loop = True
    while loop:  
        usuario_empresas = input('Digite seu nome de usuário:\n')
        email_empresa = input('\nDigite o seu email:\n')
        
        
        validando = usuario_cadastrado(usuario_empresas, email_empresa)
        if validando == "usuario_existe":
            print('\nUsuário já cadastrado. Por favor, escolha outro nome de usuário.\n')
        elif validando == "email_existe":
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
            
    alimentos_a_doar = input('\nÓtimo! Seu cadastro está quase completo... Por último, digite os alimentos que pretende doar:\n').lower().replace(" ", ",")
    alimentos_a_doar =  alimentos_a_doar.split(",")
    
    print('\nCadastro completo! Salvando...\n')
    empresas_way, empresas_insert = ler_json(usuario_empresas)
    
    inserir_json(usuario_empresas, name_empresa, address_empresa,email_empresa, password_empresas, checkedpassword_empresas, alimentos_a_doar, empresas_way, empresas_insert)
    
    print('\nTudo Ok!\n')
    
    title(title1='Bem vindo à area para Empresas!')
    

#função para fazer o login das empresas
def fazer_login(json_validado):
    print('\nOk... Vamos fazer o login!\n')
    
    looplogin = True
    while looplogin:
    
        login_empresas = input('Digite o seu usuário:\n')
        password_empresas = input('\nDigite a sua senha:\n')
        
        if login_empresas in json_validado and password_empresas == json_validado[login_empresas]["senha"]:
            title(title1=f'Bem vindo {login_empresas}!')
           
            looplogin = False
            
            while True:
                choice2 = input('\nDigite (1) para exibir suas informações.\nDigite (2) para alterar informações. \nDigite (3) para adicionar mais alimentos na sua lista\nDigite (4) para voltar ao menu principal.\n')
                
                if choice2 == '1':
                    print('\nOk... Vamos exibir suas informações!\n')
                    
                    if login_empresas in json_validado:
                        print('Informações da empresa:')
                        print(f'Nome: {json_validado[login_empresas]["nome_empresa"]}')
                        print(f'Endereço: {json_validado[login_empresas]["endereco_empresa"]}')
                        print(f'Contato: {json_validado[login_empresas]["email_empresa"]}')
                        print(f'Alimentos doados: {json_validado[login_empresas]["alimentos_a_doar"]}')
                    else:
                        print('\nEmpresa não encontrada.\n')
                    
                elif choice2 == '2':
                    print('\nVamos alterar informações!\n')
                    
                    novo_cadastro = json_validado
                    
                    if login_empresas in novo_cadastro:
                        print('\nVamos refazer o seu cadastro!\n')
                        
                        empresa_atual = novo_cadastro[login_empresas]
                        
                        novo_nome = input('Escreva o novo nome da empresa:\n')
                        empresa_atual['nome_empresa'] = novo_nome
                        
                        novo_endereco = input('\nEscreva o novo endereço:\n').lower()
                        empresa_atual['endereco_empresa'] = novo_endereco
                        
                        novo_email = input('\nEscreva o novo email:\n')
                        empresa_atual['email_empresa'] = novo_email
                        
                        with open('Json/empresas.json', 'r') as file:
                            novos_dados = json.load(file)
        
                        novos_dados['empresas_cadastradas'] = novo_cadastro
        
                        with open('Json/empresas.json', 'w') as file:
                            json.dump(novos_dados, file, indent=4)
                            
                        print('\nInformações salvas!\n')
                        title(title1='Bem vindo à area para Empresas!')
                        
                elif choice2 =='3':
                    print('\nVamos adicionar alimentos a sua lista!\n')
                    
                    with open('Json/empresas.json', 'r+') as file2:
                        caminho_empresas = json.load(file2)
                    
                    
                    if login_empresas in caminho_empresas["empresas_cadastradas"]:
                        lista_empresas = caminho_empresas["empresas_cadastradas"][login_empresas]["alimentos_a_doar"]
                        
                        looppp = True
                        while looppp:
    
                            new_alimento = input('Por Favor, digite os alimentos que deseja adicionar na lista.\n').lower().replace(" ", ",").split(",")
                            if new_alimento.isnumeric():
                                print('\nDigite alimentos.\n')

                            else:
                                lista_empresas.append(new_alimento)
                                looppp = False
                                print('Salvando...')
                        
                        with open('Json/empresas.json', 'w') as file:
                            json.dump(caminho_empresas, file, indent=4)
                        
                            print('\nA lista foi salva com êxito!\n')
                            
                            lin()
                            print(f'Bem vindo {login_empresas}!')
                            lin()    
                            
                elif choice2 == '4':
                    go_to_menu()
                    looppp = False
                    
                else:
                    print('\nOpção inválida! Tente novamente.\n')
        else:
            print('\nUsuário e senha não encontrados. Digite novamente.\n')
      

