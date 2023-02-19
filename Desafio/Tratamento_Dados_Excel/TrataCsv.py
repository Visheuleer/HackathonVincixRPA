import pandas as pd
import csv
from Desafio.Tratamento_Dados_Excel.Classes import Csv
def TrataCsv():
    csv, arquivo_aberto = AbreCsv()
    dados_csv = CriaInstanciaClasseCsv()
    dados_csv = ExtraiDados(csv, dados_csv)
    FechaCsv(arquivo_aberto)
    return dados_csv

def AbreCsv():
    arq = open(r'C:\Users\T-Gamer\Desktop\projetos\HackathonVincixRPA\Arquivos Excel\rpa_hackathon.csv', encoding='utf-8')
    return csv.reader(arq, delimiter=';'), arq

def CriaInstanciaClasseCsv():
    return Csv([], [], [], [], [], [], [])

def ExtraiDados(csv, dados_csv):
    i=0
    for coluna in csv:
        if i!=0:
            dados_csv.primeiro_nome.append(coluna[0])
            dados_csv.sobrenome.append(coluna[1])
            dados_csv.empresa.append(coluna[2])
            dados_csv.cargo.append(coluna[3])
            dados_csv.endereco.append(coluna[4])
            dados_csv.email.append(coluna[5])
            dados_csv.telefone.append(coluna[6])
        i+=1
    return dados_csv

def FechaCsv(arquivo_aberto):
    arquivo_aberto.close()




