from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Login(Launch_browser):
    driver=Launch_browser
    driver.find_element(By.ID,"text").click()

