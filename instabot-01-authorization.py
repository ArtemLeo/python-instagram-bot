from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import login, password
from selenium.webdriver.common.by import By
import time
import random


def choose_driver(driver, my_login, my_password):
    if driver == "Chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    try:
        driver.implicitly_wait(5)
        driver.get('https://www.instagram.com')
        time.sleep(random.randrange(2, 5))

        # send login
        login_input = driver.find_element(By.NAME, "username")
        login_input.clear()
        login_input.send_keys(login)
        time.sleep(random.randrange(1, 2))

        # send password
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(random.randrange(1, 2))

        # click button
        auth_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        auth_button.click()
        time.sleep(20)

        # close browser
        driver.close()
        driver.quit()

    except Exception as ex:
        print(ex)
        driver.close()
        driver.close()


choose_driver("Chrome", login, password)
