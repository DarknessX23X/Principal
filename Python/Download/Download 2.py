# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

def search_video(keyword):
    # Inicializa o driver do Selenium (certifique-se de ter o driver do navegador instalado)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    
    # Formata a palavra-chave para a URL
    formatted_keyword = keyword.replace(' ', '+')
    url = f'https://www.youtube.com/results?search_query={formatted_keyword}'

    # Abre a página no navegador
    driver.get(url)
    
    # Espera um tempo para a página carregar completamente
    time.sleep(5)
    
    # Encontra todos os elementos de título dos vídeos
    video_titles = driver.find_elements(By.XPATH,'//a[@id="video-title"]')
    
    # Imprime os nomes dos vídeos encontrados
    if video_titles:
        for video_title in video_titles:
            #print('Título do vídeo:', video_title.text)
            video_link = video_title.get_attribute('href') 
            #print('Link do vídeo:', video_link)       
            with open('C:\\XML\\urls.txt', 'a') as file:
                code = file.write(video_link+'\n')
            
    else:
        print('Nenhum vídeo encontrado para a palavra-chave especificada.')
    
    
    # Fecha o navegador
    driver.quit()
  
# Exemplo de uso
keyword = input('Digite a palavra-chave: ')
search_video(keyword)