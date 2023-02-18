import dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Login(driver):
    NavegaPaginaInicial(driver)
    user_name, senha = PegaCredenciais()
    PreencheCredenciais(driver, user_name, senha)
    time.sleep(.5)
    ApertaBotaoLogin(driver)

def NavegaPaginaInicial(driver):
    driver.get('https://www.rpahackathon.co.uk/login')

def PegaCredenciais():
    dotenv.load_dotenv(r'C:\Users\T-Gamer\Desktop\projetos\HackathonVincixRPA\Credenciais\.env')
    return os.getenv('USERNAMEE'), os.getenv('SENHA')

def PreencheCredenciais(driver, user_name, senha):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('name', 'username'))).send_keys(user_name)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('name', 'password'))).send_keys(senha)


def ApertaBotaoLogin(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('class name', 'login-button'))).click()