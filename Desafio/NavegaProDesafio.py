from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def NavegaProDesafio(driver):
    NavegaLevel1(driver)
    ClicaBotaoIniciarLevel(driver)
    SelecionaFerramentaAutomacao(driver)
    BaixaArquivoExcel(driver)
    ClicaBotaoIniciarDesafio(driver)

def NavegaLevel1(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'l1-tab-nav'))).click()

def ClicaBotaoIniciarLevel(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('xpath', '//*[@id="l1-tab"]/div/a'))).click()


def SelecionaFerramentaAutomacao(driver):
    select = Select(WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'rpaSSelect'))))
    select.select_by_visible_text('Other')

def BaixaArquivoExcel(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('class name', 'btn-success'))).click()


def ClicaBotaoIniciarDesafio(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('class name', 'btn-primary'))).click()


