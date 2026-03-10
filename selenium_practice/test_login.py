from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()





time.sleep(5)


driver.quit()