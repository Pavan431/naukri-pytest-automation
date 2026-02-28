import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

@pytest.mark.update
def test_Login(Launch_browser):
    driver=Launch_browser
    driver.find_element(By.XPATH,"//div[@class='nI-gNb-drawer__bars']").click()
    driver.find_element(By.LINK_TEXT,"View & Update Profile").click()
    wait=WebDriverWait(driver,30)
    wait.until(EC.presence_of_element_located((By.XPATH,"(//span[text()='Resume headline'])[1]"))).click()
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Resume headline']/following-sibling::span[text()='editOneTheme']"))).click()
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

def scroll_until_element(driver, xpath, timeout=25):

    wait = WebDriverWait(driver, 1)
    end_time = time.time() + timeout

    while True:
        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return element
        except:
            driver.execute_script("window.scrollBy(0,400);")
            time.sleep(1)

        if time.time() > end_time:
            raise Exception("Element not found after scrolling")


def test_apply_new_roles(Launch_browser):
    driver = Launch_browser
    wait= WebDriverWait(driver,30)
    try:
        # open early access roles
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
        view_option = wait.until(EC.visibility_of_element_located((
            By.XPATH,
            "//span[contains(.,'Early access roles')]/ancestor::div[contains(@class,'spc__header')]//a[contains(@class,'spc__view-all')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", view_option)
        driver.execute_script("arguments[0].click();", view_option)
        assert view_option.is_displayed(), "element not visible"


        #view_option.click()

        # wait roles page

    except Exception as e:
        print("No early access roles available now", e)

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Share interest']")
    ))
    '''
    i = 0
    while True:

        roles = driver.find_elements(By.XPATH, "//button[normalize-space()='Share interest']")

        if i >= len(roles):
            break

        roles[i].click()

        # success popup
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(.,'Interest shared successfully')]")
        ))

        driver.back()

        # IMPORTANT → wait page reload
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Share interest']")
        ))

        i += 1

    '''
    while True:
        roles = driver.find_elements(By.XPATH, "//button[normalize-space()='Share interest']")
        total_roles = len(roles)
        if total_roles==0:
            break
        roles[0].click()
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Interest shared successfully!']")))
        driver.back()
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        #wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share interest']")))
