
#function for ux
def formatting():
    global form
    form = '-'
    print(form*43)


#useble functions
def companies():
    print('companies')
def ongs():
    print('ongs')
def users():
    print('users')
def admin():
    print('admin')



#program start
if __name__ == '__main__':
    
    formatting()
    print('- Bem vindo ao SeedS, aquecendo corações! -')
    formatting()

loop = True
while loop:
    entrance = int(input(' Digite (1) se você é uma Empresa\n Digite (2) se você é uma ONG\n Digite (3) se você é uma Pessoa Fisíca\n Digite (4) se você é ADMIN\n'))
    choices = [1, 2, 3, 4]
    if entrance not in choices:
        print('\nOpção inválida! Tente novamente\n')   
        continue
    elif entrance in choices[0]:
        print('empresa')