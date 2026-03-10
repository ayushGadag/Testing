from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_add_to_cart():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Login
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    # Add product
    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

    # Wait until cart badge appears
    cart = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))
    )

    assert cart.text == "1"

    driver.quit()