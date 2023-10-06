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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 30)
url = "https://www.exito.com/mercado/vinos-y-licores"
driver.get(url)
df = pd.DataFrame()
time.sleep(3)
# Esperar a que la página se cargue completamente
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="exito-geolocation-3-x-modalContainer"]/div/div/div[2]/div[1]/div/button[2]/div[2]/div'))).click()
usuario_input = driver.find_element(By.XPATH, '//*[@id="requestemail-input"]')
usuario_input.send_keys("panchaponal18@gmail.com")
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="exito-geolocation-3-x-modalContainer"]/div/div/div[2]/div[3]/div[3]/div/button'))).click()



