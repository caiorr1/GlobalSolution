from funcoes.formatacao import lin, title
import funcoes.autodefs_admin as autodefs_admin
import funcoes.autodefs_empresas as autodefs_empresas

def admin_run():
    title(title1='Bem vindo à area de Admin!')
    
    loop = True
    while loop:
        
        choice = input('Digite (1) se deseja dar match nas listas.\nDigite (2) se deseja voltar ao menu.\n')
        
        if choice != '1' and choice != '2':
            print('\nOpção inválida! Tente novamente\n')
            
        elif choice == '2':
            autodefs_empresas.go_to_menu()
            
        elif choice == '1':
            print('\nOk... Enviando as listas!\n')
            autodefs_admin.encontrar_coincidencias_empresas_ongs()
            autodefs_admin.encontrar_coincidencias_pf_ong()