import json
from funcoes.formatacao import lin


def match_empresas():
    # Carregar os arquivos JSON
    with open('Json/ongs.json', 'r') as ongs_file:
        ongs_json = json.load(ongs_file)

    with open('Json/empresas.json', 'r') as empresas_file:
        empresas_json = json.load(empresas_file)

    ongs = ongs_json["ongs_cadastradas"]
    empresas = empresas_json["empresas_cadastradas"]

    match_info = []

    for empresa, empresa_dados in empresas.items():
        endereco_empresa = empresa_dados["endereco_empresa"]
        alimentos_a_doar = empresa_dados.get("alimentos_a_doar", [])

        for ong, ong_info in ongs.items():
            endereco_ong = ong_info["endereco_ong"]
            alimentos_a_receber = ong_info.get("alimentos_a_receber", [])

            if set(alimentos_a_doar) & set(alimentos_a_receber):
                match_info.append(
                    {
                        "empresa": empresa,
                        "ong": ong,
                        "endereco_empresa": endereco_empresa,
                        "endereco_ong": endereco_ong,
                        "alimentos_a_doar": alimentos_a_doar,
                        "alimentos_a_receber": alimentos_a_receber,
                    }
                )

    if len(match_info) == 0:
        print("\nNenhum informação cruzada.\n")
    else:
        lin()
        print("Informações cruzadas entre ONGs e Empresas\n")
        for match_info in match_info:
            print("Empresa:", match_info["empresa"])
            print("ONG:", match_info["ong"])
            print("Endereço Empresa:", match_info["endereco_empresa"])
            print("Endereço ONG:", match_info["endereco_ong"])
            print("Alimentos a serem doados:", match_info["alimentos_a_doar"])
            print("Alimentos a serem recebidos:", match_info["alimentos_a_receber"])
            print()
        lin()    
            
                 
def match_pessoafisica():
     # Carregar os arquivos JSON
    with open('Json/ongs.json', 'r') as ongs_file:
        ongs_json = json.load(ongs_file)

    with open('Json/pessoas.json', 'r') as pessoas_file:
        pessoas_json = json.load(pessoas_file)

    ongs = ongs_json["ongs_cadastradas"]
    pessoas = pessoas_json["pessoas_cadastradas"]

    match_info = []

    for pessoa, pessoa_dados in pessoas.items():
        endereco_pessoa = pessoa_dados["endereco_pessoa"]
        alimentos_a_doar = pessoa_dados.get("alimentos_a_doar", [])

        for ong, ong_info in ongs.items():
            endereco_ong = ong_info["endereco_ong"]
            alimentos_a_receber = ong_info.get("alimentos_a_receber", [])

            if set(alimentos_a_doar) & set(alimentos_a_receber):
                match_info.append(
                    {
                        "pessoa": pessoa,
                        "ong": ong,
                        "endereco_pessoa": endereco_pessoa,
                        "endereco_ong": endereco_ong,
                        "alimentos_a_doar": alimentos_a_doar,
                        "alimentos_a_receber": alimentos_a_receber,
                    }
                )

    if len (match_info) == 0:
        print("\nNenhum informação cruzada.\n")
    else:
        lin()
        print("Informações cruzadas entre ONGs e Pessoas Fisicas:\n")
        for match_print in match_info:
            print("Pessoa:", match_print["pessoa"])
            print("ONG:", match_print["ong"])
            print("Endereço Pessoa:", match_print["endereco_pessoa"])
            print("Endereço ONG:", match_print["endereco_ong"])
            print("Alimentos a serem doados:", match_print["alimentos_a_doar"])
            print("Alimentos a serem recebidos:", match_print["alimentos_a_receber"])
            print()
        lin()


