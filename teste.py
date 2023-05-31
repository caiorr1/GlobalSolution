import json

def test():

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
    
    return empresas_insert, senha, senha_confirmada, login, empresas_way, nome_empresa, endereco_empresa, alimentos_doados



def test2(empresas_insert, senha, senha_confirmada, login, empresas_way, nome_empresa, endereco_empresa, alimentos_doados):
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
            
if __name__ == '__main__':
    
    test()
    test2()