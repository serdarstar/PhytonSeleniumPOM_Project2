from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from Utilities import configReader
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator):
        self.driver.find_element(by, locator).click()
        log.logger.info("Clicking on an element: " + str(locator))

    def type(self, by, locator, value):
        self.driver.find_element(by, locator).send_keys(value)
        log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))

    def select(self, by, locator, value):
        global dropdown
        dropdown=self.driver.find_element(by, locator)

        select = Select(dropdown)
        select.select_by_visible_text(value)

        log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(value))

    def moveTo(self, by, locator):
        element = self.driver.find_element(by, locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("Moving to an element: " + str(locator))
