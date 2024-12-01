from selenium import webdriver
from selenium.webdriver.common.by import By

def Check_site():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    text = driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]')
    text2 = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
    button = driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]')
    if text is None and text2 is None and button is None:
        print('Элементы не найдены')
    else:
        print('Элементы найдены')