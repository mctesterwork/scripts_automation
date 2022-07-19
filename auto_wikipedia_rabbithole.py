from gettext import find
from operator import truediv
from time import sleep
from turtle import title
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from random import randint

url = "https://es.wikipedia.org" # Automatizaremos la página de Wikipedia en español
serv = Service(ChromeDriverManager().install()) # Inicializamos el servicio del webdriver para chrome
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
patron = "/wiki/"

while(not "Cola" in driver.title):
    driver.implicitly_wait(5)
    numeroAleatorio = randint(12, 18)
    listaEnlaces = driver.find_elements(By.XPATH, "//a[starts-with(@href,'/wiki/')]") # Busca todos los enlaces válidos
    listaEnlaces[numeroAleatorio].click()
            
sleep(10) # Solo para depuración
driver.close()