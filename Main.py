from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Login.Login import Login

try:
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    Login(driver)
except(Exception) as err:
    print(f'{type(err)}, {err}')