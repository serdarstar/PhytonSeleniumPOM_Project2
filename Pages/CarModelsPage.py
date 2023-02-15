from selenium.webdriver.common.by import By

from Utilities import configReader


class CarModelsPage:
    carTitle_XPATH = "//h1[@class='o-dOKno o-bNCMFw o-fzoTzs o-dKUdmM']"
    carName_XPATH = "//div[1]/div[1]/div[1]/a[1]/h3[1]"
    carPrice_XPATH = "//div[1]/div[1]/div[1]/div[2]/span[1]"

    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        print("Printing title: "+self.driver.find_element(By.XPATH, self.carTitle_XPATH).text)
        return self.driver.find_element(By.XPATH, self.carTitle_XPATH).text

    def getCarNameAndPrices(self):
        carNames = self.driver.find_elements(By.XPATH, self.carName_XPATH)
        carPrices = self.driver.find_elements(By.XPATH, self.carPrice_XPATH)

        for i in range(1, len(carPrices)):
            print(carNames[i].text + "----Prices are-----" + carPrices[i].text)
