from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Login():

    def __init__(self, driver):
        self.driver=driver

    def set_username(self, username):
        element=self.driver.find_element(By.XPATH,"//*[text()='Select Username']/parent::div//input")
        element.send_keys(username)
        element.send_keys(Keys.ENTER)

    def set_password(self, password):
        element=self.driver.find_element(By.XPATH,"//*[text()='Select Password']/parent::div//input")
        element.send_keys(password)
        element.send_keys(Keys.ENTER)

    def click_login(self):
        element=self.driver.find_element(By.ID,"login-btn")
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(element))
        element.click()
        
    