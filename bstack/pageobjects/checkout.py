from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Checkout():

    def __init__(self, driver):
        self.driver=driver

    def get_total_price(self):
        element=self.driver.find_element(By.XPATH,"//*[@class='cart-priceItem-value']")
        return element.text


        
    