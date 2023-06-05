import requests
import json
from funcoes.formatacao import title
import main


def go_to_menu():
    print('\nOk...Voltando para o menu principal\n')
    title(title1='- Bem vindo ao SeedS, aquecendo corações! -')
    main.menu_principal()


def integracao_gpt():
    
    with open('funcoes/api_key.txt', 'r') as file:
        api_key = file.read().strip()
    
    URL = "https://api.openai.com/v1/chat/completions"

    title(title1='- Bem Vindo a área da Inteligência Artificial! -')
    loop = True
    while loop:
        choice = input('\nDigite (1) se deseja descobrir o melhor alimento para ser plantado em um ambiente específico de sua escolha.\nDigite (2) se deseja descobrir o melhor local para ser plantado um alimento específico de sua escolha.\nDigite (3) se deseja saber mais sobre agricultura sustentável.\nDigite (4) para voltar ao menu principal.\n')

        choice_list = ['1', '2', '3', '4']
        if choice not in choice_list:
            print('\nOpção Inválida. Digite novamente.\n')
            continue

        elif choice == choice_list[0]:
            ambiente_user = input("\nDigite o lugar que você gostaria de plantar. Especifique sobre condições climáticas, contato com a iluminação natural, etc. Toda e qualquer tipo de informação que pode ajudar a nossa IA a entender o ambiente:\n")
            mensagem_para_gpt = [{"role": "user", "content": f"Qual o alimento mais viável para ser plantado no local: {ambiente_user}"}]

        elif choice == choice_list[1]:
            alimento_user = input("\nDigite o alimento que gostaria de plantar e a nossa IA falará o melhor ambiente para ser plantado:\n")
            mensagem_para_gpt = [{"role": "user", "content": f"Qual o melhor local para ser plantado {alimento_user}"}]

        elif choice == choice_list[2]:
            agri_sustentavel = input("\nVocê quer saber o que é agricultura sustentável? Digite (S) para sim ou (N) para não.\n")
            if agri_sustentavel.upper() == 'S':
                mensagem_para_gpt = [{"role": "user", "content": "O que é agricultura sustentável? Explique e me de exemplos."}]
            else:
                print('\nOk... Indo para o menu principal!\n')
                go_to_menu()
                break

        elif choice == choice_list[3]:
            print('\nOk... Indo para o menu principal!\n')
            go_to_menu()
            break

        payload = {
            "model": "gpt-3.5-turbo",
            "messages": mensagem_para_gpt,
            "temperature": 1.0,
            "top_p": 1.0,
            "n": 1,
            "stream": False,
            "presence_penalty": 0,
            "frequency_penalty": 0,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(URL, headers=headers, json=payload)
        dados_reposta = json.loads(response.content)

        # Acessar a resposta da API e corrigir o texto truncado
        resposta_definitiva = dados_reposta['choices'][0]['message']['content']
        resposta_definitiva = resposta_definitiva.replace('\n', '')

        print(f'\nSeedS: {resposta_definitiva}\n')
        title(title1='- Bem Vindo a área da Inteligência Artificial! -')

