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

# Configurar el controlador de Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 30)
# Definir la URL base
base_url = "https://www.exito.com/mercado/vinos-y-licores/aguardiente/cervezas/ron/whisky?fuzzy=0&initialMap=c,c&initialQuery=mercado/vinos-y-licores&map=category-1,category-2,category-3,category-3,category-3,category-3&operator=and&order=OrderByBestDiscountDESC&page="
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
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="exito-geolocation-3-x-modalContainer"]/div/div/div[2]/div[1]/div/button[2]/div[2]/div'))).click()
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="exito-geolocation-3-x-modalContainer"]/div/div/div[2]/div[3]/div[3]/button[2]'))).click()


def scroll_slowly():
    for _ in range(10):  # Ajusta el número de veces que deseas hacer scroll
        driver.execute_script("window.scrollBy(0, 400);")  # Ajusta el valor 100 para controlar la distancia del scroll
        time.sleep(0.5) 
# Navegar a través de las páginas y recopilar datos
for page_num in range(1, 3):  # Cambia 11 a la página deseada + 1
    url = base_url + str(page_num)
    driver.get(url)
    time.sleep(10)
    scroll_slowly()  # Asumiendo que esta función sigue presente
    
    # Esperar a que aparezcan todos los productos (página cargada completamente)
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')))

    productos = driver.find_elements(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')

    for producto in productos:
        nombre = producto.find_element(By.XPATH, './/h3/span').text
        try:
            print("entrando al try")
            precio_antes = producto.find_element(By.CLASS_NAME, 'exito-vtex-components-4-x-currencyContainer').text
            descuento = producto.find_element(By.XPATH, '//*[@id="gallery-layout-container"]/div[2]/section/a/article/div[3]/div[2]/div/div/div/div[1]/div/div/div[4]/div[2]/div/div/div/div/div/div/div[1]/div/div/div').text
            medio_pago = producto.find_element(By.XPATH, './/div[contains(@class, "payment-methods")]/span').text
            mi_desc = producto.find_element(By.XPATH,'//*[@id="gallery-layout-container"]/div[2]/section/a/article/div[1]/div/div[1]/div/div[2]/img')
            mi_Desc = mi_desc.get_attribute("src")
        except:
            precio_antes = 'N/A'
            descuento = 'N/A'
            medio_pago = 'N/A'
            mi_Desc = 'N/A'
        
        precio_actual = producto.find_element(By.XPATH, './/div[contains(@class, "price")]/div/span').text
        imagen = producto.find_element(By.XPATH, '//*[@id="gallery-layout-container"]/div[5]/section/a/article/div[3]/div[1]/div/img')
        img = imagen.get_attribute("src")
        
        df = pd.concat([df, pd.DataFrame({"nombre": [nombre], 
                                          "Precio_Antes": [precio_antes],
                                          "Medio_Pago": [medio_pago],
                                          "Descuento": [descuento],
                                          "Precio_Actual": [precio_actual],
                                          "Imagen": [img],
                                          "Mi_Descuento": [mi_Desc]})], ignore_index=True)

# Imprimir el DataFrame con todos los nombres de productos
st.table(df)

# Cerrar el navegador después de la extracción de datos
driver.quit()
