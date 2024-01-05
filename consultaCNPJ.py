import requests


def consulta_cnpj(cnpj):

    url = f'https://minhareceita.org/updated/{cnpj}'

    headers = {
        'Accept': 'application/json'
    }

    response =  requests.get(url, headers=headers)

    if response.status_code == 200:
        cnpj = response.json()
        
        for chave, valor in cnpj.items():
            if valor is None:
                cnpj[chave] = ""
                
        return cnpj
    else:
        print('Erro ao fazer a requisição. Código de status:', response.status_code)


def consulta_data_de_extracao_RF():

    url = 'https://minhareceita.org/updated' 
    
    headers = {
        'Accept': 'application/json'
    }

    response =  requests.get(url, headers=headers)

    if response.status_code == 200:
        resultado = response.json()['message']
        return resultado
    else:
        return f'Erro ao fazer a requisição. Código de status:{response.status_code}'



        
