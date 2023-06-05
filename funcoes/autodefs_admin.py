import requests
import json


def send_message(api_key, message):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    data = {
        'messages': [{'role': 'user', 'content': message}]
    }

    response = requests.post(url, json=data, headers=headers)
    result = response.json()

    if 'choices' in result:
        choices = result['choices']
        if len(choices) > 0:
            content = choices[0]['message']['content']
            return content

    return None


def main():
    # Carregar conteúdo dos arquivos JSON
    with open('Json/ongs.json', 'r') as file:
        ongs_json = json.load(file)

    with open('Json/empresas.json', 'r') as file:
        empresas_json = json.load(file)

    with open('Json/pessoas.json', 'r') as file:
        pessoas_json = json.load(file)

    list_empresas_string = json.dumps(empresas_json)
    list_pessoas_string = json.dumps(pessoas_json)
    list_ongs_string = json.dumps(ongs_json)
    # Formatar as mensagens
    
    mensagem_listas = {
    'role': 'user',
    'content': {
        'empresas': list_empresas_string,
        'ongs': list_ongs_string,
        'pessoas': list_pessoas_string
        }
    }

    mensagem_pergunta = {
    'role': 'user',
    'content':{
        'empresas': list_empresas_string,
        'ongs': list_ongs_string,
        'pessoas': list_pessoas_string, 
        'pergunta':'Preciso que você faça o match nas informações das listas. Preciso saber quais ONGs batem com as Empresas e as Pessoas Fisicas. Retorne uma lista no mesmo formato que te enviei.'
        }    
    }


    # Envie as mensagens para a API de chat
    api_key = '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'
    resposta = send_message(api_key, mensagem_pergunta['content'])

    # Processar a resposta da API
    if resposta is not None:
        try:
            match_list = json.loads(resposta)
            print('Resposta do ChatGPT:')
            for match in match_list:
                print(match)
        except json.JSONDecodeError:
            print('Erro: A resposta do ChatGPT não está no formato JSON.')
    else:
        print('Erro: Não foi recebida uma resposta válida do ChatGPT.')


if __name__ == '__main__':
    main()
