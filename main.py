from funcoes.formatacao import title
import funcoes.admin as admin
import Doadores.pessoafisica as pessoafisica 
import Doadores.ongs as ongs 
import Doadores.empresas as empresas
import os
import funcoes.iachat as iachat


def menu_principal():
    loop = True
    while loop:
        
        entrada = input('Digite (1) se você é uma Empresa\nDigite (2) se você é uma ONG\nDigite (3) se você é uma Pessoa Fisíca\nDigite (4) se você é ADMIN\nDigite (5) para conhecer nossa IA\nDigite (6) se deseja encerrar o programa\n')
        lista_entrada = ['1', '2', '3', '4', '5', '6']
        
        if entrada not in lista_entrada:
            print('\nOpção inválida! Tente novamente.\n')   
            
        elif entrada == lista_entrada[0]:
            print('\nOk...Indo para cadastro de Empresas.\n')
            empresas.empresas()
            loop = False
        
        elif entrada == lista_entrada[1]:
            print('\nOk...Indo para cadastro de ONGs.\n')  
            ongs.ongs()
            loop = False
        
        elif entrada == lista_entrada[2]:
            print('\nOk...Indo para cadastro de Pessoas Fisícas.\n')
            pessoafisica.pessoasnaturais()
            loop = False
            
        elif entrada == lista_entrada[3]:
            print('\nOk...Indo para área de Admin\n')
            admin.admin_run()
            loop = False
            
        elif entrada == lista_entrada[4]:
            print('\nOk...Indo para área da IA.\n')
            iachat.integracao_gpt()
            
        elif entrada == lista_entrada[5]:
            print('\nOk...Encerrando o programa.\n')
            quit()
            
            

if __name__ == '__main__':
    
    
    
    title(title1='- Bem vindo ao SeedS, aquecendo corações! -')
    menu_principal()
