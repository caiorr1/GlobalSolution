import formatacao
import main
import json


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

    
def readjson_ongs(login_ong):
    with open ('Json/ongs.json') as file:
        ongs_json = json.load(file)
    
    ongs_way = ongs_json["ongs_cadastradas"]
    ongs_insert = login_ong in ongs_way
    file.close()
    
    return ongs_way, ongs_insert


def insertjson_ongs(login_ong, name_ong, addres_ong, email_ong, password_ong, checkedpassord_ong, recived_alimentos_ong, ongs_way, ongs_insert):
    print(1)


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
    
    insertjson_ongs(login_ong, name_ong, address_ong,email_ong, password_ong, checkedpassord_ong, recived_alimentos_ong, ongs_way, ongs_insert)
    
    print('\nTudo Ok!\n')
    
    formatacao.title(title1='Bem vindo à area para ONGs!')