from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

def set_app(app):
    desired_caps = {}
    desired_caps["app"] = app
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities= desired_caps)
    return driver


def test_sum():
    driver= set_app("Microsoft.WindowsCalculator_8wekyb3d8bbwe!App")
    driver.find_element(By.NAME,"One").click()
    driver.find_element(By.NAME,"Plus").click()
    driver.find_element(By.NAME,"Seven").click()
    driver.find_element(By.NAME,"Equals").click()
    assert getresults(driver) == "8"
    driver.quit()

def test_click():
    driver= set_app("Microsoft.WindowsCalculator_8wekyb3d8bbwe!App")
    driver.find_element(By.XPATH,"//*[@AutomationId='num1Button']").click()
    driver.find_element(By.XPATH,"//*[@AutomationId='num1Button']").click()
    driver.find_element(By.XPATH,"//*[@AutomationId='num1Button']").click()
    driver.find_element(By.XPATH,"//*[@AutomationId='num1Button']").click()    
    driver.quit()

def getresults(driver):
        displaytext = driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("Display is " )
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext