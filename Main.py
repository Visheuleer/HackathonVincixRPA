from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Chrome.FormataChrome import DefineOpcoesChrome
from Login.Login import Login
from Desafio.NavegaProDesafio import NavegaProDesafio
from Desafio.ChecaPopup import ChecaSePopupApareceu

try:
    servico = Service(ChromeDriverManager().install())
    opcoes = DefineOpcoesChrome()
    driver = webdriver.Chrome(service=servico, options=opcoes)
    Login(driver)
    NavegaProDesafio(driver)
    ChecaSePopupApareceu(driver)
except(Exception) as err:
    print(f'{type(err)}, {err}')