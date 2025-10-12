import requests
from pprint import pprint
import urllib3
import time
from datetime import datetime, timedelta
import pandas as pd
import re

# Configurações
URL = "https://www2.susep.gov.br/safe/corretoresapig/dadospublicos/pesquisar"
PARTIAL_SAVE = 40 # Salva incrementalmente a cada x requisições
PARTIAL_OUTPUT_CSV = "../data/corretores_susep_parcial.csv" 
FINAL_OUTPUT_CSV = "../data/corretores_susep.csv" 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Funções Auxiliares
def remove_illegal_chars(value):
    if isinstance(value, str):
        # Remove todos os caracteres de controle ASCII (0-31), exceto \t \n \r
        return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", value)
    return value

def main():
    start = datetime.fromtimestamp(time.time())
    i = 1
    corretor_id = []
    cnpj = []
    numero_susep = []
    nome = []
    recadastrado = []
    situacao = []
    produtos = []
    pagina = []
    criado = []
    tabela_corretores = pd.DataFrame()
    wait_time = {}

    while True:
        print(f"\nIniciando Extração na página {i}")
        # Filtra apenas cadastros de Pessoa Jurídica. (Para pessoa física usar "PF")
        params = {
            "tipoPessoa": "PJ",
            "page": i
        }
        # Fazendo a requisição
        response = requests.get(URL, params=params,verify=False)

        # Verificando o resultado
        if response.status_code == 200:
            data = response.json()

        # Em caso de resposta negada por Too Many Requests
        elif response.status_code == 429:
            # inicializa tempo de espera se não existir
            try:
                wait_time[i] = wait_time[i]
            except:
                wait_time[i] = 5

            if wait_time[i]  > 300:
                print(f"Tentamos muitas vezes mas não conseguimos buscar o dado da página {i}")
                i += 1
                continue

            print(f"Erro {response.status_code} na página {i}.")
            print(f"Aguardando {wait_time[i]} segundos antes de tentar novamente...")
            time.sleep(wait_time[i])
            # Incrementamos o tempo de espera dessa requisição
            wait_time[i] = wait_time[i] * 2
            continue

        else:
            print(f"Erro {response.status_code}:")
            pprint(response.text)

        registros = data['retorno']['registros']
        total_registros = data['retorno']['totalRegistros']
        # Cada página retorna 25 corretores
        print(f"{i*25} corretores registrados de {total_registros}. {(i*25/total_registros):.4f}% Concluído")

        if not registros:
            print("Final do código.")
            break

        for corretor in registros:
            corretor_id.append(corretor.get('corretorId'))
            cnpj.append(corretor.get('cpfCnpj'))
            numero_susep.append(corretor.get('protocolo'))
            nome.append(corretor.get('nome'))
            recadastrado.append(corretor.get('recadastrado'))
            situacao.append(corretor.get('situacao'))
            produtos.append(corretor.get('produtos'))
            pagina.append(i)

            dt = datetime.fromtimestamp(time.time())
            data_formatada = dt.strftime("%Y-%m-%d %H:%M:%S")
            criado.append(data_formatada)

        timestamp = datetime.fromtimestamp(time.time())
        # Formata como string
        data_formatada = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Horário Término Extração: {data_formatada}")


        tempo_passado = timestamp - start
        progresso = i * 25 / total_registros
        tempo_total_estimado = tempo_passado / progresso
        tempo_restante = tempo_total_estimado - tempo_passado
        horario_final_estimado = timestamp + tempo_restante
        horario_final_estimado = horario_final_estimado.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Conclusão Estimada: {horario_final_estimado}")

        i += 1
        
        if i % PARTIAL_SAVE == 0:
            tabela_corretores_temp = pd.DataFrame()
            tabela_corretores_temp["corretor_id"] = corretor_id
            tabela_corretores_temp["cnpj"] = cnpj
            tabela_corretores_temp["numero_susep"] = numero_susep
            tabela_corretores_temp["nome"] = nome
            tabela_corretores_temp["recadastrado"] = recadastrado
            tabela_corretores_temp["situacao"] = situacao
            tabela_corretores_temp["produtos"] = produtos
            tabela_corretores_temp["pagina"] = pagina
            tabela_corretores_temp["criado"] = criado
            
            tabela_corretores_temp = tabela_corretores_temp.applymap(remove_illegal_chars)

            # Caso prefira salvar em .xlsx
            #tabela_corretores_temp.to_excel('../data/corretores_susep_parcial.xlsx', index = False)
            tabela_corretores_temp.to_csv(PARTIAL_OUTPUT_CSV, index = False)

            timestamp = time.time()
            # Converte para datetime
            dt = datetime.fromtimestamp(timestamp)

            # Formata como string
            data_formatada = dt.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Salvo: {data_formatada}")
    
    tabela_corretores["corretor_id"] = corretor_id
    tabela_corretores["cnpj"] = cnpj
    tabela_corretores["numero_susep"] = numero_susep
    tabela_corretores["nome"] = nome
    tabela_corretores["recadastrado"] = recadastrado
    tabela_corretores["situacao"] = situacao
    tabela_corretores["produtos"] = produtos
    tabela_corretores["pagina"] = pagina
    tabela_corretores["criado"] = criado

    tabela_corretores = tabela_corretores.applymap(remove_illegal_chars)

    # Caso prefira salvar em .xlsx
    #tabela_corretores.to_excel('../data/corretores_susep.xlsx', index = False)
    tabela_corretores.to_csv(FINAL_OUTPUT_CSV, index = False)

    end = datetime.fromtimestamp(time.time())    
    print(f"Duração de {end - start:.2f} segundos.")

if __name__ == "__main__":
    main()