from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url = "https://www.amazon.com" 
serv = Service(ChromeDriverManager().install()) # Inicializamos el servicio del webdriver para chrome
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get(url)
# Cambiar dependiendo de cuanto tiempo queremos esperar a que la página cargue
driver.implicitly_wait(10)

busqueda = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
busqueda.click()
busqueda.send_keys('audifonos')
busqueda.send_keys(Keys.ENTER)

primerArticulo = driver.find_element(By.XPATH, "//img[@data-image-index='1']")
primerArticulo.click()

alCarrito = driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']")
alCarrito.click()

# Pausa todo el programa para permitir al usuario verificar que se ejecutó correctamente y el artículo se añadió al carrito
sleep(10)
driver.close()
