from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home():

    def __init__(self, driver):
        self.driver=driver

    def select_brand(self, brand):
        self.driver.find_element(By.XPATH,"//*[text()='"+brand+"']").click()
        self.wait_load()

    def get_selected_products(self):
        texts=[]
        for element in self.driver.find_elements(By.XPATH,"//p[@class='shelf-item__title']"):
            texts.append(element.text)
        return texts

    def add_to_cart_by_reference(self, reference):
        self.wait_load()
        self.driver.find_element(By.XPATH,"//p[text()='"+reference+"']/parent::div/div[@class='shelf-item__buy-btn']").click()

    def get_price_by_reference(self, reference):
        self.wait_load()
        return self.driver.find_element(By.XPATH,"//p[text()='"+reference+"']/parent::div/div[@class='shelf-item__price']/div[1]").text
    
    def get_checkout_detail(self, reference):
        self.wait_load()
        return self.driver.find_element(By.XPATH,"//p[@class='title' and text()='"+reference+"']/parent::div/parent::div").text
    
    def click_checkout(self):
        self.wait_load()
        self.driver.find_element(By.XPATH,"//div[text()='Checkout']").click()
    
    
    def wait_load(self):
        self.driver.implicitly_wait(1)
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element((By.XPATH,"//*[@class='spinner lds-ring']")))
        self.driver.implicitly_wait(20)


        