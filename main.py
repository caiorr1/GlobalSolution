import formatacao
import rodarprograma
import doadores.pessoafisica as pessoafisica 
import doadores.ongs as ongs 
import doadores.empresas as empresas
import os


#this function makes the first contact with user, let him choose what way he wants
def main_menu():
    loop = True
    while loop:
        
        entrance = input(' Digite (1) se você é uma Empresa\n Digite (2) se você é uma ONG\n Digite (3) se você é uma Pessoa Fisíca\n Digite (4) se você é ADMIN\n Digite (5) se deseja encerrar o programa\n')
        entrance_list = ['1', '2', '3', '4', '5']
        
        if entrance not in entrance_list:
            print('\nOpção inválida! Tente novamente.\n')   
            
        elif entrance == entrance_list[0]:
            print('\nOk...Indo para cadastro de Empresas.\n')
            empresas.get_companies()
            loop = False
        
        elif entrance == entrance_list[1]:
            print('\nOk...Indo para cadastro de ONGs.\n')  
            ongs.get_ongs()
            loop = False
        
        elif entrance == entrance_list[2]:
            print('\nOk...Indo para cadastro de Pessoas Fisícas.\n')
            pessoafisica.get_natural_person()
            loop = False
            
        elif entrance == entrance_list[3]:
            print('\nOk...Indo para área de Admin\n')
            rodarprograma.admin_run()
            loop = False
            
        elif entrance == entrance_list[4]:
            print('\nOk...Encerrando o programa.\n')
            quit()
            
            
#program start
if __name__ == '__main__':
    
    main_path = './GlobalSolution'
    for root, subFolder, filename in os.walk(main_path):
        for folder in subFolder:
            print(folder)
    
    formatacao.title(title1='- Bem vindo ao SeedS, aquecendo corações! -')
    main_menu()