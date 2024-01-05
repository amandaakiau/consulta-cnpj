from consultaCNPJ import *

while True:

    input_opcao = input("""
    ########### Consulta de CNPJ ###########

                1 - Informações completas
                2 - Informações resumidas 
                3 - Sair
                        
                Digite o número da opção desejada: """)



    if input_opcao == '1' or input_opcao == '2':
        
        input_cnpj = input("""
                Insira aqui o CNPJ: """)
        
        cnpj = consulta_cnpj(input_cnpj)
        data_de_extracao_RF = consulta_data_de_extracao_RF()
            
        if input_opcao == '1':
            print(cnpj)
            print(data_de_extracao_RF)
        else:
            info = {
            'cep': cnpj['cep'],
            'uf': cnpj['uf'],
            'municipio': cnpj['municipio'],
            'bairro': cnpj['bairro'],
            'logradouro': cnpj['logradouro'],
            'numero': cnpj['numero'],
            'complemento': cnpj['complemento'],
            'email': cnpj['email'],
            'razao_social': cnpj['razao_social'],
            'nome_fantasia': cnpj['nome_fantasia'],
            'ddd_telefone_1': cnpj['ddd_telefone_1'],
            'ddd_telefone_2': cnpj['ddd_telefone_2'],
            'codigo_municipio': cnpj['codigo_municipio'],
            'codigo_municipio_ibge': cnpj['codigo_municipio_ibge']
            }

            print(info)
            print(data_de_extracao_RF)

    elif input_opcao == '3':
        break;
    else:
        print("\n Digite uma das opções listadas.")



