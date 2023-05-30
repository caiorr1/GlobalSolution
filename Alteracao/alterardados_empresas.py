import sys
import json
sys.path.append('./../RodandoUser')
from RodandoUser import empresas

def change_empresas(login):
    
    with open('./../Json/empresas.json') as file:
        empresas_json = json.load(file)
       
    user_inside_json = empresas_json['empresas_cadastradas'][login]
    print('Olá')