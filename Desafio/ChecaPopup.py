import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def ChecaSePopupApareceu(driver):
    try:
        WebDriverWait(driver, .5).until(EC.presence_of_element_located(('class name', 'modal-content')))
        palavra = VerificaPalavraPopup(driver)
        botao = AchaBotaoComAPalavra(driver, palavra)
        time.sleep(.5)
        ClicaBotaoCerto(botao)
    except(Exception):
        pass

def VerificaPalavraPopup(driver):
    frase = WebDriverWait(driver, 5).until(EC.presence_of_element_located(('xpath', '//*[@id="modal_hackathon"]/div/div/div[2]/p'))).get_attribute('innerText')
    frase = DivideFraseEmPalavra(frase)
    return PegaUltimaPalavra(frase)


def DivideFraseEmPalavra(frase):
    return frase.split()

def PegaUltimaPalavra(frase):
    return frase[-1]

def AchaBotaoComAPalavra(driver, palavra):
    botoes = driver.find_elements(By.CLASS_NAME, 'btn')
    for botao in botoes:
        if botao.get_attribute('innerText') == palavra:
            return botao
    else:
        return WebDriverWait(driver, 5).until(EC.visibility_of_element_located(('class name', 'close')))

def ClicaBotaoCerto(botao):
    botao.click()