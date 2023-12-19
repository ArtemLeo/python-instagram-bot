from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import login, password
from selenium.webdriver.common.by import By
import time
import random


def hashtag_search(driver, my_login, my_password, hashtag):
    try:
        if driver == "Chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
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
        time.sleep(10)

        # search by hashtag
        try:
            driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)

            for i in range(1, 4):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))

            hrefs = driver.find_elements(By.TAG_NAME, 'a')
            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

            for url in posts_urls:
                try:
                    driver.get(url)
                    time.sleep(3)
                    like_button = driver.find_element(By.XPATH,
                                                      '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
                    like_button.click()
                    time.sleep(random.randrange(80, 100))
                except Exception as ex:
                    print(ex)

            driver.close()
            driver.quit()
        except Exception as ex:
            print(ex)
        driver.close()
        driver.close()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


hashtag_search("Chrome", login, password, 'спортхарьков')
