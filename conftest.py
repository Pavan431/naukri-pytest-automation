import time
from configparser import ConfigParser

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def Launch_browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(service=service,options=chrome_options)
    browser = webdriver.Chrome()
    config= ConfigParser()
    config.read("config.ini")
    wait = WebDriverWait(browser, 20)
    browser.implicitly_wait(30)
    browser.get(config.get("basic info","url"))
    browser.maximize_window()
    wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Login']"))).click()
    time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Enter your active Email ID / Username"]'))).send_keys(config.get("basic info","username"))
    wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Enter your password"]'))).send_keys(config.get("basic info","password"))
    wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@type="submit"]'))).click()
    time.sleep(10)
    user = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='info__heading']"))).text
    assert user == config.get("basic info","user"), "login failed"
    yield browser
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='nI-gNb-drawer__bars']"))).click()
    browser.find_element(By.LINK_TEXT,"Logout").click()
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Login")))
    browser.quit()