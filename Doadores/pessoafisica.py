from formatacao import lin, title
import main
import funcoes.autodefs_pessoafisica as autodefs_pessoafisica

def get_natural_person():
    lin()
    print('Bem vindo à area de Pessoa Fisíca!')
    lin()
    
    loop = True
    while loop:
        
        choice = input('Digite (1) se deseja se cadastrar.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        choice_list = ['1', '2', '3']
        
        if choice not in choice_list:
            print('\nOpção inválida! Tente novamente\n')
            
        elif choice in choice_list[2]:
            print('\nOk...Voltando para o menu principal\n')
            lin()
            print('- Bem vindo ao SeedS, aquecendo corações! -')
            lin()
            main.main_menu()
        #CONTINUAR A OPCAO DE CADASTRO    
        elif choice == choice_list[0]:
            autodefs_pessoafisica.make_register_pessoa()
       
        #CONTINUAR A OPCAO DE LOGIN
        elif choice == choice_list[1]:
            validation_json_pessoas = autodefs_pessoafisica.loadjson_pessoas()
            autodefs_pessoafisica.make_login_pessoa(validation_json_pessoas)