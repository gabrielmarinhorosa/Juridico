from selenium import webdriver
from selenium.webdriver.chrome.service import Service   
from selenium.webdriver.common.by import By
import time
import pandas as pd


navegador = webdriver.Chrome(service=Service())

navegador.get("https://ww2.trt2.jus.br/")

navegador.maximize_window()

# Espera alguns segundos para garantir que a página carregou
time.sleep(3)

# Localiza o elemento pelo atributo title e clica em "Menu Serviços"
servico = navegador.find_element(By.CSS_SELECTOR, 'a[title="Menu Serviços"]')
servico.click()

time.sleep(2)  # Aguarda o menu abrir

# Localiza e clica em "Consulta Processual"
consulta = navegador.find_element(By.LINK_TEXT, "Consulta Processual")
consulta.click()

primeira_instancia = navegador.find_element(By.LINK_TEXT, "1ª Instância - processos físicos")
primeira_instancia.click()



time.sleep(10)  # Aguarda para visualizar o resultado