import formatacao
import main


def get_natural_person():
    formatacao.formatting()
    print('Bem vindo à area de Pessoa Fisíca!')
    formatacao.formatting()
    
    loop = True
    while loop:
        
        choice = input('Digite (1) se deseja se cadastrar.\nDigite (2) se deseja fazer login\nDigite (3) se deseja voltar ao menu principal.\n')
        choice_list = ['1', '2', '3']
        
        if choice not in choice_list:
            print('\nOpção inválida! Tente novamente\n')
            
        elif choice in choice_list[2]:
            print('\nOk...Voltando para o menu principal\n')
            formatacao.formatting()
            print('- Bem vindo ao SeedS, aquecendo corações! -')
            formatacao.formatting()
            main.main_menu()
        #CONTINUAR A OPCAO DE CADASTRO    
        elif choice == choice_list[0]:
            print('CONTINUA')
        #CONTINUAR A OPCAO DE LOGIN
        elif choice == choice_list[1]:
            print('CONTINUA') 