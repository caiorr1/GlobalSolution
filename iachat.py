import requests
import json
from funcoes.senha import api_key

def send_to_gpt():
    URL = "https://api.openai.com/v1/chat/completions"

    api_key = api_key

    with open('Json/ongs.json', 'r') as file:
        ongs_json = json.load(file)

    with open('Json/empresas.json', 'r') as file:
        empresas_json = json.load(file)

    with open('Json/pessoas.json', 'r') as file:
        pessoas_json = json.load(file)
        
    list_empresas_string = json.dumps(empresas_json)
    list_pessoas_string = json.dumps(pessoas_json)
    list_ongs_string = json.dumps(ongs_json)


    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"I need you to match the lists I'm going to send you, reorganize if necessary. Consider only food to be donated by individuals and by companies and the address. By ONGs, consider the food to be received and the address. I need you to compare them and let me know the match between them, return me an entire text"},
                {"role": "user", "content": f"The lists are as follows {list_empresas_string},{list_ongs_string},{list_pessoas_string} "}],
    "temperature" : 1.0,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(URL, headers=headers, json=payload, stream=False)
        

    print(response.content)