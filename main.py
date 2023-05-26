import formatacao
import rodarprograma
import pessoafisica
import ongs
import empresas

#program start
if __name__ == '__main__':
    
    formatacao.formatting()
    print('- Bem vindo ao SeedS, aquecendo corações! -')
    formatacao.formatting()

loop = True
while loop:
    
    entrance = input(' Digite (1) se você é uma Empresa\n Digite (2) se você é uma ONG\n Digite (3) se você é uma Pessoa Fisíca\n Digite (4) se você é ADMIN\n')
    choices = ['1', '2', '3', '4']
    
    if entrance not in choices:
        print('\nOpção inválida! Tente novamente\n')   
        continue
    
    elif entrance == choices[0]:
        print('\nOk...Indo para cadastro de Empresas.')
        empresas.get_companies()
        loop = False
    
    elif entrance == choices[1]:
        print('\nOk...Indo para cadastro de ONGs')  
        ongs.get_ongs()
        loop = False
    
    elif entrance == choices[2]:
        print('\nOk...Indo para cadastro de Pessoas Fisícas')
        pessoafisica.get_natural_person()
        loop = False
        
    elif entrance == choices[3]:
        print('Ok...Indo para área de Admin')
        rodarprograma.admin_run()
        loop = False