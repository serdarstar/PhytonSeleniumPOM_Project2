from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):
    phone_XPATH = "// input[ @ name = 'phone']"
    name_XPATH = "// input[ @ name = 'name']"
    email_XPATH = "// input[ @ name = 'email']"
    country_XPATH = "// select[ @ name = 'country']"
    city_XPATH = "// input[ @ name = 'city']"
    username_XPATH = "// div[ @ id = 'load_box'] // input[ @ name = 'username']"
    password_XPATH = "// div[ @ id = 'load_box'] // input[ @ name = 'password']"
    submit_XPATH = "// div[ @ id = 'load_box'] // input[ @ value = 'Submit']"

    def __init__(self, driver):
        super().__init__(driver)

    def fillForm(self, name, phoneNum, email, country, city, username, password):
        self.type(By.XPATH, self.name_XPATH,name)
        self.type(By.XPATH,self.phone_XPATH,phoneNum)
        self.type(By.XPATH,self.email_XPATH,email)
        self.select(By.XPATH,self.country_XPATH, country)
        self.type(By.XPATH,self.city_XPATH,city)
        self.type(By.XPATH,self.username_XPATH,username)
        self.type(By.XPATH,self.password_XPATH, password)
        #self.click(By.XPATH,self.submit_XPATH)
