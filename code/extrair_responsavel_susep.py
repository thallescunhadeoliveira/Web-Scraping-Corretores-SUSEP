import pprint
import re
import time
import unicodedata
from datetime import datetime

import numpy as np
import pandas as pd
import requests
import urllib3
from bs4 import BeautifulSoup
from openpyxl.utils.exceptions import IllegalCharacterError


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Definições iniciais
URL = "https://www2.susep.gov.br/safe/menumercado/certidoes/emite_certidoescorretores_2011.asp"
timestamp_inicio = datetime.fromtimestamp(time.time())

def remover_acentos(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

def remove_illegal_chars(value):
    if isinstance(value, str):
        # Remove todos os caracteres de controle ASCII (0-31), exceto \t \n \r
        return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", value)
    return value

def pesquisar_registro(id):

    params = {
        "id": id
    } 
    response = requests.get(URL, params=params, verify=False)

    # Verificando o resultado
    if response.status_code == 200:
        texto_html = BeautifulSoup(response.text, 'html.parser')

    else:
        print(f"Erro {response.status_code}:")
        pprint(response.text)
        texto_html = None
    
    # Retorna o texto encontrado na aba de certidão do corretor
    return texto_html


def extrair_dados(texto, id):

    # Cria dicionário vazio com os dados do corretor
    corretor_dic = {}
    
    try:      
        nome_responsaveis = []
        susep_responsaveis = []
        texto_tabela = texto.find('table').find('table').get_text().split('técnico')[1]
        texto_tabela = remover_acentos(texto_tabela)

        # Regex agora pode ser mais simples (sem letras acentuadas)
        padrao = r'([A-Z ]+?)\s*-\s*(\d{9})'
        resultados = re.findall(padrao, texto_tabela)

        for nome, numero in resultados:
            nome_responsaveis.append(nome.strip())
            susep_responsaveis.append(numero.strip())
        
        #Transforma a lista em string e adiciona ao dicionário
        corretor_dic["id_corretor"] = id
        corretor_dic["nome_responsavel"] = ", ".join(nome_responsaveis)
        corretor_dic["susep_responsavel"] = ", ".join(susep_responsaveis)
    
    except:
        corretor_dic["id_corretor"] = id
        corretor_dic["nome_responsavel"] = "Erro" 
        corretor_dic["susep_responsavel"] = "Erro" 
    
    return corretor_dic


def main():

    # Lendo a lista de corretores a serem pesquisados
    base_susep_parcial = pd.read_csv(r"../data/corretores_susep_parcial.csv")

    ## Caso tenha a base_susep_completa
    ## base_susep_completa = pd.read_csv(r"../data/corretores_susep.csv")

    # Cria lista de ids de corretores
    id_corretores = base_susep_parcial['corretor_id'].to_list()
    total_corretores = len(id_corretores)
    lista_corretores = []
    i = 0

    print(f"Iniciando: {timestamp_inicio}")
    print(f"Total Corretores: {total_corretores}\n")

    # Itera todas elementos da lista de id de corretores
    for id in id_corretores:

        try:
            # Aplica a função de buscar os dados do corretor na susep
            texto_susep = pesquisar_registro(id)
            # Trata os valores do texto_susep
            atributos_corretor = extrair_dados(texto_susep, id)
            
            # Adiciona dicionário na lista de corretores
            lista_corretores.append(atributos_corretor)

            i += 1

            print(f"\n{i}")
            print(f"{(i / total_corretores) * 100:.2f}%".replace('.', ','))
            timestamp = datetime.fromtimestamp(time.time())
            tempo_passado = timestamp - timestamp_inicio
            progresso = i / total_corretores
            tempo_total_estimado = tempo_passado / progresso
            tempo_restante = tempo_total_estimado - tempo_passado
            horario_final_estimado = timestamp + tempo_restante
            horario_final_estimado = horario_final_estimado.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Conclusão Estimada: {horario_final_estimado}")

            
        except:
            pass

        if i % 40 == 0:
            df_corretores_temp = pd.DataFrame(lista_corretores)
            try:
                data_formatada = datetime.fromtimestamp(time.time())
                print(f"Salvando: {data_formatada}")

                df_corretores_temp = df_corretores_temp.applymap(remove_illegal_chars)
                df_corretores_temp.to_csv("../data/validacao_corretores_temp.csv", index=False)

                print()
            except:
                pass
            # Teste
            # break

    timestamp_fim = datetime.fromtimestamp(time.time())
    tempo_total = timestamp_fim - timestamp_inicio
    print(f"Tempo total de Execução: {round(tempo_total)} segundos")

    data_formatada = datetime.fromtimestamp(time.time())
    print(f"Salvando: {data_formatada}")

    df_corretores = df_corretores.applymap(remove_illegal_chars)
    df_corretores.to_csv("../data/validacao_corretores_completo.csv",index=False)


if __name__ == "__main__": 
    main()