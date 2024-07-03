from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Iniciar el navegador y abrir WhatsApp Web
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

# Esperar a que el usuario escanee el código QR
input("Escanea el código QR y presiona Enter")

# Seleccionar el chat
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys('Silvia')
search_box.send_keys(Keys.ENTER)

# Enviar mensaje automático
message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
message_box.send_keys('Mensaje automático')
message_box.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
