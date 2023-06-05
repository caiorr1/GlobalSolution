from funcoes.formatacao import title, lin
import json
import funcoes.autodefs_empresas as autodefs_empresas


# função para verificar se o usuario e o email já estão registrados   
def usuario_registrado_ongs(login_ong, email_ong):
    with open('Json/ongs.json') as file:
        ongs_json = json.load(file)
    
    ongs_way = ongs_json["ongs_cadastradas"]
    
    for login, email_validation_ong in ongs_way.items():
        if login == login_ong:
            return "usuario_existe"
        elif "email_ong" in email_validation_ong and email_validation_ong["email_ong"] == email_ong:
            return "email_existe"
    
    return None


# função para ler o json das ongs   
def lerjson_ongs(login_ong):
    with open ('Json/ongs.json') as file:
        ongs_json = json.load(file)
    
    ongs_way = ongs_json["ongs_cadastradas"]
    ongs_insert = login_ong in ongs_way
    file.close()
    
    return ongs_way, ongs_insert


# função para inserir os dados no json das ongs
def inserirjson_ongs(login_ong, name_ong, address_ong, email_ong, password_ong, checkedpassord_ong, alimentos_a_receber, ongs_way, ongs_insert):
    if not ongs_insert:
        if password_ong == checkedpassord_ong:
            ongs_way[login_ong] = {
                "senha" : checkedpassord_ong,
                "nome_ong" : name_ong,
                "endereco_ong" : address_ong,
                "email_ong" : email_ong,
                "alimentos_a_receber" : alimentos_a_receber,
            }
            print('\nOk! Seu cadastro foi salvo... Caso queira alterar, adicionar ou exibir suas informações, faça o login.\n')
            
            with open('Json/ongs.json', 'r') as file:
                data = json.load(file)
        
            data["ongs_cadastradas"].update(ongs_way)
        
            with open('Json/ongs.json', 'w') as file:
                json.dump(data, file, indent=4)

# funcao para carregar o json, usada para validação das ongs
def carregarjson_ongs():
    with open('Json/ongs.json') as arquivo_validado:
       arquivo_validado_ongs = json.load(arquivo_validado)
        
    json_validado_ongs = arquivo_validado_ongs["ongs_cadastradas"]
    
    return json_validado_ongs


# função para fazer o cadastro das ongs                           
def registrar_ongs():
    print('Ok... Vamos cadastrar sua ONG!\n')
    
    looplogin = True
    while looplogin:  
        login_ong = input('Digite seu nome de usuário:\n')
        email_ong = input('\nDigite o seu email:\n')
        
        # verifica se o usuário já está cadastrado no JSON
        validar_registro_ong = usuario_registrado_ongs(login_ong, email_ong)
        if validar_registro_ong == "usuario_existe":
            print('\nUsuário já cadastrado. Por favor, escolha outro nome de usuário.\n')
        elif validar_registro_ong == "email_existe":
            print('\nE-mail já cadastrado. Por favor, utilize outro e-mail.\n')
        else:
            break
            
    name_ong = input('\nDigite o nome da sua ONG:\n')
    address_ong = input('\nDigite o endereço da sua ONG:\n').lower()
    
    loop2 = True
    while loop2:
        password_ong = input('\nDigite sua senha:\n')
        checkedpassord_ong = input('\nConfirme sua senha:\n')
        if password_ong != checkedpassord_ong:
            print('\nSenhas não conferem. Digite novamente.\n')
        elif password_ong == checkedpassord_ong:
            break 
            
    alimentos_a_receber = input('\nÓtimo! Seu cadastro está quase completo... Por último, digite os alimentos que gostaria de receber:\n').lower().replace(" ", ",")
    alimentos_a_receber = [alimentos_a_receber]
    
    print('\nCadastro completo! Salvando...\n')
    ongs_way, ongs_insert = lerjson_ongs(login_ong)
    
    inserirjson_ongs(login_ong, name_ong, address_ong, email_ong, password_ong, checkedpassord_ong, alimentos_a_receber, ongs_way, ongs_insert)
    
    print('\nTudo Ok!\n')
    
    title(title1='Bem vindo à area para ONGs!')
    
    
#função para fazer o login das ongs
def login_ongs(json_validado_ongs):
    print('\nOk... Vamos fazer o login!\n')
    
    looplogin = True
    while looplogin:
    
        login_ong = input('Digite o seu usuário:\n')
        password_ong = input('\nDigite a sua senha:\n')
        
        json_validado_ongs = carregarjson_ongs()
        
        if login_ong in json_validado_ongs and password_ong == json_validado_ongs[login_ong]["senha"]:
            title(title1=f'Bem vindo {login_ong}!')
           
            looplogin = False
            
            while True:
                choice2 = input('\nDigite (1) para exibir suas informações.\nDigite (2) para alterar informações. \nDigite (3) para adicionar mais alimentos na sua lista\nDigite (4) para voltar ao menu principal.\n')
                
                if choice2 == '1':
                    print('\nOk... Vamos exibir suas informações!\n')
                    
                    if login_ong in json_validado_ongs:
                        lin()
                        print('Informações da ONG:')
                        print(f'Nome: {json_validado_ongs[login_ong]["nome_ong"]}')
                        print(f'Endereço: {json_validado_ongs[login_ong]["endereco_ong"]}')
                        print(f'Contato: {json_validado_ongs[login_ong]["email_ong"]}')
                        print(f'Alimentos que gostariam de receber: {json_validado_ongs[login_ong]["alimentos_a_receber"]}')
                        lin()
                    else:
                        print('\nONG não encontrada.\n')
                    
                elif choice2 == '2':
                    print('\nOk... Vamos alterar informações!\n')
                    
                    new_cadaster_ong = json_validado_ongs
                    
                    if login_ong in new_cadaster_ong:
                        print('\nVamos refazer o seu cadastro!\n')
                        
                        current_ong = new_cadaster_ong[login_ong]
                        
                        new_name_ong = input('Digite o novo nome da ONG:\n')
                        current_ong['nome_ong'] = new_name_ong
                        
                        new_address_ong = input('\nDigite o novo endereço:\n').lower()
                        current_ong['endereco_ong'] = new_address_ong
                        
                        new_email_ong= input('\nDigite o novo email:\n')
                        current_ong['email_ong'] = new_email_ong
                        
                        with open('Json/ongs.json', 'r') as file:
                            data_ongs = json.load(file)
        
                        data_ongs["ongs_cadastradas"][login_ong] = current_ong
        
                        with open('Json/ongs.json', 'w') as file:
                            json.dump(data_ongs, file, indent=4)

                        print('\nInformações salvas com sucesso!\n')
                        title(title1='Bem vindo à area para ONGs!')
                        
                elif choice2 =='3':
                    print('\nVamos adicionar alimentos a sua lista!\n')
                    
                    with open('Json/ongs.json', 'r+') as file2:
                        caminho_ongs = json.load(file2)
                    
                    
                    if login_ong in caminho_ongs["ongs_cadastradas"]:
                        lista_ongs = caminho_ongs["ongs_cadastradas"][login_ong]["alimentos_a_receber"]
                        
                        loopstring = True
                        while loopstring:
    
                            new_alimento = input('Digite os alimentos que deseja adicionar na lista.\n').lower().replace(" ", ",")
                            if new_alimento.isnumeric():
                                print('\nDigite alimentos.\n')

                            else:
                                lista_ongs.append(new_alimento)
                                loopstring = False
                                print('Salvando...')

                        with open('Json/ongs.json', 'w') as file:
                            json.dump(caminho_ongs, file, indent=4)
                            
                            print('\nA lista foi salva com êxito!\n')
                            
                            lin()
                            print(f'Bem vindo {login_ong}!')
                            lin()    
                            
                elif choice2 == '4':
                    autodefs_empresas.go_to_menu()
                    break
                    
                else:
                    print('\nOpção inválida! Tente novamente.\n')
        else:
            print('\nUsuário e senha não encontrados. Digite novamente.\n')