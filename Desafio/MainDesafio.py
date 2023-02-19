from Desafio.NavegaProDesafio import NavegaProDesafio
from Desafio.ChecaPopup import ChecaSePopupApareceu
import Desafio.Tratamento_Dados_Excel.TrataCsv as csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def MainDesafio(driver):
    NavegaProDesafio(driver)
    dados_csv = csv.TrataCsv()
    for i in range(0, 20):
        if i != 20:
            ChecaSePopupApareceu(driver)
            PreenchePrimeiroNome(driver, dados_csv.primeiro_nome[i])
            PreencheSobrenome(driver, dados_csv.sobrenome[i])
            PreencheNomeEmpresa(driver, dados_csv.empresa[i])
            PreencheEndereco(driver, dados_csv.endereco[i])
            PreencheTelefone(driver, dados_csv.telefone[i])
            PreencheCargo(driver, dados_csv.cargo[i])
            PreencheEmail(driver, dados_csv.email[i])
            ClicaBotaoConfirma(driver)
    else:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('xpath', '/html/body/div/div/div[3]/div[2]/a'))).click()


def PreenchePrimeiroNome(driver, primeiro_nome):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'first_name'))).send_keys(primeiro_nome)

def PreencheSobrenome(driver, sobrenome):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'last_name'))).send_keys(sobrenome)

def PreencheNomeEmpresa(driver, nome_empresa):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'company_name'))).send_keys(nome_empresa)

def PreencheEndereco(driver, endereco):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'address'))).send_keys(endereco)

def PreencheTelefone(driver, telefone):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'phone_number'))).send_keys(telefone)

def PreencheCargo(driver, cargo):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'role_in_company'))).send_keys(cargo)

def PreencheEmail(driver, email):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'email'))).send_keys(email)

def ClicaBotaoConfirma(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('class name', 'btn-success'))).click()