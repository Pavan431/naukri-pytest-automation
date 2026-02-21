import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

def test_Login(Launch_browser):
    driver=Launch_browser
    driver.find_element(By.XPATH,"//div[@class='nI-gNb-drawer__bars']").click()
    driver.find_element(By.LINK_TEXT,"View & Update Profile").click()
    wait=WebDriverWait(driver,30)
    wait.until(EC.presence_of_element_located((By.XPATH,"(//span[text()='Resume headline'])[1]"))).click()
    driver.find_element(By.XPATH,"//span[text()='Resume headline']/following-sibling::span[text()='editOneTheme']").click()
    headline_box= wait.until(EC.visibility_of_element_located((By.XPATH,"//textarea[@id='resumeHeadlineTxt']")))
    headline_text= headline_box.text
    print(headline_text)
    headline_box.click()
    headline_box.send_keys(Keys.CONTROL,"a")
    headline_box.send_keys(Keys.DELETE)
    headline_box.send_keys(headline_text)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//button[text()='Save']"))).click()
    #time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Profile updated successfully']")))
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()


