import time
from configparser import ConfigParser

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.fixture(scope="function")
def Launch_browser():
    browser=webdriver.Chrome()
    config= ConfigParser()
    config.read("config.ini")
    wait = WebDriverWait(browser, 20)
    browser.implicitly_wait(30)
    browser.get(config.get("basic info","url"))
    browser.maximize_window()
    browser.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(10)

    wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Enter your active Email ID / Username"]'))).send_keys(config.get("basic info","username"))
    wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Enter your password"]'))).send_keys(config.get("basic info","password"))
    wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@type="submit"]'))).click()
    time.sleep(10)
    user = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='info__heading']"))).text
    assert user == config.get("basic info","user"), "login failed"


Launch_browser()