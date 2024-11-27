from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#поиск элемента
text = driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]')
if text is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

text2 = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
if text2 is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

button = driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]')
if button is None:
    print('Элемент не найден')
else:
    print('Элемент найден')