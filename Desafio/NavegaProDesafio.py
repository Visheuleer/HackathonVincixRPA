from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


def NavegaProDesafio(driver):
    NavegaLevel1(driver)
    ClicaBotaoIniciarDesafio(driver)
    SelecionaFerramentaAutomacao(driver)
    BaixaArquivoExcel(driver)

def NavegaLevel1(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'l1-tab-nav'))).click()

def ClicaBotaoIniciarDesafio(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('xpath', '//*[@id="l1-tab"]/div/a'))).click()


def SelecionaFerramentaAutomacao(driver):
    select = Select(WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('id', 'rpaSSelect'))))
    select.select_by_visible_text('Other')

def BaixaArquivoExcel(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(('class name', 'btn-success'))).click()
    time.sleep(10)

