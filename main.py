from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time


# Initiate Chrome browser and get url
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

# select English as langauge
a = ActionChains(driver)
driver.implicitly_wait(10)
language = driver.find_element(By.ID, "langSelect-EN").click()

# Identify clickable objects
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')


# cookie balance checker
def cookie_balance():
    cookie_retrieval = driver.find_element(By.XPATH, '//*[@id="cookies"]').get_attribute('innerHTML')
    comma_remove = cookie_retrieval.replace(",", "")
    return int(comma_remove.split(" ", maxsplit=1)[0])


# automated add-on purchaser
def check_purchase():
    balance = cookie_balance()

    try:
        bank_comma = driver.find_element(By.XPATH, '//*[@id="productPrice4"]').get_attribute('innerHTML')
        bank_price = int(bank_comma.replace(",", ""))
        if balance <= bank_price:
            bank = driver.find_element(By.XPATH, '//*[@id="product3"]')
            webdriver.ActionChains(driver).move_to_element(bank).click(bank).perform()
    except StaleElementReferenceException:
        pass

    try:
        factory_comma = driver.find_element(By.XPATH, '//*[@id="productPrice3"]').get_attribute('innerHTML')
        factory_price = int(factory_comma.replace(",", ""))
        if balance >= factory_price:
            factory = driver.find_element(By.XPATH, '//*[@id="product3"]')
            webdriver.ActionChains(driver).move_to_element(factory).click(factory).perform()
    except StaleElementReferenceException:
        pass

    try:
        farm_comma = driver.find_element(By.XPATH, '//*[@id="productPrice2"]').get_attribute('innerHTML')
        farm_price = int(farm_comma.replace(",", ""))
        if balance >= farm_price:
            farm = driver.find_element(By.XPATH, '//*[@id="product2"]')
            webdriver.ActionChains(driver).move_to_element(farm).click(farm).perform()
    except StaleElementReferenceException:
        pass

    try:
        grandma_comma = driver.find_element(By.XPATH, '//*[@id="productPrice1"]').get_attribute('innerHTML')
        grandma_price = int(grandma_comma.replace(",", ""))
        if balance >= 2 * grandma_price:
            grandma = driver.find_element(By.XPATH, '//*[@id="product1"]')
            webdriver.ActionChains(driver).move_to_element(grandma).click(grandma).perform()
    except StaleElementReferenceException:
        pass

    try:
        cursor_comma = driver.find_element(By.XPATH, '//*[@id="productPrice0"]').get_attribute('innerHTML')
        cursor_price = int(cursor_comma.replace(",", ""))
        if balance >= 2 * cursor_price:
            cursor = driver.find_element(By.XPATH, '//*[@id="product0"]')
            webdriver.ActionChains(driver).move_to_element(cursor).click(cursor).perform()
    except StaleElementReferenceException:
        pass


# automated cookie clicker
def cookie_click():
    start = time.time()
    max_time = 5
    elapsed = 0
    while max_time > elapsed:
        cookie.click()
        elapsed = time.time() - start
    check_purchase()
    cookie_click()


# run the program
cookie_click()
