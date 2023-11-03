from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import streamlit as st

d=0
# Configurar el controlador de Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 30)
# Definir la URL base
url = "https://tienda.exito.com/"
# Crear un DataFrame para almacenar los resultados
df = pd.DataFrame()
# Realizar el inicio de sesión una vez, fuera del bucle
driver.get("https://www.exito.com/login")
time.sleep(3)
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/ul/li[1]/div/button/div/span'))).click()
print('si entro')
time.sleep(2)
usuario_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/form/div[1]/label/div/input")
contrasena_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input")
# Ingresa tu nombre de usuario y contraseña
usuario_input.send_keys("panchaponal18@gmail.com")
contrasena_input.send_keys("Ale13312")
# Envía el formulario de inicio de sesión (puede variar según el sitio)
contrasena_input.send_keys(Keys.RETURN)
time.sleep(5)
wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/div/div/span'))).click()

wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="exito-geolocation-3-x-modalContainer"]/div/div/div[2]/div[1]/div/button[2]/div[2]/div'))).click()
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="exito-geolocation-3-x-modalContainer"]/div/div/div[2]/div[3]/div[3]/button[2]'))).click()
time.sleep(5)

busqueda= driver.find_element(By.XPATH, '//*[@id="downshift-0-input"]')
busqueda.send_keys('COCA COLA')
wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[4]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/label/div/span'))).click()
time.sleep(4)

def scroll_slowly():
    for _ in range(10):  # Ajusta el número de veces que deseas hacer scroll
        driver.execute_script("window.scrollBy(0, 400);")  # Ajusta el valor 100 para controlar la distancia del scroll
        time.sleep(0.5) 
# Navegar a través de las páginas y recopilar datos
scroll_slowly()
time.sleep(4)
productos = driver.find_elements(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')

for producto in productos:
    nombre = producto.find_element(By.CLASS_NAME, 'vtex-store-components-3-x-productBrand').text
    df = pd.concat([df, pd.DataFrame({"nombre": [nombre]})])
    d = d +1
print(d)
st.table(df)
#cambiihhjkfd



    
