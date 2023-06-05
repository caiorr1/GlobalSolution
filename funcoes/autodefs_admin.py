import json
from funcoes.formatacao import lin


def encontrar_coincidencias_empresas_ongs():
    # Carregar os arquivos JSON
    with open('Json/ongs.json', 'r') as ongs_file:
        ongs_json = json.load(ongs_file)

    with open('Json/empresas.json', 'r') as empresas_file:
        empresas_json = json.load(empresas_file)

    ongs = ongs_json["ongs_cadastradas"]
    empresas = empresas_json["empresas_cadastradas"]

    coincidencias = []

    for empresa, empresa_info in empresas.items():
        endereco_empresa = empresa_info["endereco_empresa"]
        alimentos_doados = empresa_info.get("alimentos_doados", [])

        for ong, ong_info in ongs.items():
            endereco_ong = ong_info["endereco_ong"]
            alimentos_recebidos = ong_info.get("receber_alimentos", [])

            if set(alimentos_doados) & set(alimentos_recebidos):
                coincidencias.append(
                    {
                        "empresa": empresa,
                        "ong": ong,
                        "endereco_empresa": endereco_empresa,
                        "endereco_ong": endereco_ong,
                        "alimentos_doados": alimentos_doados,
                        "alimentos_recebidos": alimentos_recebidos,
                    }
                )

    if len(coincidencias) == 0:
        print("\nNenhuma coincidência encontrada.\n")
    else:
        lin()
        print("Coincidências entre ONGs e Empresas encontradas:\n")
        for coincidencia in coincidencias:
            print("Empresa:", coincidencia["empresa"])
            print("ONG:", coincidencia["ong"])
            print("Endereço Empresa:", coincidencia["endereco_empresa"])
            print("Endereço ONG:", coincidencia["endereco_ong"])
            print("Alimentos a serem doados:", coincidencia["alimentos_doados"])
            print("Alimentos a serem recebidos:", coincidencia["alimentos_recebidos"])
            print()
        lin()    
            
                 
def encontrar_coincidencias_pf_ong():
     # Carregar os arquivos JSON
    with open('Json/ongs.json', 'r') as ongs_file:
        ongs_json = json.load(ongs_file)

    with open('Json/pessoas.json', 'r') as pessoas_file:
        pessoas_json = json.load(pessoas_file)

    ongs = ongs_json["ongs_cadastradas"]
    pessoas = pessoas_json["pessoas_cadastradas"]

    coincidencias = []

    for pessoa, pessoa_info in pessoas.items():
        endereco_pessoa = pessoa_info["endereco_pessoa"]
        alimentos_doados = pessoa_info.get("alimentos_doados", [])

        for ong, ong_info in ongs.items():
            endereco_ong = ong_info["endereco_ong"]
            alimentos_recebidos = ong_info.get("receber_alimentos", [])

            if set(alimentos_doados) & set(alimentos_recebidos):
                coincidencias.append(
                    {
                        "pessoa": pessoa,
                        "ong": ong,
                        "endereco_pessoa": endereco_pessoa,
                        "endereco_ong": endereco_ong,
                        "alimentos_doados": alimentos_doados,
                        "alimentos_recebidos": alimentos_recebidos,
                    }
                )

    if len(coincidencias) == 0:
        print("\nNenhuma coincidência encontrada.\n")
    else:
        lin()
        print("Coincidências entre ONGs e Pessoas Fisicas encontradas:\n")
        for coincidencia in coincidencias:
            print("Pessoa:", coincidencia["pessoa"])
            print("ONG:", coincidencia["ong"])
            print("Endereço Pessoa:", coincidencia["endereco_pessoa"])
            print("Endereço ONG:", coincidencia["endereco_ong"])
            print("Alimentos a serem doados:", coincidencia["alimentos_doados"])
            print("Alimentos a serem recebidos:", coincidencia["alimentos_recebidos"])
            print()
        lin()


