from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ChecaSePopupApareceu(driver):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(('class name', 'modal-content')))
        palavra = VerificaPalavraPopup(driver)
        botao = AchaBotaoComAPalavra(palavra)
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
    botoes = driver.find_elements_by_class_name('btn')
    for botao in botoes:
        if botao.get_attribute('innerText') == palavra:
            return botao

def ClicaBotaoCerto(botao):
    botao.click()