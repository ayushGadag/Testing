from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username = driver.find_element(By.ID, "user-name")

username.send_keys("gunesh")

pass_word = driver.find_element(By.ID,"password")
pass_word.send_keys("123")


time.sleep(5)


driver.quit()