from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#Lines needed to be added in the code
option = Options()
option.add_experimental_option("debuggerAddress","localhost:9222")

# Ruta al archivo de texto que contiene los enlaces
archivo_enlaces = 'lista_canales.txt'

# geckodriver allows you to use emojis, chromedriver does not
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

# Leer los enlaces desde el archivo de texto
with open(archivo_enlaces, 'r') as file:
    enlaces = file.readlines()

# Iterar sobre los enlaces y visitar cada página
for enlace in enlaces:
    # Limpiar los caracteres de nueva línea y espacios en blanco
    enlace = enlace.strip()

    # Navegar a la página
    driver.get(enlace)
    try:
        # Encontrar el elemento del botón por su selector y hacer clic en él
        sleep(2)
        subscribe_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/yt-smartimation/yt-button-shape/button')))
        subscribe_button.click()
    except NoSuchElementException:
        print(f"No se encontró el botón en la página: {enlace}")
    except ElementNotInteractableException:
        print(f"Ya estas suscrito a este canal: {enlace}")
    except TimeoutException:
        # Si el elemento no se encuentra dentro del tiempo de espera, imprimir un mensaje de error
        print("El elemento no se encontró en la página.")

# Cerrar el navegador
driver.quit()