from selenium import webdriver
from selenium.webdriver.common.by import By

import time

link="http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME,"first_name")
    input1.send_keys("Edvinas")
    input2 = browser.find_element(By.NAME,"last_name")
    input2.send_keys("Gaidamavicius")
    input3 = browser.find_element(By.CLASS_NAME,"city")
    input3.send_keys("Vilnius")
    input4 = browser.find_element(By.ID,"country")
    input4.send_keys("Lithuania")
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
