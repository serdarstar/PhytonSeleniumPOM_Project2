from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):
    newCar_XPATH = "//div[normalize-space()='NEW CARS']"
    findNewCars_XPATH = "//div[contains(text(),'Find New Cars')]"


    def __init__(self, driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.click(By.XPATH, self.newCar_XPATH)
        self.click(By.XPATH, self.findNewCars_XPATH)


    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass
