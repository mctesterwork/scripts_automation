from gettext import find
from operator import truediv
from time import sleep
from turtle import title
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from random import randint

url = "https://www.amazon.com" # Automatizaremos la página de Wikipedia en español
serv = Service(ChromeDriverManager().install()) # Inicializamos el servicio del webdriver para chrome
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)

busqueda = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
busqueda.click()
driver.implicitly_wait(5)

busqueda.send_keys('audifonos')
busqueda.send_keys(Keys.ENTER)
driver.implicitly_wait(5)

tercerArticulo = driver.find_element(By.XPATH, "//img[@data-image-index='3']")
# Estas líneas son por si Selenium falla en hacer scroll hacia el objeto:

#driver.execute_script("arguments[0].scrollIntoView(true)", tercerArticulo)
#driver.implicitly_wait(5)
tercerArticulo.click()
driver.implicitly_wait(5)

alCarrito = driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']")

# Estas líneas son por si Selenium falla en hacer scroll hacia el objeto:

#driver.execute_script("arguments[0].scrollIntoView(true)", alCarrito)
#driver.implicitly_wait(5)
alCarrito.click()


sleep(5)
driver.close()