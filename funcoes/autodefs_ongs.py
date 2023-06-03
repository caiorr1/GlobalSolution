from funcoes.formatacao import title, lin
import json
import funcoes.autodefs_empresas as autodefs_empresas


#função para verificar se o usuario e o email já estão registrados   
def is_user_registered_ongs(login_ong, email_ong):
    with open('Json/ongs.json') as file:
        ongs_json = json.load(file)
    
    ongs_way = ongs_json["ongs_cadastradas"]
    
    for login, email_validation_ong in ongs_way.items():
        if login == login_ong:
            return "USER_EXISTS"
        elif "email_ong" in email_validation_ong and email_validation_ong["email_ong"] == email_ong:
            return "EMAIL_EXISTS"
    
    return None


#função para ler o json das ongs   
def readjson_ongs(login_ong):
    with open ('Json/ongs.json') as file:
        ongs_json = json.load(file)
    
    ongs_way = ongs_json["ongs_cadastradas"]
    ongs_insert = login_ong in ongs_way
    file.close()
    
    return ongs_way, ongs_insert


#função para inserir os dados no json das ongs
def insertjson_ongs(login_ong, name_ong, address_ong, email_ong, password_ong, checkedpassord_ong, recived_alimentos_ong, ongs_way, ongs_insert):
    if not ongs_insert:
        if password_ong == checkedpassord_ong:
            ongs_way[login_ong] = {
                "senha" : checkedpassord_ong,
                "nome_ong" : name_ong,
                "endereco_ong" : address_ong,
                "email_ong" : email_ong,
                "receber_alimentos" : recived_alimentos_ong,
            }
            print('\nOk! Seu cadastro foi salvo... Caso queira alterar, adicionar ou exibir suas informações, faça o login.\n')
            
            with open('Json/ongs.json', 'w') as final_file:
                json.dump({"ongs_cadastradas" : ongs_way}, final_file)
            final_file.close()


#funcao para carregar o json, usada para validação das ongs
def loadjson_ongs():
    with open('Json/ongs.json') as arquivo_validado:
        validation_file_ongs = json.load(arquivo_validado)
        
        validation_json_ongs = validation_file_ongs["ongs_cadastradas"]
    
    return validation_json_ongs


#função para fazer o cadastro das ongs                           
def make_register_ongs():
    print('Ok... Vamos cadastrar sua ONG!\n')
    
    looplogin = True
    while looplogin:  
        login_ong = input('Digite seu nome de usuário:\n')
        email_ong = input('\nDigite o seu email:\n')
        
        # Verifica se o usuário já está cadastrado no JSON
        result_ong = is_user_registered_ongs(login_ong, email_ong)
        if result_ong == "USER_EXISTS":
            print('\nUsuário já cadastrado. Por favor, escolha outro nome de usuário.\n')
        elif result_ong == "EMAIL_EXISTS":
            print('\nE-mail já cadastrado. Por favor, utilize outro e-mail.\n')
        else:
            break
            
    name_ong = input('\nDigite o nome da sua ONG:\n')
    address_ong = input('\nDigite o endereço da sua ONG:\n')
    
    loop2 = True
    while loop2:
        password_ong = input('\nDigite sua senha:\n')
        checkedpassord_ong = input('\nConfirme sua senha:\n')
        if password_ong != checkedpassord_ong:
            print('\nSenhas não conferem. Digite novamente.\n')
        elif password_ong == checkedpassord_ong:
            break 
            
    recived_alimentos_ong = input('\nÓtimo! Seu cadastro está quase completo... Por último, digite os alimentos que gostaria de receber:\n')
    recived_alimentos_ong = [recived_alimentos_ong]
    
    print('\nCadastro completo! Salvando...\n')
    ongs_way, ongs_insert = readjson_ongs(login_ong)
    
    insertjson_ongs(login_ong, name_ong, address_ong, email_ong, password_ong, checkedpassord_ong, recived_alimentos_ong, ongs_way, ongs_insert)
    
    print('\nTudo Ok!\n')
    
    title(title1='Bem vindo à area para ONGs!')
    
    
#função para fazer o login das ongs
def make_login_ongs(validation_json_ongs):
    print('\nOk... Vamos fazer o login!\n')
    
    looplogin = True
    while looplogin:
    
        login_ong = input('Digite o seu usuário:\n')
        password_ong = input('\nDigite a sua senha:\n')
        
        validation_json_ongs = loadjson_ongs()
        
        if login_ong in validation_json_ongs and password_ong == validation_json_ongs[login_ong]["senha"]:
            title(title1=f'Bem vindo {login_ong}!')
           
            looplogin = False
            
            while True:
                choice2 = input('\nDigite (1) para exibir suas informações.\nDigite (2) para alterar informações. \nDigite (3) para adicionar mais alimentos na sua lista\nDigite (4) para voltar ao menu principal.\n')
                
                if choice2 == '1':
                    print('\nOk... Vamos exibir suas informações!\n')
                    
                    if login_ong in validation_json_ongs:
                        lin()
                        print('Informações da ONG:')
                        print(f'Nome: {validation_json_ongs[login_ong]["nome_ong"]}')
                        print(f'Endereço: {validation_json_ongs[login_ong]["endereco_ong"]}')
                        print(f'Contato: {validation_json_ongs[login_ong]["email_ong"]}')
                        print(f'Alimentos que gostariam de receber: {validation_json_ongs[login_ong]["receber_alimentos"]}')
                        lin()
                    else:
                        print('\nONG não encontrada.\n')
                    
                elif choice2 == '2':
                    print('\nOk... Vamos alterar informações!\n')
                    
                    new_cadaster_ong = validation_json_ongs
                    
                    if login_ong in new_cadaster_ong:
                        print('\nVamos refazer o seu cadastro!\n')
                        
                        current_ong = new_cadaster_ong[login_ong]
                        
                        new_name_ong = input('Digite o novo nome da ONG:\n')
                        current_ong['nome_ong'] = new_name_ong
                        
                        new_address_ong = input('\nDigite o novo endereço:\n')
                        current_ong['endereco_ong'] = new_address_ong
                        
                        new_email_ong= input('\nDigite o novo email:\n')
                        current_ong['email_ong'] = new_email_ong
                        
                        with open('Json/ongs.json', 'w') as file:
                            json.dump(current_ong, file, indent=4)

                        print('\nInformações salvas com sucesso!\n')
                        title(title1='Bem vindo à area para ONGs!')
                        
                elif choice2 =='3':
                    print('\nOk...Vamos adicionar alimentos a sua lista!\n')
                    
                    with open('Json/ongs.json', 'r+') as file2:
                        data_ongs = json.load(file2)
                    
                    
                    if login_ong in data_ongs["ongs_cadastradas"]:
                        lista_ongs = data_ongs["ongs_cadastradas"][login_ong]["receber_alimentos"]
                        
                        loopstring = True
                        while loopstring:
    
                            new_alimento = input('Digite os alimentos que deseja adicionar na lista.\n')
                            if new_alimento.isnumeric():
                                print('\nDigite alimentos.\n')

                            else:
                                lista_ongs.append(new_alimento)
                                loopstring = False
                                print('Salvando...')

                            file.seek(0)  
                            json.dump(data_ongs, file, indent=4)
                            file.truncate()  
                            
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