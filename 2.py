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

# Configurar el controlador de Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 30)
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
time.sleep(3)
wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/div/div/span'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="exito-geolocation-3-x-modalContainer"]/div/div/div[2]/div[1]/div/button[2]/div[2]/div'))).click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="exito-geolocation-3-x-modalContainer"]/div/div/div[2]/div[3]/div[3]/button[2]'))).click()
