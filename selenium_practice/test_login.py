from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Enter username
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# Enter password
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# Click login
login = driver.find_element(By.ID, "login-button")
login.click()

time.sleep(3)

# Add product to cart
add_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_cart.click()

time.sleep(2)

# Now cart badge exists
cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

print("Cart items:", cart.text)

time.sleep(3)

driver.quit()