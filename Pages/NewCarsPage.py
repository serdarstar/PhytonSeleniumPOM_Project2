from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class NewCarsPage(BasePage):
    hyundai_XPATH = "//div[normalize-space()='Hyundai']"
    Bmw_XPATH = "//div[normalize-space()='BMW']"
    honda_XPATH = "//div[normalize-space()='Honda']"
    toyota_XPATH = "//div[normalize-space()='Toyota']"

    def __init__(self, driver):
        super().__init__(driver)

    def selectHyundai(self):
        self.click(By.XPATH, self.hyundai_XPATH)

    def selectToyota(self):
        self.click(By.XPATH,self.toyota_XPATH)

    def selectBMW(self):
        self.click(By.XPATH,self.Bmw_XPATH)

    def selectHonda(self):
        self.click(By.XPATH,self.honda_XPATH)
